import secrets
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/index")
def index():
    flash("give me a user")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("hello " + str(request.form['user_input']) + "!")
    return render_template("index.html")
    
