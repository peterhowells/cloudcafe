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

from cloudcafe.identity.v2_0.base import BaseIdentityModel
from cloudcafe.identity.v2_0.common.constants import V2_0Constants


class User(BaseIdentityModel):

    def __init__(self, id_=None, username=None, 
        email=None, enabled=None, password=None):
        """
        Models a new user model for Keystone
        """
        self.username = username
        self.email = email
        self.enabled = enabled
        self.password = password

    @classmethod
    def _obj_to_json(self):
        ret = {"user": self._obj_to_dict()}
        return json.dumps(ret)

    @classmethod
    def _obj_to_dict(self):
        ret = {}
        if self.id_ is not None:
            ret['id'] = self.id_
        if self.username is not None:
            ret['username'] = self.username
        if self.email is not None:
            ret['email'] = self.email
        if self.enabled is not None:
            ret['enabled'] = self.enabled
        if self.password is not None:
            ret['OS-KSADM:password'] = self.password

        return ret

    @classmethod
    def _obj_to_xml(self):
        element = self._obj_to_xml_ele()
        element.set('xmlns', V2_0Constants.XML_NS)
        element.set('xmlns:OS-KSADM', V2_0Constants.XML_NS_OS_KSADM)
        return ElementTree.tostring(element)

    @classmethod
    def _obj_to_xml_ele(self):
        element = ElementTree.Element('user')
        if self.username is not None:
            element.set('username', self.username)
        if self.email is not None:
            element.set('email', self.email)
        if self.enabled is not None:
            element.set('enabled', self.enabled)
        if self.password is not None:
            element.set('OS-KSADM:password', self.password)
        return element
