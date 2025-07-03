import sqlite3
import hashlib
import jwt
import datetime
from flask import Flask, request, jsonify, make_response
from functools import wraps


class FlaskAppWithDB:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'your_secret_key'
        self.init_routes()

    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']

            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            try:
                data = jwt.decode(token, self.app.config['SECRET_KEY'], algorithms=['HS256'])
                current_user = data['id']
            except:
                return jsonify({'message': 'Token is invalid!'}), 401

            return f(current_user, *args, **kwargs)

        return decorated

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect('./instance/users.db')
        except sqlite3.Error as e:
            print(e)
        return conn

    def create_table(self, conn):
        try:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         username TEXT NOT NULL UNIQUE,
                         password TEXT NOT NULL)''')
        except sqlite3.Error as e:
            print(e)

    def register(self):
        data = request.get_json()
        hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()

        conn = self.create_connection()
        self.create_table(conn)

        try:
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?,?)",
                      (data['username'], hashed_password))
            conn.commit()
            return jsonify({'message': 'New user created!'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'message': 'Username already exists!'}), 409
        finally:
            conn.close()

    def login(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW - Authenticate': 'Basic realm="Login required!"'})

        hashed_password = hashlib.sha256(auth.password.encode()).hexdigest()

        conn = self.create_connection()
        self.create_table(conn)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username =? AND password =?", (auth.username, hashed_password))
        user = c.fetchone()
        conn.close()

        if not user:
            return make_response('Could not verify', 401, {'WWW - Authenticate': 'Basic realm="Login required!"'})

        token = jwt.encode({'id': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           self.app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({'token': token})

    def protected(self, current_user):
        return jsonify({'message': 'This is a protected route', 'user': current_user})

    def get_user(self, current_user, user_id):
        conn = self.create_connection()
        self.create_table(conn)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id =?", (user_id,))
        user = c.fetchone()
        conn.close()
        if user:
            return jsonify({'user': user})
        else:
            return jsonify({'message': 'User not found'}), 404

    def update_user(self, current_user, user_id):
        data = request.get_json()
        new_password = hashlib.sha256(data['password'].encode()).hexdigest() if 'password' in data else None
        new_username = data['username'] if 'username' in data else None

        conn = self.create_connection()
        self.create_table(conn)
        c = conn.cursor()
        update_query = "UPDATE users SET "
        values = []
        if new_password:
            update_query += "password =? "
            values.append(new_password)
        if new_username:
            if new_password:
                update_query += ", "
            update_query += "username =? "
            values.append(new_username)
        values.append(user_id)
        update_query += "WHERE id =?"

        try:
            c.execute(update_query, tuple(values))
            conn.commit()
            return jsonify({'message': 'User updated successfully'})
        except sqlite3.IntegrityError:
            return jsonify({'message': 'Username already exists!'}), 409
        finally:
            conn.close()

    def delete_user(self, current_user, user_id):
        conn = self.create_connection()
        self.create_table(conn)
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id =?", (user_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User deleted successfully'})

    def init_routes(self):
        self.app.route('/register', methods=['POST'])(self.register)
        self.app.route('/login')(self.login)
        self.app.route('/protected', methods=['GET'])(self.token_required(self.protected))
        self.app.route('/user/<int:user_id>', methods=['GET'])(self.token_required(self.get_user))
        self.app.route('/user/<int:user_id>', methods=['PUT'])(self.token_required(self.update_user))
        self.app.route('/user/<int:user_id>', methods=['DELETE'])(self.token_required(self.delete_user))

    def run(self, **kwargs):
        self.app.run(**kwargs)


if __name__ == '__main__':
    app = FlaskAppWithDB()
    app.run(debug=True)
