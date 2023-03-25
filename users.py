from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash
from db import db

def register(name, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (name,password) VALUES (:name,:password)")
        db.session.execute(sql, {"name":name, "password":hash_value})
        db.session.commit()
    except:
        print("exception")
        return False

    return True
