from flask import Flask, render_template
checkers = Flask(__name__)

@checkers.route('/')
def display_checker():
        return render_template('index.html', x = int(8), y = int(8))

@checkers.route('/4')
def eightbyfour():
    return render_template('index.html', x = int(8), y = int(4))

@checkers.route('/<x>/<y>')
def you_choose_dimensions(x,y):
    return render_template('index.html', x = int(x), y = int(y))

# @checkers.route('/<x>/<y>/color1/color2')
# def pick_dimensions_and_colors(x,y,color1,color2):
#     return render_template('index.html', x = int(x), y = int(y),color1 = color1, color2 = color2)

if __name__=="__main__":       
    checkers.run(debug=True)