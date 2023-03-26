from flask import render_template, request, redirect
from app import app
import users
import cardcollections

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return "error: passwords don't match"
        if users.register(username, password1):
            return redirect("/")

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return "error: wrong username or password"
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/collections", methods=["get", "post"])
def collections():
    user_id = users.user_id()
    if request.method == "GET":
        return render_template("cardcollections.html", collections=cardcollections.get_collections(user_id))
    if request.method == "POST":
        title = request.form["title"]
        cardcollections.create_collection(title)
        return redirect("/collections")
