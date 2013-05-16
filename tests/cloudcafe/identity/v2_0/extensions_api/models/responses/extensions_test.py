from unittest import TestCase
from cloudcafe.identity.v2_0.extensions_api.models.responses.extensions import Extensions, Value, Values

class ExtensionsTest(TestCase):
  def setUp(self):
    self.values = Values(values=[Value()])
    self.json_dict = {'extensions': [{'values':self.values}]}
    self.extensions = Extensions(values=self.values)

    self.serialized_str = '{"extensions": {"extensions": [{"values": []}]}}'

  def test_dict_to_obj(self):
    assert Extensions._dict_to_obj(self.json_dict) == self.extensions

  def test_json_to_obj(self):
    assert Extensions._json_to_obj(self.serialized_str) == self.extensions

