import re
from flask import render_template, request, redirect
from app import app
import users
import cardcollections
import collectioninvites
import cards
import decks
import cards_in_decks

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
        error_message = "something went wrong"
        if users.find_one_by_username(username):
            error_message="username is taken"
        if not re.match(r"^[A-Za-z0-9]+$", username):
            error_message="username must only have English letters or numbers"
        if len(username) < 1:
            error_message="username must not be empty"
        if len(username) > 60:
            error_message="username is too long: max 60 characters"
        if len(password1) < 6:
            error_message="password must have at least 6 characters"
        if password1 != password2:
            error_message="passwords don't match"
        elif users.register(username, password1):
            return redirect("/login")
        return render_template("error.html", message=error_message)

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
            collections=cardcollections.get_collections_by_user(user_id),
            authorized_collections=cardcollections.get_collections_that_invited_guest(user_id))
    if request.method == "POST":
        users.check_csrf()
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
    users.check_csrf()
    collection_id = request.form["collection_id"]
    cardcollections.delete_collection(collection_id)
    return redirect("/collections")

@app.route("/collections/<int:collection_id>")
def collectionlist(collection_id):
    user_id = users.user_id()
    owner_id = cardcollections.collection_owner(collection_id)
    cardcollections.set_collection_id(collection_id)
    cardlist = cards.get_cards(collection_id)
    collection = cardcollections.get_collection_by_id(collection_id)
    invited_users = users.find_invited_users_by_collection_id(collection_id)
    decks_in_collection = decks.get_decks_by_collection(collection_id)

    is_invited = collectioninvites.find_guest_in_collection_id(user_id, collection_id)
    if user_id == owner_id or is_invited:
        return render_template("collectionlist.html",
            cardlist=cardlist, collection=collection, invited_users=invited_users,
            decks=decks_in_collection, logged_userid=user_id)
    return render_template("error.html",
        message="not your collection")

@app.route("/inviteuser", methods=["post"])
def inviteuser():
    users.check_csrf()

    collection_id = cardcollections.get_collection_id()
    username = request.form["usernametoinvite"]

    if not username:
        return render_template("error.html",
            message="invitation must have a username")

    invited_user_id = users.find_one_by_username(username)

    if not invited_user_id:
        return render_template("error.html", message="user does not exist")

    invitation_exists = collectioninvites.find_one_by_guest_and_collection(
                        invited_user_id, collection_id)

    if invitation_exists:
        return render_template(
            "error.html", message="user is already invited to this collection")

    collectioninvites.invite_user_to_collection(collection_id, invited_user_id)
    return redirect(f"collections/{collection_id}")

@app.route("/uninviteuser", methods=["post"])
def uninviteuser():
    users.check_csrf()

    collection_id = request.form["collection_id"]
    uninvited_user_id = request.form["uninvited_user"]

    collectioninvites.remove_guest_from_collection(
        uninvited_user_id, collection_id)

    return redirect(f"/collections/{collection_id}")

@app.route("/addcard", methods=["post"])
def addcard():
    users.check_csrf()

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
    users.check_csrf()

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

@app.route("/createdeck", methods=["post"])
def createdeck():
    users.check_csrf()

    collection_id = cardcollections.get_collection_id()
    creator_id = users.user_id()
    deck_name = request.form["deckname"]

    if len(deck_name) < 1:
        return render_template("error.html",
            message="deck name missing")
    if len(deck_name) > 150:
        return render_template("error.html",
                message="deck name too long: max 150 characters")
    decks.create_deck(deck_name, collection_id, creator_id)
    return redirect(f"/collections/{collection_id}")

@app.route("/deletedeck", methods=["post"])
def deletedeck():
    users.check_csrf()

    collection_id = cardcollections.get_collection_id()
    deck_id = request.form["deck_id"]
    decks.delete_deck(deck_id)
    return redirect(f"/collections/{collection_id}")

@app.route("/decks/<int:deck_id>")
def decklist(deck_id):
    user_id = users.user_id()
    decklist = cards_in_decks.get_cards_by_deck_id(deck_id)
    deck = decks.get_one_by_id(deck_id)
    collection_id = cardcollections.get_collection_id()
    collection = cardcollections.get_collection_by_id(collection_id)
    collectionlist = cards.get_cards(collection_id)

    return render_template("decklist.html",
        decklist=decklist, collectionlist=collectionlist, deck=deck,
        logged_userid=user_id, collection=collection
    )

@app.route("/addcardtodeck", methods=["post"])
def addcardtodeck():
    users.check_csrf()

    card_id = request.form["card_to_add"]
    deck_id = request.form["deck_id"]

    if not card_id:
        return render_template("error.html",
            message="card doesn't exist")
    if not deck_id:
        return render_template("error.html",
            message="deck doesn't exist")

    cards_in_decks.add_card_to_deck(card_id, deck_id)
    return redirect(f"decks/{deck_id}")

@app.route("/removecardfromdeck", methods=["post"])
def removecardfromdeck():
    users.check_csrf()

    deck_id = request.form["deck_id"]
    cardslot_id = request.form["cardslot_id"]

    if not cardslot_id:
        return render_template("error.html",
            message="card doesn't exist in deck")

    cards_in_decks.remove_cardslot(cardslot_id)
    return redirect(f"decks/{deck_id}")
