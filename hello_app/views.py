import re
from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
def hello():
    return "Hello Flask"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+", name)
    print(match_object)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/hi/")
@app.route("/hi/<name>")
def hi(name = None):
    return render_template("hi_there.html", name=name, date=datetime.now())

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
