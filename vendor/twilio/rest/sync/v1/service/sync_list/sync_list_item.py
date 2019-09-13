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


class SyncListItemList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, list_sid):
        """
        Initialize the SyncListItemList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Sync Service that the resource is associated with
        :param list_sid: The SID of the Sync List that contains the List Item

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemList
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemList
        """
        super(SyncListItemList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'list_sid': list_sid, }
        self._uri = '/Services/{service_sid}/Lists/{list_sid}/Items'.format(**self._solution)

    def create(self, data, ttl=values.unset, item_ttl=values.unset,
               collection_ttl=values.unset):
        """
        Create a new SyncListItemInstance

        :param dict data: A JSON string that represents an arbitrary, schema-less object that the List Item stores
        :param unicode ttl: An alias for item_ttl
        :param unicode item_ttl: How long, in seconds, before the List Item expires
        :param unicode collection_ttl: How long, in seconds, before the List Item's parent Sync List expires

        :returns: Newly created SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        """
        data = values.of({
            'Data': serialize.object(data),
            'Ttl': ttl,
            'ItemTtl': item_ttl,
            'CollectionTtl': collection_ttl,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
        )

    def stream(self, order=values.unset, from_=values.unset, bounds=values.unset,
               limit=None, page_size=None):
        """
        Streams SyncListItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param SyncListItemInstance.QueryResultOrder order: The order to return the List Items
        :param unicode from_: The index of the first Sync List Item resource to read
        :param SyncListItemInstance.QueryFromBoundType bounds: Whether to include the List Item referenced by the from parameter
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(order=order, from_=from_, bounds=bounds, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, order=values.unset, from_=values.unset, bounds=values.unset,
             limit=None, page_size=None):
        """
        Lists SyncListItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param SyncListItemInstance.QueryResultOrder order: The order to return the List Items
        :param unicode from_: The index of the first Sync List Item resource to read
        :param SyncListItemInstance.QueryFromBoundType bounds: Whether to include the List Item referenced by the from parameter
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance]
        """
        return list(self.stream(order=order, from_=from_, bounds=bounds, limit=limit, page_size=page_size, ))

    def page(self, order=values.unset, from_=values.unset, bounds=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SyncListItemInstance records from the API.
        Request is executed immediately

        :param SyncListItemInstance.QueryResultOrder order: The order to return the List Items
        :param unicode from_: The index of the first Sync List Item resource to read
        :param SyncListItemInstance.QueryFromBoundType bounds: Whether to include the List Item referenced by the from parameter
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemPage
        """
        params = values.of({
            'Order': order,
            'From': from_,
            'Bounds': bounds,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SyncListItemPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncListItemInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SyncListItemPage(self._version, response, self._solution)

    def get(self, index):
        """
        Constructs a SyncListItemContext

        :param index: The index of the Sync List Item resource to fetch

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemContext
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemContext
        """
        return SyncListItemContext(
            self._version,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            index=index,
        )

    def __call__(self, index):
        """
        Constructs a SyncListItemContext

        :param index: The index of the Sync List Item resource to fetch

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemContext
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemContext
        """
        return SyncListItemContext(
            self._version,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            index=index,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncListItemList>'


class SyncListItemPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SyncListItemPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Sync Service that the resource is associated with
        :param list_sid: The SID of the Sync List that contains the List Item

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemPage
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemPage
        """
        super(SyncListItemPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncListItemInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        """
        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncListItemPage>'


class SyncListItemContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, list_sid, index):
        """
        Initialize the SyncListItemContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Sync Service with the Sync List Item resource to fetch
        :param list_sid: The SID of the Sync List with the Sync List Item resource to fetch
        :param index: The index of the Sync List Item resource to fetch

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemContext
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemContext
        """
        super(SyncListItemContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'list_sid': list_sid, 'index': index, }
        self._uri = '/Services/{service_sid}/Lists/{list_sid}/Items/{index}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a SyncListItemInstance

        :returns: Fetched SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            index=self._solution['index'],
        )

    def delete(self):
        """
        Deletes the SyncListItemInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, data=values.unset, ttl=values.unset, item_ttl=values.unset,
               collection_ttl=values.unset):
        """
        Update the SyncListItemInstance

        :param dict data: A JSON string that represents an arbitrary, schema-less object that the List Item stores
        :param unicode ttl: An alias for item_ttl
        :param unicode item_ttl: How long, in seconds, before the List Item expires
        :param unicode collection_ttl: How long, in seconds, before the List Item's parent Sync List expires

        :returns: Updated SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        """
        data = values.of({
            'Data': serialize.object(data),
            'Ttl': ttl,
            'ItemTtl': item_ttl,
            'CollectionTtl': collection_ttl,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            index=self._solution['index'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncListItemContext {}>'.format(context)


class SyncListItemInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class QueryResultOrder(object):
        ASC = "asc"
        DESC = "desc"

    class QueryFromBoundType(object):
        INCLUSIVE = "inclusive"
        EXCLUSIVE = "exclusive"

    def __init__(self, version, payload, service_sid, list_sid, index=None):
        """
        Initialize the SyncListItemInstance

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        """
        super(SyncListItemInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'index': deserialize.integer(payload['index']),
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'list_sid': payload['list_sid'],
            'url': payload['url'],
            'revision': payload['revision'],
            'data': payload['data'],
            'date_expires': deserialize.iso8601_datetime(payload['date_expires']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'created_by': payload['created_by'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'list_sid': list_sid,
            'index': index or self._properties['index'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SyncListItemContext for this SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemContext
        """
        if self._context is None:
            self._context = SyncListItemContext(
                self._version,
                service_sid=self._solution['service_sid'],
                list_sid=self._solution['list_sid'],
                index=self._solution['index'],
            )
        return self._context

    @property
    def index(self):
        """
        :returns: The automatically generated index of the List Item
        :rtype: unicode
        """
        return self._properties['index']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Sync Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def list_sid(self):
        """
        :returns: The SID of the Sync List that contains the List Item
        :rtype: unicode
        """
        return self._properties['list_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL of the List Item resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def revision(self):
        """
        :returns: The current revision of the item, represented as a string
        :rtype: unicode
        """
        return self._properties['revision']

    @property
    def data(self):
        """
        :returns: An arbitrary, schema-less object that the List Item stores
        :rtype: dict
        """
        return self._properties['data']

    @property
    def date_expires(self):
        """
        :returns: The ISO 8601 date and time in GMT when the List Item expires
        :rtype: datetime
        """
        return self._properties['date_expires']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: The identity of the List Item's creator
        :rtype: unicode
        """
        return self._properties['created_by']

    def fetch(self):
        """
        Fetch a SyncListItemInstance

        :returns: Fetched SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SyncListItemInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, data=values.unset, ttl=values.unset, item_ttl=values.unset,
               collection_ttl=values.unset):
        """
        Update the SyncListItemInstance

        :param dict data: A JSON string that represents an arbitrary, schema-less object that the List Item stores
        :param unicode ttl: An alias for item_ttl
        :param unicode item_ttl: How long, in seconds, before the List Item expires
        :param unicode collection_ttl: How long, in seconds, before the List Item's parent Sync List expires

        :returns: Updated SyncListItemInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemInstance
        """
        return self._proxy.update(data=data, ttl=ttl, item_ttl=item_ttl, collection_ttl=collection_ttl, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncListItemInstance {}>'.format(context)
