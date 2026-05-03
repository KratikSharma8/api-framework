import requests


def test_get_user_returns_200(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/1')
    assert response.status_code == 200

def test_get_user_has_data_key(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/1')
    data = response.json()
    assert 'data' in data

def test_user_has_email(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/1')
    data = response.json()
    assert 'email' in data['data']

def test_user_email_has_at_symbol(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/1')
    data = response.json()
    assert '@' in data['data']['email']

def test_user_name_is_correct(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/1')
    data = response.json()
    assert data['data']['name'] == 'Kratik Sharma'

def test_user_not_found_returns_404(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/999')
    assert response.status_code == 404

def test_missing_user_has_error_message(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/999')
    data = response.json()
    assert 'detail' in data

def test_get_all_users_returns_200(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    assert response.status_code == 200

def test_user_list_has_total_key(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    data = response.json()
    assert 'total' in data

def test_user_list_is_not_empty(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    data = response.json()
    assert len(data['data']) > 0

def test_user_list_total_is_correct(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    data = response.json()
    assert data['total'] == 3

def test_each_user_has_required_fields(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    data = response.json()
    for user in data['data']:
        assert 'id' in user
        assert 'name' in user
        assert 'email' in user
        assert 'role' in user

def test_each_user_email_is_valid(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    data = response.json()
    for user in data['data']:
        assert '@' in user['email']

def test_each_user_has_a_role(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    data = response.json()
    for user in data['data']:
        assert user['role'] in ['admin', 'user']

def test_invalid_user_returns_404(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/999')
    assert response.status_code == 404

def test_invalid_user_returns_error_detail(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/999')
    data = response.json()
    assert 'detail' in data
    assert data['detail'] == 'User not found'

def test_user_zero_returns_404(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/0')
    assert response.status_code == 404

def test_negative_user_id_returns_404(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/-1')
    assert response.status_code == 404

def test_create_user_returns_201(api_base_url, new_user):
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    assert response.status_code == 201

def test_create_user_has_id(api_base_url, new_user):
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    data = response.json()
    assert 'id' in data

def test_create_user_name_matches(api_base_url, new_user):
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    data = response.json()
    assert data['name'] == new_user['name']

def test_create_user_email_matches(api_base_url, new_user):
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    data = response.json()
    assert data['email'] == new_user['email']

def test_create_user_role_matches(api_base_url, new_user):
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    data = response.json()
    assert data['role'] == new_user['role']

def test_create_user_with_empty_name(api_base_url):
    new_user = {
        'name': "",
        'email': "kratik@example.com"
    }
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    data = response.json()
    assert response.status_code == 201
    assert data['name'] == ""
    
def test_get_user_test_fixture(get_user_1):
    assert get_user_1['data']['name'] == 'Kratik Sharma'

