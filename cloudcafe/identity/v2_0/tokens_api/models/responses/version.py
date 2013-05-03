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

from cloudcafe.identity.v2_0.tokens_api.models.base import \
    BaseIdentityModel, BaseIdentityListModel


class Version(BaseIdentityModel):

    TAG = 'version'

    def __init__(self, status=None, updated=None, media_types=None, 
                 id=None, links=None):
        self.status = status
        self.updated = updated
        self.media_types = media_types
        self.id = id


class MediaTypes(BaseIdentityListModel):

    TAG = 'mediaTypes'

    def __init__(self, media_types=None):
        '''
        An Object that models a list of mediaTypes
        @param media_types List of mediaType
        '''
        super(MediaTypes, self).__init__()
        self.extend(media_types)


class MediaType(BaseIdentityModel):

    TAG = 'mediaType'

    def __init__(self):
        self.base = None
        self.type = None

    @classmethod
    def _dict_to_obj(cls, media_type_dic):
        media_type = MediaType()
        media_type.base = media_type_dic.get('base')
        media_type.type = media_type_dic.get('type')
        
        return media_type


class Links(BaseIdentityListModel):

    TAG = 'links'

    def __init__(self, links=None):
        '''
        A Object that models a list of version.Link()

        @param links
        '''
        super(Links, self).__init__()
        self.extend(links)

    @classmethod
    def _list_to_obj(cls, link_dict_list):
        links = Links()
        for link_dict in link_dict_list:
            link = Link._dict_to_obj(link_dict)
            links.append(link)

        return links

class Link(BaseIdentityModel):

    TAG = 'link'

    def __init__(self):
        self.href = None
        self.type = None
        self.rel = None

    def _dict_to_obj(cls, link_dict):
        link = Link()
        link.href = link_dict.get('href')
        link.rel = link_dict.get('rel')

        # Some links have a type, others dont
        if link_dict['type']:
            link.type = link_dict.get('type')
        
        return link
