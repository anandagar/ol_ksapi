# coding: utf-8


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ks_api_client.api_client import ApiClient
from ks_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OrderApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_order(self, consumerKey, sessionToken, orderId, **kwargs):  # noqa: E501
        """Cancel an order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_order(consumerKey, sessionToken, orderId, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param orderId: Order ID to cancel. (required)
        :type orderId: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_order_with_http_info(consumerKey, sessionToken, orderId, **kwargs)  # noqa: E501

    def cancel_order_with_http_info(self, consumerKey, sessionToken, orderId, **kwargs):  # noqa: E501
        """Cancel an order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_order_with_http_info(consumerKey, sessionToken, orderId, async_req=True)
        >>> result = thread.get()

        :param consumerKey: (required)
        :type consumerKey: str
        :param sessionToken: (required)
        :type sessionToken: str
        :param orderId: Order ID to cancel. (required)
        :type orderId: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'consumerKey',
            'sessionToken',
            'orderId'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_order" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `cancel_order`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `cancel_order`")  # noqa: E501
        # verify the required parameter 'orderId' is set
        if self.api_client.client_side_validation and ('orderId' not in local_var_params or  # noqa: E501
                                                        local_var_params['orderId'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `orderId` when calling `cancel_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'orderId' in local_var_params:
            path_params['orderId'] = local_var_params['orderId']  # noqa: E501

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/orders/1.1/orders/{orderId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def modify_order(self, consumerKey, sessionToken, ExistingOrder, **kwargs):  # noqa: E501
        """Modify an existing order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_order(consumerKey, sessionToken, ExistingOrder, async_req=True)
        >>> result = thread.get()

        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID for your application (required)
        :type sessionToken: str
        :param ExistingOrder: (required)
        :type ExistingOrder: ExistingOrder
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.modify_order_with_http_info(consumerKey, sessionToken, ExistingOrder, **kwargs)  # noqa: E501

    def modify_order_with_http_info(self, consumerKey, sessionToken, ExistingOrder, **kwargs):  # noqa: E501
        """Modify an existing order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_order_with_http_info(consumerKey, sessionToken, ExistingOrder, async_req=True)
        >>> result = thread.get()

        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID for your application (required)
        :type sessionToken: str
        :param ExistingOrder: (required)
        :type ExistingOrder: ExistingOrder
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'consumerKey',
            'sessionToken',
            'ExistingOrder'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_order" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `modify_order`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `modify_order`")  # noqa: E501
        # verify the required parameter 'ExistingOrder' is set
        if self.api_client.client_side_validation and ('ExistingOrder' not in local_var_params or  # noqa: E501
                                                        local_var_params['ExistingOrder'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ExistingOrder` when calling `modify_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ExistingOrder' in local_var_params:
            body_params = local_var_params['ExistingOrder']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/orders/1.1/orders', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def place_new_order(self, consumerKey, sessionToken, NewOrder, **kwargs):  # noqa: E501
        """Place a New order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.place_new_order(consumerKey, sessionToken, NewOrder, async_req=True)
        >>> result = thread.get()

        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID Generated with successful login. (required)
        :type sessionToken: str
        :param NewOrder: (required)
        :type NewOrder: NewOrder
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.place_new_order_with_http_info(consumerKey, sessionToken, NewOrder, **kwargs)  # noqa: E501

    def place_new_order_with_http_info(self, consumerKey, sessionToken, NewOrder, **kwargs):  # noqa: E501
        """Place a New order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.place_new_order_with_http_info(consumerKey, sessionToken, NewOrder, async_req=True)
        >>> result = thread.get()

        :param consumerKey: Unique ID for your application (required)
        :type consumerKey: str
        :param sessionToken: Session ID Generated with successful login. (required)
        :type sessionToken: str
        :param NewOrder: (required)
        :type NewOrder: NewOrder
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'consumerKey',
            'sessionToken',
            'NewOrder'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_new_order" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'consumerKey' is set
        if self.api_client.client_side_validation and ('consumerKey' not in local_var_params or  # noqa: E501
                                                        local_var_params['consumerKey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `consumerKey` when calling `place_new_order`")  # noqa: E501
        # verify the required parameter 'sessionToken' is set
        if self.api_client.client_side_validation and ('sessionToken' not in local_var_params or  # noqa: E501
                                                        local_var_params['sessionToken'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sessionToken` when calling `place_new_order`")  # noqa: E501
        # verify the required parameter 'NewOrder' is set
        if self.api_client.client_side_validation and ('NewOrder' not in local_var_params or  # noqa: E501
                                                        local_var_params['NewOrder'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `NewOrder` when calling `place_new_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'consumerKey' in local_var_params:
            header_params['consumerKey'] = local_var_params['consumerKey']  # noqa: E501
        if 'sessionToken' in local_var_params:
            header_params['sessionToken'] = local_var_params['sessionToken']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'NewOrder' in local_var_params:
            body_params = local_var_params['NewOrder']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/orders/1.1/orders', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
