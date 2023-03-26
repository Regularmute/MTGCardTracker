from sqlalchemy import text
from flask import session
from db import db

def get_collections(user_id):
    sql = text("SELECT name FROM collections WHERE owner_id=:owner_id")
    return db.session.execute(sql, {"owner_id": user_id}).fetchall()

def create_collection(name):
    logged_user_id = session.get("user_id", 0)
    sql = text("INSERT INTO collections (name, owner_id) VALUES (:name,:owner_id)")
    db.session.execute(sql, {"name": name, "owner_id":logged_user_id})
    db.session.commit()
    return True
