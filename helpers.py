from flask import redirect, flash, render_template, request, session
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def sorry(message):
    flash(message)
    return render_template("sorry.html")


def updateMessage(message):
    flash(message)
    return render_template("message.html")