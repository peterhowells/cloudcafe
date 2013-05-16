from unittest import TestCase
from cloudcafe.identity.v2_0.tenants_api.models.responses.roles import Role, Roles

class RolesTest(TestCase):
  
  def setUp(self):
    self.role_dict = {"id": "2", "name": "KeystoneServiceAdmin"}
    self.expected_role = Role(id_="2", name="KeystoneServiceAdmin")
    self.role_dict_list = [self.role_dict]
    self.expected_roles = Roles(roles=[self.expected_role])

  def test_dict_to_obj(self):
    assert self.expected_role == Role._dict_to_obj(self.role_dict)

  def test_list_to_obj(self):
    self.expected_roles == Roles._list_to_obj(self.role_dict_list)