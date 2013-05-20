from unittest import TestCase
from cloudcafe.identity.v2_0.tokens_api.client import TokenAPI_Client
from httpretty import HTTPretty

IDENTITY_ENDPOINT_URL = "http://localhost:9292"

class ClientTest(TestCase):
  def setUp(self):

    self.token_api_client = TokenAPI_Client(
      url=IDENTITY_ENDPOINT_URL,
      auth_token="36a04b4e71484ab9aacb1d0ac95733fc",
      serialize_format="json",
      deserialize_format="json",
      )

    self.expected_response_body= 'MOCK_RESPONSE_CONTENT'

    HTTPretty.enable()

  def test_list_of_images(self):
    HTTPretty.register_uri(HTTPretty.POST, "{0}/v2.0/tokens".format(IDENTITY_ENDPOINT_URL),
                          body=self.expected_response_body,
                          content_type="application/json")

    actual_response = self.token_api_client.authenticate("username", "password", "tenant_name")

    assert HTTPretty.last_request.headers['X-Auth-Token'] == '36a04b4e71484ab9aacb1d0ac95733fc'
    assert HTTPretty.last_request.headers['Content-Type'] == 'application/json'
    assert HTTPretty.last_request.headers['Accept'] == 'application/json'

    assert actual_response.status_code == 200
    assert self.expected_response_body==actual_response.content
