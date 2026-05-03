import pytest
import requests

Base_url = "http://127.0.0.1:8000"

@pytest.fixture
def api_base_url():
    return Base_url

@pytest.fixture
def new_user():
    return {
        'name': "Rakesh Sharma",
        'email': "rakesh@example.com",
        'role': "User"
    }

@pytest.fixture
def user_created(api_base_url, new_user):
    response = requests.post(f'{api_base_url}/api/users', json=new_user)
    return response

@pytest.fixture
def get_user_1(api_base_url):
    response = requests.get(f'{api_base_url}/api/users/1')
    return response.json()

