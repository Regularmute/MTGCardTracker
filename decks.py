from sqlalchemy import text
from db import db

def get_decks_by_collection(collection_id):
    sql = text("""SELECT decks.id, decks.name, decks.creator_id, users.username
                FROM decks INNER JOIN users ON decks.creator_id=users.id
                WHERE collection_id=:collection_id ORDER BY id DESC""")
    return db.session.execute(sql, {"collection_id": collection_id}).fetchall()

def create_deck(name, collection_id, creator_id):
    sql = text("""INSERT INTO decks (name, collection_id, creator_id)
                VALUES (:name,:collection_id,:creator_id)""")
    db.session.execute(sql,
        {"name": name, "collection_id":collection_id, "creator_id":creator_id})
    db.session.commit()
    return True

def delete_deck(deck_id):
    sql = text("DELETE FROM decks WHERE id=:deck_id")
    db.session.execute(sql, {"deck_id": deck_id})
    db.session.commit()
    return True
