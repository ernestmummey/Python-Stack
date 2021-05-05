from flask import Flask, render_template
playground = Flask(__name__)

@playground.route('/play')
def boxes():
    return render_template('index.html', num = 3, color = 'aqua')

@playground.route('/play/<num>')
def multiples(num):
    return render_template('index.html', num = int(num), color = 'aqua')

@playground.route('/play/<num>/<color>')
def color(num, color):
    return render_template('index.html', num = int(num), color = color)


if __name__=="__main__":       
    playground.run(debug=True)