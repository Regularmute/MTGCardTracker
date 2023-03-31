from sqlalchemy import text
from db import db

def get_cards(collection_id):
    sql = text("""SELECT name, wins, losses, id FROM cards
                WHERE collection_id=:collection_id ORDER BY id DESC""")
    return db.session.execute(sql, {"collection_id": collection_id}).fetchall()

def add_card(name, collection_id):
    sql = text("""INSERT INTO cards (name, collection_id, wins, losses)
                VALUES (:name,:collection_id, 0, 0)""")
    db.session.execute(sql, {"name": name, "collection_id":collection_id,})
    db.session.commit()
    return True

def delete_card(card_id):
    sql = text("DELETE FROM cards WHERE id=:card_id")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

def increase_wins(card_id):
    sql = text("UPDATE cards SET wins=wins+1 WHERE id=:card_id")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

def remove_wins(card_id):
    sql = text("UPDATE cards SET wins=wins-1 WHERE id=:card_id")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

def increase_losses(card_id):
    sql = text("UPDATE cards SET losses=losses+1 WHERE id=:card_id")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

def remove_losses(card_id):
    sql = text("UPDATE cards SET losses=losses-1 WHERE id=:card_id")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True
