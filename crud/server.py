from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    # call the function, passing in the name of our db
    mysql = connectToMySQL('users_schema')
    # call the query_db function, pass in the query as a string
    user  = mysql.query_db('SELECT * FROM users;')
    return render_template("read(all).html", users = user)


@app.route("/created")
def add_users():
    return render_template('create.html')


@app.route('/new_user', methods = ['POST'])
def add_friend():
    query = "INSERT INTO users_schema.users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_names)s, %(last_names)s, %(Email)s, NOW(), NOW());"
    data = {
        "first_names": request.form["fname"],
        "last_names": request.form["lname"],
        "Email": request.form['email'],
    }
    user_id = connectToMySQL('users_schema')
    user_id.query_db(query, data)
    return redirect("/")


@app.route("/read/<int:id>")
def only_one_id(id):
    query = 'SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE  id = %(id)s'
    data = {
        'id': id
    }
    db = connectToMySQL('users_schema')
    bd = db.query_db(query, data) 
    return render_template("read(one).html", one_user = bd)


@app.route('/edit_form/<int:id>')
def editing_form(id):
    query = 'SELECT id FROM users WHERE  id = %(id)s'
    data = {
        'id': id
    }
    one_person = connectToMySQL('users_schema')
    base = one_person.query_db(query, data) 
    return render_template('edit.html', that_one_id = base)


@app.route("/edit/<int:id>", methods = ['POST'])
def edit_form(id):
    query = "UPDATE users_schema.users SET first_name = %(first_names)s, last_name = %(last_names)s, email = %(Email)s WHERE id = %(id)s"
    data = {
        "id": id,
        "first_names": request.form["fname"],
        "last_names": request.form["lname"],
        "Email": request.form['email'],
    }
    edit_person = connectToMySQL('users_schema')
    edit_person.query_db(query, data)
    return redirect(f"/read/{id}")


@app.route("/delete/<int:id>")
def bye_bye(id):
    query = 'DELETE FROM users WHERE  id = %(id)s'
    data = {
        'id': id
    }
    one_person = connectToMySQL('users_schema')
    base = one_person.query_db(query, data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)