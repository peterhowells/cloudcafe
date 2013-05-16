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
from cloudcafe.identity.v2_0.tokens_api.models.base import \
    BaseIdentityModel, BaseIdentityListModel


class Tenants(BaseIdentityListModel):

    def __init__(self, tenants=None):
        '''An object that represents an tenants response object.
        '''
        super(Tenants, self).__init__()
        self.extend(tenants)

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._list_to_obj(json_dict.get('tenants'))

    @classmethod
    def _list_to_obj(cls, list_):
        ret = {'tenants': [Tenant(**tenant) for tenant in list_]}
        return Tenants(**ret)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        element = ElementTree.fromstring(serialized_str)
        cls._remove_identity_xml_namespaces(element)
        if element.tag != 'tenants':
            return None
        return cls._xml_list_to_obj(element.findall('tenant'))

    @classmethod
    def _xml_list_to_obj(cls, xml_list):
        kwargs = {'tenants': [Tenant._xml_ele_to_obj(ele)
                                 for ele in xml_list]}
        return Tenants(**kwargs)


class Tenant(BaseIdentityModel):

    def __init__(self, id_=None, name=None, description=None, enabled=None,
                 created=None):
        '''An object that represents an tenants response object.
        '''
        self.id_ = id_
        self.name = name
        self.description = description
        self.enabled = enabled
        self.created = created

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._dict_to_obj(json_dict.get('tenant'))

    @classmethod
    def _dict_to_obj(cls, dic):
        return Tenant(**dic)

    @classmethod
    def _xml_to_obj(cls, serialized_str):
        element = ElementTree.fromstring(serialized_str)
        cls._remove_identity_xml_namespaces(element)
        if element.tag != 'tenant':
            return None
        return cls._xml_ele_to_obj(element)

    @classmethod
    def _xml_ele_to_obj(cls, xml_ele):
        kwargs = {'name': xml_ele.get('name'),
                  'description': xml_ele.get('description'),
                  'created': xml_ele.get('created')}
        try:
            kwargs['id'] = int(xml_ele.get('id'))
        except (ValueError, TypeError):
            kwargs['id'] = xml_ele.get('id')
        if xml_ele.get('enabled') is not None:
            kwargs['enabled'] = json.loads(xml_ele.get('enabled').lower())
        return Tenant(**kwargs)
