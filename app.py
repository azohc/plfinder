import secrets
from flask import Flask, render_template, request, flash
import spoti
import asyncio

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/")
def index():
    flash("give me a spotify user URI pls")
    return render_template("index.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    user_uri = str(request.form['user_input'])
    if (user_uri != ""):
        userstr = asyncio.run(spoti.user(user_uri))
        flash(userstr)
    else:
        flash("give me a (non empty) spotify user URI pls")

    return render_template("index.html")
    
