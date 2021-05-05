from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.utils import redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

app.secret_key = "secret key"

@app.route("/")
def index():
    return render_template('index.html',)

@app.route("/users", methods = ['POST'])
def create_user():
    is_valid = True
    if len(request.form['user_name']) < 1:
        is_valid = False
        flash("Please enter your name")
    if len(request.form['dojo_location']) < 1:
        is_valid = False
        flash("Please enter your dojo location")
    if len(request.form['comment']) < 5:
        is_valid = False
        flash("Plese fill out the comments section")

    if not is_valid:
        return redirect("/")
    
    if is_valid:
        flash("Friend successfully added!")

        name = request.form['user_name']
        location = request.form['dojo_location']
        language = request.form['favorite_language']
        referral = request.form['referral']
        comments = request.form['comment']
        
        return render_template('show.html', personal_name = name, school_location = location, coding_language = language, would_you_refer = referral, your_comment= comments)

if __name__=="__main__":
    app.run(debug=True)