from sqlalchemy import text
from flask import session
from db import db

def get_collections(user_id):
    sql = text("SELECT name, id FROM collections WHERE owner_id=:owner_id")
    return db.session.execute(sql, {"owner_id": user_id}).fetchall()

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
