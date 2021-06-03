from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

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

@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template("shop.html")

'''
# UPLOAD

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'static/poze'


images = UploadSet('images', IMAGES)
configure_uploads(app, images)
'''
class MyForm(FlaskForm):
    image = FileField('image')
'''
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = MyForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: { filename }'
    return render_template('upload .html', form=form)
'''
