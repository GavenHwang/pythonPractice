import random
import string
import requests

import sqlite3


def generate_six_char_string():
    all_characters = string.ascii_letters + string.digits
    result = ''.join(random.choice(all_characters) for i in range(6))
    return result


class TestFlaskApp:
    base_url = 'http://127.0.0.1:5000'
    username = generate_six_char_string()
    password = generate_six_char_string()
    password_new = generate_six_char_string()

    def test_01_register(self):
        url = f'{self.base_url}/register'
        data = {
            'username': self.username,
            'password': self.password
        }
        response = requests.post(url, json=data)
        assert response.status_code == 201
        assert 'New user created!' in response.text

    def test_02_register_duplicate(self):
        url = f'{self.base_url}/register'
        data = {
            'username': self.username,
            'password': self.password
        }
        response = requests.post(url, json=data)
        assert response.status_code == 409
        assert 'Username already exists!' in response.text

    def test_03_login(self):
        url = f'{self.base_url}/login'
        auth = (self.username, self.password)
        response = requests.get(url, auth=auth)
        assert response.status_code == 200
        assert 'token' in response.json()

    def test_04_protected(self):
        login_url = f'{self.base_url}/login'
        auth = (self.username, self.password)
        login_response = requests.get(login_url, auth=auth)
        token = login_response.json()['token']

        protected_url = f'{self.base_url}/protected'
        headers = {'x-access-token': token}
        response = requests.get(protected_url, headers=headers)
        assert response.status_code == 200
        assert 'This is a protected route' in response.text

    def test_05_get_user(self):
        login_url = f'{self.base_url}/login'
        auth = (self.username, self.password)
        login_response = requests.get(login_url, auth=auth)
        token = login_response.json()['token']

        conn = sqlite3.connect('./instance/users.db')
        c = conn.cursor()
        c.execute(f"SELECT id FROM users WHERE username = '{self.username}'")
        user_id = c.fetchone()[0]
        conn.close()

        get_user_url = f'{self.base_url}/user/{user_id}'
        headers = {'x-access-token': token}
        response = requests.get(get_user_url, headers=headers)
        assert response.status_code == 200
        assert 'user' in response.json()

    def test_06_update_user(self):
        login_url = f'{self.base_url}/login'
        auth = (self.username, self.password)
        login_response = requests.get(login_url, auth=auth)
        token = login_response.json()['token']

        conn = sqlite3.connect('./instance/users.db')
        c = conn.cursor()
        c.execute(f"SELECT id FROM users WHERE username = '{self.username}'")
        user_id = c.fetchone()[0]
        conn.close()

        update_url = f'{self.base_url}/user/{user_id}'
        headers = {'x-access-token': token}
        new_data = {
            'password': self.password_new
        }
        response = requests.put(update_url, headers=headers, json=new_data)
        assert response.status_code == 200
        assert 'User updated successfully' in response.text

    def test_07_delete_user(self):
        login_url = f'{self.base_url}/login'
        auth = (self.username, self.password_new)
        login_response = requests.get(login_url, auth=auth)
        token = login_response.json()['token']

        conn = sqlite3.connect('./instance/users.db')
        c = conn.cursor()
        c.execute(f"SELECT id FROM users WHERE username = '{self.username}'")
        user_id = c.fetchone()[0]
        conn.close()

        delete_url = f'{self.base_url}/user/{user_id}'
        headers = {'x-access-token': token}
        response = requests.delete(delete_url, headers=headers)
        assert response.status_code == 200
        assert 'User deleted successfully' in response.text
