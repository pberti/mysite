from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="Albert73",
    password="812288qwe",
    hostname="Albert73.mysql.pythonanywhere-services.com",
    databasename="Albert73$visitors",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Visit(db.Model):
    __tablename__ = "guests"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    host = db.Column(db.String(4096))
    company = db.Column(db.String(4096))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", guests=Visit.query.all())
    visit = Visit(name=request.form["contents"], host=request.form["host"],  company=request.form["company"])
    db.session.add(visit)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/list", methods=["GET", "POST"])
def wibble():
    return render_template("list.html", guests=Visit.query.all())




#SHOP

@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template("shop.html")


app.config["IMAGE_UPLOADS"] = "/home/Albert73/mysite/static/poze"

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            image.save(os.path.join(app.root_path, app.config["IMAGE_UPLOADS"], image.filename))

            return redirect(request.url)
    return render_template("upload_image.html")


#LOGIN

from flask import session, g

app.secret_key = os.urandom(24)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method ==  'POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('login'))


@app.before_request()
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
'''
@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('login.html')
'''
