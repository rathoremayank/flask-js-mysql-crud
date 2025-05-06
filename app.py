from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Hesoyam@56'
app.config['MYSQL_DB'] = 'flask_crud'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User added"}), 201

@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (data['name'], data['email'], id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User updated"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
