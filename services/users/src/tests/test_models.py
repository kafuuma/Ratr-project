import json


def test_empty_db(client):
    response = client.get('/api/v1/users')
    assert not response.get_json()['user']


def test_create_user(client):
    data = {
        "user": {
            "mobile_number": "0788088831",
            "email": "arkafuuma@gmail.com",
            "username": "henry",
            "password": "password@1"
        }
    }
    response = client.post('/api/v1/users',
                           data=json.dumps(data),
                           headers={'content-type': 'application/json'})
    assert response.status_code == 200
    assert response.get_json()['user']['id'] == 1
