from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"copy
@app.route('/')          # The "@" decorator associates this route with the function immediately following
# import statements, maybe some other routes
def hello_world():
        return render_template('index.html', phrase="hello", times=5)


@app.route('/success')
def success():
    return "success"
    
# app.run(debug=True) should be the very last statement! 


# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mo