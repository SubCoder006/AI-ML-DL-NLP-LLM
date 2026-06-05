 

from flask import Flask,render_template,request
import jinja2

'''
It creates an instance of the Flask class,
which will be your WSGI application.
'''
## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route("/about")
def about():
    return render_template('about.html')

## variable rule
@app.route("/success/<int:score>")
def success(score):
    # return "The marks you got is "+ str(score)
    res=""
    if score > 60:
        res = "PASS"
    else :
        res = "FAIL"
    
    return render_template('result.html',results=res)


@app.route("/Successes/<int:score>")
def Succeses(score):
    if score > 60:
        res = {"Result": "PASS", "Score": score}
    else:
        res = {"Result": "FAIL", "Score": score}
    
    return render_template('result1.html', results=res)


@app.route("/Successif/<int:score>")
def Succesif(score):
    pass
    return render_template('result2.html',results=score)

if __name__=="__main__":
    app.run(debug=True)
    

