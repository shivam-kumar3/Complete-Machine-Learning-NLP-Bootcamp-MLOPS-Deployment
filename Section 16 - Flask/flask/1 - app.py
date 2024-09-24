from flask import Flask
'''
    It creates an instance of the flask class,
    which will be your WSGI(web server gateway interface) application

'''
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Hello , Welcome to Shivam Kumar Portfolio.'

@app.route('/index')
def index():
    return 'Welcome to the index page'



if __name__ == "__main__":
    app.run(debug=True)
