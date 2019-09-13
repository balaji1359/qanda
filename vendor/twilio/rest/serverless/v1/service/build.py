# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class BuildList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid):
        """
        Initialize the BuildList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.

        :returns: twilio.rest.serverless.v1.service.build.BuildList
        :rtype: twilio.rest.serverless.v1.service.build.BuildList
        """
        super(BuildList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Builds'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams BuildInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.build.BuildInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists BuildInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.build.BuildInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of BuildInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return BuildPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BuildInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return BuildPage(self._version, response, self._solution)

    def create(self, asset_versions=values.unset, function_versions=values.unset,
               dependencies=values.unset):
        """
        Create a new BuildInstance

        :param unicode asset_versions: List of Asset Version Sids.
        :param unicode function_versions: List of Function Version Sids.
        :param unicode dependencies: List of Dependencies.

        :returns: Newly created BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        data = values.of({
            'AssetVersions': serialize.map(asset_versions, lambda e: e),
            'FunctionVersions': serialize.map(function_versions, lambda e: e),
            'Dependencies': dependencies,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return BuildInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def get(self, sid):
        """
        Constructs a BuildContext

        :param sid: Build Sid.

        :returns: twilio.rest.serverless.v1.service.build.BuildContext
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        return BuildContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a BuildContext

        :param sid: Build Sid.

        :returns: twilio.rest.serverless.v1.service.build.BuildContext
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        return BuildContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.BuildList>'


class BuildPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the BuildPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.

        :returns: twilio.rest.serverless.v1.service.build.BuildPage
        :rtype: twilio.rest.serverless.v1.service.build.BuildPage
        """
        super(BuildPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BuildInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.build.BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        return BuildInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.BuildPage>'


class BuildContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the BuildContext

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param sid: Build Sid.

        :returns: twilio.rest.serverless.v1.service.build.BuildContext
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        super(BuildContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Builds/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a BuildInstance

        :returns: Fetched BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return BuildInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the BuildInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildContext {}>'.format(context)


class BuildInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Status(object):
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the BuildInstance

        :returns: twilio.rest.serverless.v1.service.build.BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        super(BuildInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'status': payload['status'],
            'asset_versions': payload['asset_versions'],
            'function_versions': payload['function_versions'],
            'dependencies': payload['dependencies'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: BuildContext for this BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        if self._context is None:
            self._context = BuildContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: Build Sid.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def status(self):
        """
        :returns: The current state of the Build.
        :rtype: BuildInstance.Status
        """
        return self._properties['status']

    @property
    def asset_versions(self):
        """
        :returns: List of Asset Version Sids.
        :rtype: dict
        """
        return self._properties['asset_versions']

    @property
    def function_versions(self):
        """
        :returns: List of Function Version Sids.
        :rtype: dict
        """
        return self._properties['function_versions']

    @property
    def dependencies(self):
        """
        :returns: List of Dependencies.
        :rtype: dict
        """
        return self._properties['dependencies']

    @property
    def date_created(self):
        """
        :returns: The date that this Build was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this Build was updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this Build.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a BuildInstance

        :returns: Fetched BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the BuildInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildInstance {}>'.format(context)
