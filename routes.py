from flask import render_template, request, redirect
from app import app
import users
import cardcollections
import cards

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
            return render_template("error.html",
                message="passwords don't match")
        if users.register(username, password1):
            return redirect("/login")

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html",
                message="wrong username or password")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/collections", methods=["get", "post"])
def collections():
    user_id = users.user_id()
    if request.method == "GET":
        return render_template("cardcollections.html",
            collections=cardcollections.get_collections(user_id))
    if request.method == "POST":
        title = request.form["title"]
        cardcollections.create_collection(title)
        return redirect("/collections")

@app.route("/collections/<int:collection_id>")
def collectionlist(collection_id):
    user_id = users.user_id()
    owner_id = cardcollections.collection_owner(collection_id)
    cardcollections.set_collection_id(collection_id)
    cardlist = cards.get_cards(collection_id)
    if user_id == owner_id:
        return render_template("collectionlist.html",
            cardlist=cardlist)
    return render_template("error.html",
        message="error: not your collection")

@app.route("/addcard", methods=["get", "post"])
def addcard():
    collection_id = cardcollections.get_collection_id()
    if request.method == "GET":
        return redirect(f"/collections/{collection_id}")
    if request.method == "POST":
        cardname = request.form["cardname"]
        cards.add_card(cardname, collection_id)
        return redirect(f"/collections/{collection_id}")
