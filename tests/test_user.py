def get_user():
    return {
        'name': "Kratik",
        'email': "kratik@gmail.com",
        'role': "admin"
    }

def test_user():
    user = get_user()
    assert 'name' in user

def test_email():
    user = get_user()
    assert 'email' in user

def test_role():
    user = get_user()
    assert user['role'] == 'admin'

def test_user_email():
    user = get_user()
    assert '@' in user['email'] 

def test_user_name():
    user = get_user()
    assert user['name'] == 'Kratik'


def test_user_has_no_password():
    user = get_user()
    assert 'password' not in user

def test_user_has_no_phone():
    user = get_user()
    assert 'phone' not in user

def validate_user(user):
    if "name" not in user:
        return "FAIL - Name is missing"
    if "email" not in user:
        return "FAIL - Email is missing"
    if "@" not in user['email']:
        return "FAIL - Invalid email format"
    if "role" not in user:
        return "FAIL - Role is missing"
    return "PASS"

def test_validate_user():
    user = {'name': 'Kratik', 'email': 'k@test.com', 'role': 'admin'}
    assert validate_user(user) == "PASS"

def test_missing_name():
    user = {'email': 'k@test.com', 'role': 'admin'}
    assert validate_user(user) == "FAIL - Name is missing"

def test_missing_email():
    user = {'name': 'Kratik', 'role': 'admin'}
    assert validate_user(user) == "FAIL - Email is missing"

def test_invalid_email():
    user = {'name': 'Kratik', 'email': 'invalid-email', 'role': 'admin'}
    assert validate_user(user) == "FAIL - Invalid email format"

def test_missing_role():
    user = {'name': 'Kratik', 'email': 'k@test.com'}
    assert validate_user(user) == "FAIL - Role is missing"