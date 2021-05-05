from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fname = request.form["first_name"]
    lname = request.form["last_name"]
    stud_id = request.form["student_id"]
    sberry = request.form["strawberry"]
    rberry = request.form["raspberry"]
    frapple = request.form["apple"]
    print(f"Charging {fname} {lname} for {int(sberry)+int(rberry)+ int(frapple)} fruits ")
    return render_template("checkout.html", firstname=fname, lastname=lname, studentid=stud_id, Strawberry = sberry, Raspberry = rberry, Apple = frapple)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    