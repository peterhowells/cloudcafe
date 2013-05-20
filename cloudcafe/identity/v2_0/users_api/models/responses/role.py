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
from xml.etree import ElementTree

from cloudcafe.identity.v2_0.base import \
BaseIdentityModel, BaseIdentityListModel
from cloudcafe.identity.v2_0.common.constants import V2_0Constants


class Roles(BaseIdentityListModel):

    def __init__(self, roles=None):
        super(Roles, self).__init__()
        self.extend(roles)

    def _list_to_obj(self, roles_dict_list):
        roles = Roles()
        for role_dict in roles_dict_list:
            role = Role._dict_to_obj(role_dict)
            roles.append(role)

        return roles


class Role(BaseIdentityModel):

    def __init__(self, id_=None, name=None, description=None):
        self.id_ = id_
        self.name = name
        self.description = description

    def _json_to_obj(self, serialized_str):
        json_dict = json.loads(serialized_str)
        return self._dict_to_obj(json_dict)

    def _dict_to_obj(self, role_dict):
        role=Role(id_ = role_dict.get('id'), 
                  name = role_dict.get('name'),
                  description = role_dict.get('description'))

        return role
