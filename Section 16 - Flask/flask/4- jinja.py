# Building url dynamically 
# Variable rule 
#  Jinja 2 Templete engine
    # {{ }} Expression to print outpur in html
    #  {%...%} conditions, for loops
    #  {#...#} comments


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

@app.route('/submit', methods =['GET', 'POST'])
def submit():
    if request.method =='POST':
        name  = request.form['name']
        return f'Hello {name}!!!!!!'
    return render_template('form.html')

# Variable Rule
@app.route('/sucess/<int:score>') #int value
def sucess(score):
    # return "The marks you got is " + str(score) #that why we typecast
    res = ""
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'
    return render_template('result.html',results=res)

# Variable Rule
@app.route('/sucessresult/<int:score>') #int value
def sucessresult(score):
    # return "The marks you got is " + str(score) #that why we typecast
    res = ""
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'

    exp = {'Score': score,"Result":res}
    return render_template('result1.html',results=exp)



if __name__ == "__main__":
    app.run(debug=True)
