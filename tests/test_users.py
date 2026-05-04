import pytest
import requests

@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2,200),
    (3, 200),
    (999, 404),
    (0, 404),
    (-1, 404)
])

def test_get_user_by_id(user_id, expected_status, api_base_url):
    """Verify that valid user IDs return 200 and invalid IDs return 404."""
    response = requests.get(f'{api_base_url}/api/users/{user_id}')
    assert response.status_code == expected_status

@pytest.mark.parametrize('user_id, expected_name', [
    (1, 'Kratik Sharma'),
    (2, 'Rahul Verma'),
    (3, 'Priya Singh')
])

def test_user_name_by_id(user_id, expected_name, api_base_url):
    response = requests.get(f'{api_base_url}/api/users/{user_id}')
    data = response.json()
    assert data['data']['name'] == expected_name

@pytest.mark.parametrize('name, email, role', [
    ('Amit Shah', 'amit@test.com', 'user'),
    ('Sneha Patel', 'sneha@test.com', 'admin'),
    ('Ravi Kumar', 'ravi@test.com', 'user'),
])

def test_create_user(name, email, role, api_base_url):
    new_user = {
        'name': name,
        'email': email,
        'role': role
    }
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    data = response.json()
    assert response.status_code == 201
    assert data['data']['name'] == name
    assert data['data']['email'] == email
    assert data['data']['role'] == role

@pytest.mark.parametrize('invalid_email', [
    'notanemail',
    'missing@',
    '@nodomain',
    '',
    'spaces in@email.com',
])

def test_create_user_invalid_email(invalid_email, api_base_url):
    new_user = {
        'name': 'Test User',
        'email': invalid_email,
        'role': 'user'
    }
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    assert response.status_code == 201

def test_get_all_users(api_base_url):
    response = requests.get(f'{api_base_url}/api/users')
    data = response.json()
    for user in data['data']:
        assert 'name' in user
        assert len(user['name']) >= 0

def test_post_user_with_id(api_base_url):
    new_user = {
        'name': 'Test User',
        'email': 'test@example.com',
        'role': 'user',
    }
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    data = response.json()
    assert data['data']['id'] > 0

@pytest.mark.parametrize('user_id, expected_name', [
    (1, 'Kratik Sharma'),
    (2, 'Rahul Verma'),
    (3, 'Priya Singh')
])
def test_user_by_id(user_id, expected_name, api_base_url):
    response = requests.get(f'{api_base_url}/api/users/{user_id}')
    data = response.json()
    assert data['data']['name'] == expected_name