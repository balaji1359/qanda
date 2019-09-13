from qanda.slack import (
    SlackSlashcommandSchema,
    SlackSlashcommandResponseSchema,
    SlackApp,
)
from qanda import g_model, app, g_notify, g_invoker
import qanda.table
from flask_apispec import use_kwargs, marshal_with
from flask import request, redirect, url_for, jsonify
import requests
from slackclient import SlackClient
from urllib.parse import urlencode
import logging

log = logging.getLogger(__name__)


@app.route("/slack/slash_ask", methods=["POST"])
@use_kwargs(SlackSlashcommandSchema())
@marshal_with(SlackSlashcommandResponseSchema)
def slack_slash_ask(**kwargs):
    """Slashcommand handler."""
    g_invoker.invoke_async(
        func="SLACK_SLASH_FUNCTION", payload=dict(slack_args=kwargs, command="ask")
    )
    return {
        "response_type": "in_channel",
        "text": "Your question has been asked. Please wait for random humans to answer it.",
    }


@app.route("/slack/action", methods=["POST"])
def slack_action():
    """Handle custom action component."""
    info = request.get_json()

    response_url = info["response_url"]
    callback_id = info["callback_id"]

    requests.post(response_url, jsonify({"text": "Ok!"}))

    return "ok"


@app.route("/slack/event", methods=["POST"])
def slack_event():
    """Receive event from slack and queue it for later processing."""
    evt_callback = request.get_json()

    # check it's really slack and they have our secret
    token = evt_callback["token"]
    if token != app.config["SLACK_VERIFICATION_TOKEN"]:
        log.error(f"got invalid SLACK_VERIFICATION_TOKEN: {token}")
        return "invalid token", 400

    type = evt_callback["type"]

    # subscribe challenge
    if type == "url_verification":
        return evt_callback["challenge"]

    # skip processing some dumb events here
    if "event" in evt_callback:
        evt = evt_callback["event"]
        type = evt["type"]
        if type == "message":
            if "bot_id" in evt:
                # this is a message FROM the bot... don't care since we sent it
                print("skipping bot_id message")
                return "ok"

    # process event async
    g_invoker.invoke_async(
        func="SLACK_EVENT_FUNCTION", payload=dict(slack_event_callback=evt_callback)
    )

    return "ok"


def get_oauth_redirect_url():
    return url_for("slack_oauth", _external=True)


@app.route("/slack/install", methods=["GET"])
def slack_install():
    """Begin OAuth flow for install."""

    # chat:write:user got changed to chat:write
    if app.config["WORKSPACE_PERMISSIONS"]:
        chat_write = "chat:write"  # new
    else:
        chat_write = "chat:write:bot"  # old

    scopes = f"commands bot {chat_write}"
    # scopes += ' channels:history'

    url = "https://slack.com/oauth/authorize?" + urlencode(
        dict(
            client_id=app.config["SLACK_OAUTH_CLIENT_ID"],
            scope=scopes,
            redirect_uri=app.config["SLACK_OAUTH_REDIRECT_URL"],
            _external=True,
        )
    )
    return redirect(url)


@app.route("/slack/oauth", methods=["GET"])
def slack_oauth():
    """Handle Slack oauth.

    Exchange code for auth token. Save in auth_token.
    """
    req = request.args
    if "error" in req:
        return "im so sorry :("

    # exchange code for access token
    code = req["code"]
    sc = SlackClient("")
    auth_response = sc.api_call(
        "oauth.access",
        client_id=app.config["SLACK_OAUTH_CLIENT_ID"],
        client_secret=app.config["SLACK_OAUTH_CLIENT_SECRET"],
        redirect_uri=app.config["SLACK_OAUTH_REDIRECT_URL"],
        code=code,
    )
    if "error" in auth_response:
        log.error(f"got error in auth response: {auth_response['error']}")
        return auth_response["error"]

    # save
    g_model.save_slack_tokens(auth_response)
    return redirect("http://www.appqanda.com/slack")
