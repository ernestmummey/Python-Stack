from flask import Flask 
my_first_bulid = Flask(__name__)
@my_first_bulid.route('/')

def hello():
    return 'Hello World'

@my_first_bulid.route('/dojo')
def dojo():
    return 'Dojo'

@my_first_bulid.route('/say/<name>')
def greetings(name):
    name = name.capitalize()
    return (f"Hi {name}!")
# There is no need to ensure if it is a string if it is already being return a string

@my_first_bulid.route('/repeat/<number_of_times>/<string>')
def repeat(number_of_times, string):
    num = int(number_of_times)
    space = string + ' '
    return space * num

if __name__=='__main__':
    my_first_bulid.run(debug=True)