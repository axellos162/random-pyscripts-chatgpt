from flask import Flask, jsonify, request
from flaskext.mysql import MySQL

app = Flask(__name__)

# Database configuration
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'database'
app.config['MYSQL_DATABASE_HOST'] = 'host'
mysql = MySQL(app)

# HTTP GET endpoint at /user to retrieve a single user record
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = mysql.get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    data = cursor.fetchone()
    if data:
        user = {
            'id': data[0],
            'username': data[1],
            'password': data[2],
            'status': data[3]
        }
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# HTTP GET endpoints at /users to retrieve all user records
@app.route('/users', methods=['GET'])
def get_users():
    conn = mysql.get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    users = []
    for row in data:
        user = {
            'id': row[0],
            'username': row[1],
            'password': row[2],
            'status': row[3]
        }
        users.append(user)
    return jsonify(users)

# HTTP POST endpoint at /newuser to create a new user record
@app.route('/newuser', methods=['POST'])
def create_user():
    conn = mysql.get_db()
    cursor = conn.cursor()
    username = request.json['username']
    password = request.json['password']
    status = request.json['status']
    cursor.execute("INSERT INTO users (username, password, status) VALUES (%s, %s, %s)", (username, password, status))
    conn.commit()
    user_id = cursor.lastrowid
    user = {
        'id': user_id,
        'username': username,
        'password': password,
        'status': status
    }
    return jsonify(user)

# HTTP DELETE endpoint at /deleteuser to delete an existing user record
@app.route('/deleteuser', methods=['DELETE'])
def delete_user():
    conn = mysql.get_db()
    cursor = conn.cursor()
    user_id = request.json['id']
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
