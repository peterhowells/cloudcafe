from unittest import TestCase
from httpretty import HTTPretty
from cloudcafe.identity.v2_0.tenants_api.client import TenantsAPI_Client

IDENTITY_ENDPOINT_URL = "http://localhost:5000"

class TenantsClientTest(TestCase):
  def setUp(self):
    self.url = IDENTITY_ENDPOINT_URL
    self.serialize_format = "json"
    self.deserialize_format = "json"
    self.auth_token = "AUTH_TOKEN"
    self.tenant_api_client = TenantsAPI_Client(url=self.url,
                                               auth_token=self.auth_token,
                                               serialize_format=self.serialize_format,
                                               deserialize_format=self.deserialize_format)
    self.tenant_id = "1"
    HTTPretty.enable()

  def test_list_tenants(self):
    url = "{0}/v2.0/tenants".format(self.url)
    HTTPretty.register_uri(HTTPretty.GET, url, body=self._build_list_tenants_expected_response())

    actual_response = self.tenant_api_client.list_tenants()

    assert HTTPretty.last_request.headers['Content-Type'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['Accept'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['X-Auth-Token'] == self.auth_token
    assert 200 == actual_response.status_code
    assert url == actual_response.url

  def test_get_tenant(self):
    url = "{0}/v2.0/tenants/{1}".format(self.url, self.tenant_id)
    HTTPretty.register_uri(HTTPretty.GET, url, body=self._build_get_tenant_expected_response())

    actual_response = self.tenant_api_client.get_tenant(tenant_id=self.tenant_id)

    assert HTTPretty.last_request.headers['Content-Type'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['Accept'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['X-Auth-Token'] == self.auth_token
    assert 200 == actual_response.status_code
    assert url == actual_response.url

  def test_create_tenant(self):
    url = "{0}/v2.0/tenants".format(self.url)
    HTTPretty.register_uri(HTTPretty.POST, url)

    actual_response = self.tenant_api_client.create_tenant(name="Admin")

    assert HTTPretty.last_request.headers['Content-Type'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['Accept'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['X-Auth-Token'] == self.auth_token
    assert 200 == actual_response.status_code
    assert url == actual_response.url

  def test_update_tenant(self):
    url = "{0}/v2.0/tenants/{1}".format(self.url, self.tenant_id)
    HTTPretty.register_uri(HTTPretty.PUT, url)

    actual_response = self.tenant_api_client.update_tenant(tenant_id=self.tenant_id)

    assert HTTPretty.last_request.headers['Content-Type'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['Accept'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['X-Auth-Token'] == self.auth_token
    assert 200 == actual_response.status_code
    assert url == actual_response.url

  def test_update_tenant(self):
    url = "{0}/v2.0/tenants/{1}".format(self.url, self.tenant_id)
    HTTPretty.register_uri(HTTPretty.DELETE, url)

    actual_response = self.tenant_api_client.delete_tenant(tenant_id=self.tenant_id)

    assert HTTPretty.last_request.headers['Content-Type'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['Accept'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['X-Auth-Token'] == self.auth_token
    assert 200 == actual_response.status_code
    assert url == actual_response.url

  def test_get_users_for_tenant(self):
    url = "{0}/v2.0/tenants/{1}/users".format(self.url, self.tenant_id)
    HTTPretty.register_uri(HTTPretty.GET, url, body=self._build_list_of_users_for_tenant())

    actual_response = self.tenant_api_client.get_users_for_tenant(tenant_id=self.tenant_id)

    assert HTTPretty.last_request.headers['Content-Type'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['Accept'] == 'application/{0}'.format(self.
    serialize_format)
    assert HTTPretty.last_request.headers['X-Auth-Token'] == self.auth_token
    assert 200 == actual_response.status_code
    assert url == actual_response.url

  def _build_list_tenants_expected_response(self):
    return [{"tenants": {"enabled": True,
                         "description": "None",
                         "name": "customer-x",
                         "id": "1"}}]

  def _build_get_tenant_expected_response(self):
    return {"tenant": {"enabled": True,
                        "description": "None",
                        "name": "customer-x",
                        "id": "1"}}

  def _build_list_of_users_for_tenant(self):
    return {"users": [{"name": "user_name",
                        "id": "user_id",
                        "tenantId": "tenant_id",
                        "enabled": True,
                        "email": "user_email"}]}