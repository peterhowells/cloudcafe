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

import json

from cloudcafe.identity.v2_0.base import \
    BaseIdentityModel, BaseIdentityListModel

class Users(BaseIdentityListModel):

    TAG = 'users'

    def __init__(self, users=None):
        '''
        Models a users list returned by keystone
        '''
        super(Users, self).__init__()
        self.extend(users)

    @classmethod
    def _list_to_obj(cls, users_dict_list):
        users = Users()
        for user_dict in users_dict_list:
            user = user_dict

class User(BaseIdentityModel):

    TAG = 'user'

    def __init__(self):
        '''
        Models a user returned by keystone
        '''
        self.name = None
        self.id = None
        self.tenantId = None
        self.enabled = None
        self.email = None

    @classmethod
    def _dict_to_obj(self, user_dict):
        user = User()
        user.name = user_dict.get('name')
        user.id = user_dict.get('id')
        user.tenantId = user_dict.get('tenantId')
        user.enabled = user_dict.get('enabled')
        user.email = user_dict.get('email')

        return user