from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "12345678",
    "database": "dev1",
}

# Create a connection to the database
db = mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    try:
        cursor = db.cursor()

        # Get data from the form
        name = request.form['name']
        email = request.form['email']

        # Insert data into the database
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(sql, values)

        # Commit the changes to the database
        db.commit()

        cursor.close()

        return "Data inserted successfully!"

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)