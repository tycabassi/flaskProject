from flask import Flask

app = Flask(__name__)


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=0.0):
    fahrenheit = (celsius * 9 / 5) + 32
    return f" {celsius} celsius = {fahrenheit} fahrenheit"


if __name__ == '__main__':
    app.run()

# @app.route('/')
# def hello_world():  # put application's code here
#     return '<h1>Hello World!:)</h1>'
#
#
# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name=""):
#     return f'Hello{name}'
#
#
# if __name__ == '__main__':
#     app.run()
