from sqlalchemy import text
from flask import session
from db import db

def get_collections_by_user(user_id):
    sql = text("SELECT name, id FROM collections WHERE owner_id=:owner_id")
    return db.session.execute(sql, {"owner_id": user_id}).fetchall()

def get_collections_that_invited_guest(guest_id):
    sql = text("""SELECT name, collections.id FROM collections INNER JOIN collection_invitations
                ON collections.id=collection_invitations.collection_id
                WHERE collection_invitations.guest_id=:guest_id""")
    return db.session.execute(sql, {"guest_id": guest_id}).fetchall()

# Find a collection and its owner's username from table "collections" and "users"
def get_collection_by_id(collection_id):
    sql = text("""SELECT collections.name, collections.id, owner_id, users.username
                FROM collections INNER JOIN users ON collections.owner_id=users.id
                WHERE collections.id=:collection_id""")
    return db.session.execute(sql, {"collection_id": collection_id}).fetchone()

def create_collection(name):
    logged_user_id = session.get("user_id", 0)
    sql = text("INSERT INTO collections (name, owner_id) VALUES (:name,:owner_id)")
    db.session.execute(sql, {"name": name, "owner_id":logged_user_id})
    db.session.commit()
    return True

def delete_collection(collection_id):
    sql = text("DELETE FROM collections WHERE id=:collection_id")
    db.session.execute(sql, {"collection_id": collection_id})
    db.session.commit()
    return True

def collection_owner(collection_id):
    sql = text("SELECT owner_id FROM collections WHERE id=:id")
    result = db.session.execute(sql, {"id": collection_id})
    owner = result.fetchone()[0]
    return owner

def set_collection_id(collection_id):
    session["collection_id"] = collection_id
    return True

def get_collection_id():
    return session.get("collection_id", 0)
