from cloudcafe.identity.v2_0.tokens_api.models.requests.auth import Auth, Token
from cloudcafe.identity.v2_0.tokens_api.models.requests.credentials import \
    PasswordCredentials


def test_auth_to_json():
    expected_json = '{"auth": {"token": {"id": "a1b2c3d4f5"}, "tenantName": "tenant_name", "passwordCredentials": {"username": "username", "password": "password"}}}'

    password_credentials = PasswordCredentials("username", "password")
    token = Token("a1b2c3d4f5", "2015-01-01")
    auth = Auth(password_credentials, "tenant_name", token)

    assert auth._obj_to_json() == expected_json
