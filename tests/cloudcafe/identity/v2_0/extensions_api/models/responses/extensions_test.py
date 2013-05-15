from unittest import TestCase
from cloudcafe.identity.v2_0.extensions_api.models.responses.extensions import Extensions, Value

class ExtensionsTest(TestCase):
  def setUp(self):
    self.json_dict = {'extensions': [{'values':[]}]}
    self.extensions = Extensions(values=[Value()])


  def test_dict_to_extensions(self):
    assert Extensions._dict_to_obj(self.json_dict) == self.extensions