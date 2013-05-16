from cloudcafe.identity.v2_0.tokens_api.models.requests.role import Roles


def test_json_to_role():
    roles_json = """
    {
    "roles":[{
            "id": "123",
            "name": "compute:admin",
            "description": "Nova Administrator"
        }
    ],
    "roles_links":[]
    }
    """

    roles = Roles._json_to_obj(roles_json)
    role = roles[0]

    assert role.id == "123"
    assert role.name == "compute:admin"
    assert role.description == "Nova Administrator"
