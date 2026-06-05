try:
    from flask import Flask
except Exception as e:
    raise RuntimeError(
        "Flask is not installed or cannot be imported. Install it with: pip install flask\nOriginal error: {}".format(e)
    )

'''
It creates an instance of the Flask class,
which will be your WSGI application.
'''
## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course.\n This should be an amazing coarse."

@app.route("/index")
def index():
    return "Welcome to Index Page. \n\n Home   About   Contact"
    

if __name__=="__main__":
    app.run(debug=True)
