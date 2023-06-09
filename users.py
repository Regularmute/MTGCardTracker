import secrets
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from flask import abort, request, session
from db import db

def login(username, password):
    sql = text("SELECT password, id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if check_password_hash(user[0], password):
        session["user_id"] = user[1]
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
        return True
    return False

def find_one_by_username(username):
    sql = text("SELECT id FROM users WHERE username=:username")
    user = db.session.execute(sql, {"username": username}).fetchone()
    if not user:
        return False
    return user[0]

def find_invited_users_by_collection_id(collection_id):
    sql = text("""SELECT users.username, users.id FROM users
                INNER JOIN collection_invitations
                ON users.id=collection_invitations.guest_id
                WHERE collection_invitations.collection_id=:collection_id""")
    return db.session.execute(sql, {"collection_id": collection_id}).fetchall()

def logout():
    del session["user_id"]
    del session["username"]
    del session["csrf_token"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except IntegrityError:
        print("Username is already in use")
        return False
    return True

def user_id():
    return session.get("user_id", 0)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
