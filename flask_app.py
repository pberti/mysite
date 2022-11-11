from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello baaa mumu, fara, x2</p>"
'''


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def intro():
    return render_template('index.html')

@app.route("/portfolio", methods=["GET", "POST"])
def portfolio():
    return render_template('portfolio.html')

@app.route("/courses", methods=["GET", "POST"])
def courses():
    return render_template('courses.html')

'''
