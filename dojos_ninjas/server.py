from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/dojos")
def index():
    # call the function, passing in the name of our db
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    # call the query_db function, pass in the query as a string
    city = mysql.query_db('SELECT * FROM dojos;')
    return render_template("dojos.html", cities = city)



@app.route("/createlocation", methods=["POST"])
def home_page():
    query = "INSERT INTO dojos_and_ninjas_schema.dojos (cities,created_at, updated_at) VALUES (%(city)s, Now(), Now());"
    data = {
            "city": request.form["loca"],
    }
    db = connectToMySQL('dojos_and_ninjas_schema')
    db.query_db(query, data)
    return redirect ("/dojos")

@app.route("/ninjas")
def ninjas_html():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojo = mysql.query_db('SELECT * FROM dojos;')
    return render_template("new_ninja.html", loco_dojo = dojo)


@app.route("/ninjas_form", methods=["POST"])
def adding_ninjas():
    query = "INSERT INTO dojos_and_ninjas_schema.ninjas (dojo_id, first_name, last_name, age,created_at, updated_at) VALUES (%(id)s,%(fname)s, %(lname)s, %(ninja_age)s, Now(), Now());"
    data = {
            "id":request.form['dojo_cities'],
            "fname": request.form["first_name"],
            "lname": request.form["last_name"],
            "ninja_age": request.form["age"],
    }
    id = request.form['dojo_cities']
    person = connectToMySQL('dojos_and_ninjas_schema')
    person.query_db(query, data)
    return redirect (f"/dojo_ninja/{id}") 


@app.route("/dojo_ninja/<int:id>")
def dojo_ninjas(id):
    query = ("SELECT dojos.cities, ninjas.first_name, ninjas.last_name, ninjas.age FROM dojos_and_ninjas_schema.dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;")
    data = {
        'id':id
    }
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    d_n = mysql.query_db(query, data)
    return render_template("/dojo_show.html", dojo_ninjas = d_n, )



if __name__ == "__main__":
    app.run(debug=True)