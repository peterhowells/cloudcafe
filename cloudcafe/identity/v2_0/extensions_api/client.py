"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cafe.engine.clients.rest import AutoMarshallingRestClient
from cloudcafe.identity.v2_0.extensions_api.responses.extensions import \
    Extensions

_version = 'v2.0'


class ExtensionAPI_Client(AutoMarshallingRestClient):

    def __init__(self, url, serialize_format, deserialize_format=None,
                 auth_token=None):
        """
        @param url: Base URL for the compute service
        @type url: String
        @param auth_token: Auth token to be used for all requests
        @type auth_token: String
        @param serialize_format: Format for serializing requests
        @type serialize_format: String
        @param deserialize_format: Format for de-serializing responses
        @type deserialize_format: String
        """

        super(ExtensionAPI_Client, self).__init__(
            serialize_format, deserialize_format)
        self.base_url = '{0}/{1}'.format(url,_version)
        self.default_headers['Content-Type'] = 'application/{0}'.format(
            serialize_format)
        self.default_headers['Accept'] = 'application/{0}'.format(
            serialize_format)
        self.default_headers['X-Auth-Token'] = auth_token

    def list_extensions(self, requestslib_kwards=None):
        """
        @summary: Lists all the extensions. Maps to /extensions
        @return: server_response
        @rtype: Response
        """
        url = '%s/extensions' % self.base_url
        server_response = self.request('GET', url, 
                                       response_entity_type=Extensions,
                                       requestslib_kwargs=requestslib_kwargs)

        return server_response
