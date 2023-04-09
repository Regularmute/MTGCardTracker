import re
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
        if users.find_one_by_username(username):
            return render_template("error.html",
                message="username is taken")
        if not re.match(r"^[A-Za-z0-9]+$", username):
            return render_template("error.html",
                message="username must only have English letters or numbers")
        if len(username) < 1:
            return render_template("error.html",
                message="username must not be empty")
        if len(username) > 60:
            return render_template("error.html",
                message="username is too long: max 60 characters")
        if len(password1) < 6:
            return render_template("error.html",
                message="password must have at least 6 characters")
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
            collections=cardcollections.get_collections_by_user(user_id))
    if request.method == "POST":
        title = request.form["title"].strip()
        if len(title) < 1:
            return render_template("error.html",
                message="collection name missing")
        if len(title) > 60:
            return render_template("error.html",
                message="collection title too long: max 60 characters")
        cardcollections.create_collection(title)
        return redirect("/collections")

@app.route("/deletecollection", methods=["post"])
def deletecollection():
    collection_id = request.form["collection_id"]
    cardcollections.delete_collection(collection_id)
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
        message="not your collection")

@app.route("/addcard", methods=["post"])
def addcard():
    collection_id = cardcollections.get_collection_id()
    cardname = request.form["cardname"]
    if len(cardname) < 1:
        return render_template("error.html",
            message="card name missing")
    if len(cardname) > 150:
        return render_template("error.html",
                message="card name too long: max 150 characters")
    cards.add_card(cardname, collection_id)
    return redirect(f"/collections/{collection_id}")

@app.route("/deletecard", methods=["post"])
def deletecard():
    collection_id = cardcollections.get_collection_id()
    card_id = request.form["card_id"]
    cards.delete_card(card_id)
    return redirect(f"/collections/{collection_id}")

@app.route("/updatewins", methods=["post"])
def updatewins():
    collection_id = cardcollections.get_collection_id()
    card_id = request.form["card_id"]
    direction = request.form["direction"]
    if direction == "add":
        cards.increase_wins(card_id)
    if direction == "remove":
        cards.remove_wins(card_id)
    return redirect(f"/collections/{collection_id}")

@app.route("/updatelosses", methods=["post"])
def updatelosses():
    collection_id = cardcollections.get_collection_id()
    card_id = request.form["card_id"]
    direction = request.form["direction"]
    if direction == "add":
        cards.increase_losses(card_id)
    if direction == "remove":
        cards.remove_losses(card_id)
    return redirect(f"/collections/{collection_id}")
