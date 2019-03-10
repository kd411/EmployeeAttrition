from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
import sqlite3
from flask_session import Session
from tempfile import mkdtemp
from helpers import login_required, sorry, updateMessage
from machine import run

app = Flask(__name__)


app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-re-validate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
@login_required
def index():
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    db = SQL("sqlite:///hr.db")
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return sorry("must provide username")
        elif not request.form.get("password"):
            return sorry("must provide password")
        rows = db.execute("SELECT * FROM login WHERE username = :username", username=request.form.get("username"))
        if len(rows) != 1 or rows[0]["password"] != request.form.get("password"):
            return sorry("invalid username and/or password")
        session["user_id"] = rows[0]["id"]
        return redirect("/home")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/home")
@login_required
def home():
    return render_template("home.html")


@app.route("/view")
@login_required
def view():
    conn = sqlite3.connect("dataset.db")
    cur = conn.execute("SELECT * FROM dataset")
    data = cur.fetchall()
    return render_template("view.html", data=data)


@app.route("/update")
@login_required
def update():
    return render_template("update.html")


@app.route("/updateDet")
@login_required
def updateDet():
    if not request.values.get("id"):
        return updateMessage("must enter ID")
    id = request.values.get("id")
    param = request.values.get("parameter")
    paramval = request.values.get("paramvalue")
    job = request.values.get("JobRole")
    marstat = request.values.get("MaritalStatus")
    if int(id) < 0 or int(id) > 29:
        return updateMessage("ID not found")
    db = SQL("sqlite:///dataset.db")
    if param == "":
        if job == "":
            db.execute("UPDATE dataset SET MaritalStatus=:ms WHERE ID=:i", ms=marstat, i=int(id))
        elif marstat == "":
            db.execute("UPDATE dataset SET JobRole=:j WHERE ID=:i", j=job, i=int(id))
        else:
            db.execute("UPDATE dataset SET  JobRole=:j, MaritalStatus=:ms WHERE ID=:i", j=job, ms=marstat, i=int(id))
    else:
        if job == "" and marstat == "":
            db.execute("UPDATE dataset SET " + param + "=:val WHERE ID=:i", val=int(paramval), i=int(id))
        elif job == "":
            db.execute("UPDATE dataset SET " + param + "=:val, MaritalStatus=:ms WHERE ID=:i", val=int(paramval), ms=marstat, i=int(id))
        elif marstat == "":
            db.execute("UPDATE dataset SET " + param + "=:val, JobRole=:j WHERE ID=:i", val=int(paramval), j=job, i=id)
        else:
            db.execute("UPDATE dataset SET " + param + "=:val, JobRole=:j, MaritalStatus=:ms WHERE ID=:i", val=int(paramval), j=job, ms=marstat, i=int(id))
    return updateMessage("Updated successfully")


@app.route("/attrition")
@login_required
def attrition():
    conn = sqlite3.connect("dataset.db")
    cur = conn.execute("SELECT * FROM dataset")
    data = cur.fetchall()
    att = run(data)
    newd = []
    i=0
    for row in att:
        t = ()
        t = t + (i,)
        t = t + (row,)
        i = i+1
        newd.append(t)
    return render_template("attrition.html", data=newd)


@app.route("/graph")
@login_required
def graph():
    return render_template("graph.html")
