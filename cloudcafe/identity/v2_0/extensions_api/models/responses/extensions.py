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
from cloudcafe.identity.v2_0.shared.base import \
    BaseIdentityModel, BaseIdentityListModel

class Extensions(BaseIdentityModel):

    TAG = 'extensions'

    def __init__(self):
        '''
        Models a extensions object returned by keystone
        '''
        self.values = Values()

    @classmethod
    def _json_to_obj(cls, serialized_str):
        json_dict = json.loads(serialized_str)
        return cls._dict_to_obj(json_dict.get(cls.TAG))

    @classmethod
    def _dict_to_obj(cls, json_dict):
        extensions = Extensions()
        extensions.values = Values._list_to_obj(
            json_dict.get(Values.TAG))

        return extensions

class Values(BaseIdentityListModel):

    TAG = 'values'

    def __init__(self, values=None):
        '''
        Models a list of values returned by keystone
        '''
        super(Values, self).__init__()
        self.extend(values)

    @classmethod
    def _list_to_obj(self, value_dict_list):
        values = Values()
        for value_dict in value_dict_list:
            value = Value._dict_to_obj(value_dict)
            values.append(value)

        return values


class Value(BaseIdentityModel):

    TAG = 'value'

    def __init__(self):
        '''
        Models a value  object returned by keystone
        '''
        self.updated = None
        self.name = None
        self.links = Links()
        self.namespace = None
        self.alias = None
        self.description = None

    @classmethod
    def _dict_to_obj(cls, json_dict):
        value = Value()
        value.updated = json_dict.get('updated')
        value.name = json_dict.get('name')
        value.namespace = json_dict.get('namespace')
        value.alias = json_dict.get('alias')
        value.description = json_dict.get('description')
        value.links = Links._list_to_obj(json_dict.get(Links.TAG))

class Links(BaseIdentityListModel):

    TAG = 'links'

    def __init__(self, links=None):
        '''
        Models a list of links returned by keystone
        '''
        super(Links, self).__init__()
        self.extend(links)

    @classmethod
    def _list_to_obj(self, link_dict_list):
        links = Links()
        for link_dict in link_dict_list:
            link = Link._dict_to_obj(link_dict)
            links.append(link)

        return links

class Link(BaseIdentityModel):

    TAG = 'link'

    def __init__(self):
        '''
        Models a link object returned by keystone
        '''
        self.href = None
        self.type = None
        self.rel = None

    @classmethod
    def _dict_to_obj(cls, json_dict):
        link = Link()
        link.href = json_dict.get('href')
        link.type = json_dict.get('type')
        link.rel = json_dict.get('rel')

        return link