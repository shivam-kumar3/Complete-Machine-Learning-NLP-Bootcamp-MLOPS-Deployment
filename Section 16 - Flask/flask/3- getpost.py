from flask import Flask, render_template, request
'''
    It creates an instance of the flask class,
    which will be your WSGI(web server gateway interface) application

'''
app = Flask(__name__)


@app.route('/')
def welcome():
    return '<html><H1>Hello , Welcome to Shivam Kumar Portfolio.</H1></HTML>'

@app.route('/index',methods =['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods =['GET', 'POST'])
def form():
    if request.method =='POST':
        name  = request.form['name']
        return f'Hello {name}!!!!!!'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
