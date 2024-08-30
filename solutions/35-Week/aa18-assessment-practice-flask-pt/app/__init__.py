from flask import Flask, render_template, redirect
from flask_migrate import Migrate

from .config import Configuration
from .forms import SimpleForm
from .models import db, SimplePerson

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)

@app.route("/")
def home():
  return render_template("main_page.html")

@app.route("/simple-form")
def simple_form():
  form = SimpleForm()

  return render_template("simple_form.html", form=form)

@app.route("/simple-form", methods=["POST"])
def simple_data():
  form = SimpleForm()

  if form.validate_on_submit():
    data = SimplePerson()
    form.populate_obj(data)

    db.session.add(data)
    db.session.commit()

    return redirect("/")
  
  return "Bad Data"

@app.route("/simple-form-data")
def data():
  result = SimplePerson.query.filter(SimplePerson.name.like("M%")).all()

  return render_template("simple_form_data.html", result=result)