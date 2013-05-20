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

from cloudcafe.identity.v2_0.users_api.requests.user import \
    User as RequestUser
from cloudcafe.identity.v2_0.users_api.responses.role import Roles
from cloudcafe.identity.v2_0.users_api.responses.user import \
    Users as ResponseUsers, User as ResponseUser

_version = '2.0'


class UsersAPI_Client(AutoMarshallingRestClient):

    def __init__(self, url, auth_token, 
                 serialize_format=None, deserialize_format=None):
        """
        @param url: Base URL for the keystone service
        @type url: String
        @param auth_token: Auth token to be used for all requests
        @type auth_token: String
        @param serialize_format: Format for serializing requests
        @type serialize_format: String
        @param deserialize_format: Format for de-serializing responses
        @type deserialize_format: String
        """

        super(TenantsAPI_Client, self).__init__(
            serialize_format, deserialize_format)
        self.base_url = '{0}/{1}'.format(url,_version)
        self.default_headers['Content-Type'] = 'application/{0}'.format(
            serialize_format)
        self.default_headers['Accept'] = 'application/{0}'.format(
            serialize_format)
        self.default_headers['X-Auth-Token'] = auth_token

    def list_users(self, requestslib_kwargs=None):
        """
        @summary: Lists all users. Maps to /users
        @return: server_response
        @rtype: Response
        """

        url = '%s/users' % self.base_url
        server_response = self.request('GET', url, 
                                       response_entity_type=ResponseUsers,
                                       requestslib_kwargs=requestslib_kwargs)

        return server_response

    def add_user(self, username, email, enabled, 
                 password, requestslib_kwargs=None):

        '''
        @summary: creates a user in keystone
        @param username: The username of the new username
        @type username: String
        @param email: Email of the new username
        @type email: String
        @param enabled: true or false, user enabled
        @type enabled: Boolean
        @param password: password for the new username
        @type password: String
        @return: server_response object returning RepsonseUser entity
        @rtype: Response Object
        '''
        kwargs = {'username': username, 'email': email, 
                  'enabled': enabled, 'password': password}
        user = RequestUser(**kwargs)

        url = '%s/users' % self.base_url
        server_response = self.post(url, response_entity_type=RepsonseUser,
                                    request_entity=user_request_entity,
                                    requestslib_kwargs=requestslib_kwargs)

        return response

    def update_user(self, username, email, enabled, 
                    id_, requestslib_kwargs=None):

        '''
        @summary: updates a user in keystone
        @param username: The username of the new username
        @type username: String
        @param email: Email of the new username
        @type email: String
        @param enabled: true or false, user enabled
        @type enabled: Boolean
        @param id_: The ID of the user to update_user
        @type id_: String
        @return: server_response object returning RepsonseUser entity
        @rtype: Response Object
        '''
        kwargs = {'username': username, 'email': email, 
                  'enabled': enabled, 'id_': id_}
        user = RequestUser(**kwargs)

        url = '%s/users/%s' % (self.base_url, id_)
        server_response = self.post(url, response_entity_type=ResponseUser,
                                    request_entity=user_request_entity,
                                    requestslib_kwargs=requestslib_kwargs)

        return response

    def delete_user(self, user_id, requestslib_kwargs=None):
        '''
        @summary: Deletes a user from keystone
        @param user_id: The id of the user to delete_user
        @type user_id: String
        @return server_response
        @rtype: Response Object
        '''

        url = '%s/users/%s' % (self.base_url, user_id)
        server_response = self.delete(url, 
                                      requestslib_kwargs=requestslib_kwargs)

        return server_response

    def list_roles_for_user(self, user_id, service_id=None, 
                            requestslib_kwargs=None):
        '''
        @summary: list all the roles for a user
        @param user_id: The id of the user
        @type user_id: String
        @return: server_response object returning Roles
        @rtype: Response Object
        '''

        if service_id is not None:
            url = '%s/users/%s/roles?serviceId=%s' % (self.base_url, 
                                                      user_id, 
                                                      service_id)
        else:
            url = '%s/users/%s/roles' % (self.base_url, user_id)

        server_response = self.get(url, response_entity_type=Roles,
                                   requestslib_kwargs=requestslib_kwargs)

        return server_response