from unittest import TestCase
from cloudcafe.identity.v2_0.tenants_api.models.responses.tenant import Tenant, TenantsLink

class TenantTest(TestCase):
  def setUp(self):
    self.tenant_id = "3"
    self.tenant_name = "project-y"
    self.tenant_description = "None"
    self.tenant_enabled = False

    self.tenant_dict = {
                    "id_": self.tenant_id,
                    "name": self.tenant_name,
                    "description": self.tenant_description,
                    "enabled": self.tenant_enabled,
                    }


    self.tenant_serialized_str = '{"tenant": {"id_":"3", "name": "project-y", "description": "None", "enabled": false}}'

    self.expected_tenant = Tenant(id_=self.tenant_id,
                                  name=self.tenant_name,
                                  description=self.tenant_description,
                                  enabled=self.tenant_enabled)

    self.expected_tenant_link = TenantsLink("HREF", "TYPE", "REL")

  def test_dict_to_obj(self):
    assert self.expected_tenant == Tenant._dict_to_obj(self.tenant_dict)

  def test_json_to_obj(self):
    assert self.expected_tenant == Tenant._json_to_obj(self.tenant_serialized_str)