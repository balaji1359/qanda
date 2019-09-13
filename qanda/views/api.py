from qanda import app, g_model, docs
from flask import request
from flask_apispec import use_kwargs, marshal_with
from marshmallow import fields, Schema
import simplejson as json  # for handling Decimal types from dynamodb
from typing import List, Dict, Any
import requests


class AnswerSchema(Schema):
    body = fields.Str(required=True)
    question_id = fields.Str(dump_only=True)
    id = fields.Str(dump_only=True)
    created = fields.Int(dump_only=True)


class QuestionSchema(Schema):
    body = fields.Str(required=True)
    tags = fields.Str(many=True, required=False)
    created = fields.Int(dump_only=True)
    id = fields.Str(dump_only=True)
    answers = fields.Nested(AnswerSchema, many=True)


class QuestionListSchema(Schema):
    start_key = fields.Str()
    source = fields.Str()
    questions = fields.Nested(QuestionSchema, many=True)


class QuestionBatchLookupSchema(Schema):
    ids = fields.List(fields.Str, load_only=True)


@app.route("/api/question/ask", methods=["POST"])
@use_kwargs(QuestionSchema())
@marshal_with(QuestionSchema())
def api_question_ask(body, tags=[]):
    """Ask a question from the web."""
    q = g_model.new_question_from_web(body=body, remote_ip=request.remote_addr)
    return q


@app.route("/api/question", methods=["GET"])
@use_kwargs(QuestionListSchema())
@marshal_with(QuestionListSchema())
def api_list_questions(start_key: str = None, source: str = None) -> Dict[str, Any]:
    """Get a list of recent questions."""
    start_key = json.loads(start_key) if start_key else None
    res = g_model.get_questions(source=source, start_key=start_key)
    return dict(
        questions=res["Items"],
        start_key=json.dumps(res["LastEvaluatedKey"])
        if "LastEvaluatedKey" in res
        else None,
    )


@app.route("/api/question_batch", methods=["POST"])
@use_kwargs(QuestionBatchLookupSchema())
@marshal_with(QuestionListSchema())
def api_get_question_batch(ids: List[str]) -> Dict[str, Any]:
    """Get a list of recent questions."""
    res = g_model.get_questions_by_id(question_ids=ids)
    return dict(questions=res)


@app.route("/api/question/<string:pk>", methods=["GET"])
@marshal_with(QuestionSchema())
def api_question_get(pk: str) -> Dict:
    """Fetch a question (and answers)."""
    question = g_model.get_question(id=pk)
    return question


@app.route("/api/question/<string:pk>/reply", methods=["POST"])
@use_kwargs(AnswerSchema())
def api_question_answer_post(pk: str, body: str) -> str:
    """Fetch a question (and answers)."""
    question = g_model.get_question(id=pk)
    g_model.new_answer_from_web(
        body=body, remote_ip=request.remote_addr, question=question
    )
    return "ok"


class ContactSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    message = fields.Str(required=True)


@app.route("/api/contact", methods=["POST"])
@use_kwargs(ContactSchema())
def api_contact(message: str, name: str = None, email: str = None) -> None:
    """Contact form handler."""
    cstr = f"""Contact form!
Name: {name}
Email: {email}
{message}"""
    slack_log_endpoint = app.config.get("SLACK_LOG_ENDPOINT")
    requests.post(slack_log_endpoint, data=json.dumps({"text": cstr}))


docs.register(api_question_ask)
docs.register(api_question_answer_post)
docs.register(api_question_get)
docs.register(api_get_question_batch)
docs.register(api_list_questions)
docs.register(api_contact)
