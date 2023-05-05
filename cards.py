from sqlalchemy import text
from db import db

def get_cards(collection_id):
    sql = text("""SELECT name, wins, losses, win_rate, id FROM cards
                WHERE collection_id=:collection_id ORDER BY id DESC""")
    return db.session.execute(sql, {"collection_id": collection_id}).fetchall()

def add_card(name, collection_id):
    sql = text("""INSERT INTO cards (name, collection_id, wins, losses, win_rate)
                VALUES (:name,:collection_id, 0, 0, 0)""")
    db.session.execute(sql, {"name": name, "collection_id":collection_id,})
    db.session.commit()
    return True

def delete_card(card_id):
    sql = text("DELETE FROM cards WHERE id=:card_id")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

# following queries set the card's win-rate to its wins/total games multiplied by 100.
# the hundred is a float in order to avoid integer division.
# if total games is zero, the card's win-rate is set to 0.

def increase_wins(card_id):
    sql = text("""UPDATE cards SET wins=CASE WHEN (wins+1) > 1000000000 THEN 1000000000
                ELSE wins+1 END, win_rate=
                CASE WHEN (wins+losses+1)=0 THEN 0
                ELSE (wins+1)*100.0/(wins+losses+1) END WHERE id=:card_id""")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

def remove_wins(card_id):
    sql = text("""UPDATE cards SET wins=CASE WHEN (wins-1) < 0 THEN 0
                ELSE wins-1 END, win_rate=CASE WHEN (wins-1) <= 0 THEN 0
                ELSE (wins-1)*100.0/(wins+losses-1) END WHERE id=:card_id""")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

def increase_losses(card_id):
    sql = text("""UPDATE cards SET losses=CASE WHEN (losses+1) > 1000000000 THEN 1000000000
                ELSE losses+1 END, win_rate=
                CASE WHEN (wins+losses+1)=0 THEN 0
                ELSE (wins)*100.0/(wins+losses+1) END WHERE id=:card_id""")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True

def remove_losses(card_id):
    sql = text("""UPDATE cards SET losses=CASE WHEN (losses-1) < 0 THEN 0
                ELSE losses-1 END, win_rate=
                CASE WHEN (losses-1) <= 0 AND wins <= 0 THEN 0
                WHEN (losses-1) <= 0 THEN 100
                ELSE (wins)*100.0/(wins+losses-1) END WHERE id=:card_id""")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()
    return True
