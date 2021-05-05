from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

import random
rand = random.randint(1,100)

app.secret_key = 't0day'


@app.route("/")
def random_num():
    session.clear()
    session['rand'] = rand
    print(rand)
    return render_template("index.html")

@app.route("/home", methods = ['POST'])
def user():
    session['guess'] = int(request.form['user_guess'])
    print(session['guess'])
    if session['guess'] == session['rand']:
        session['answer'] = 'Correct'
    elif session['guess'] < session['rand']:
        session['answer'] = 'Too low!'
    elif session['guess'] > session['rand']:
        session['answer'] = 'Too high!'
    return render_template('index.html', guess = session['guess'], random_num = session['rand'], result = session['answer'])


if __name__ == "__main__":
    app.run(debug = True)
