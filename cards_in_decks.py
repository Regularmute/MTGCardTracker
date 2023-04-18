from sqlalchemy import text
from db import db

def add_card_to_deck(card_id, deck_id):
    sql = text("""INSERT INTO cards_in_decks (card_id, deck_id)
                VALUES (:card_id, :deck_id)""")
    db.session.execute(sql, {"card_id": card_id, "deck_id": deck_id})
    db.session.commit()
    return True

def find_one_by_deck_and_card(deck_id, card_id):
    sql = text("""SELECT id FROM cards_in_decks WHERE deck_id=:deck_id
                AND card_id=:card_id""")
    card_in_deck = db.session.execute(sql,
                {"deck_id": deck_id,"card_id": card_id}).fetchone()

    if not card_in_deck:
        return False

    return card_in_deck

def get_cards_by_deck_id(deck_id):
    sql = text("""SELECT cards.id, cards_in_decks.id, name, wins, losses FROM cards_in_decks
                INNER JOIN cards ON cards_in_decks.card_id=cards.id
                WHERE cards_in_decks.deck_id=:deck_id ORDER BY cards_in_decks.id DESC""")

    decklist = db.session.execute(sql, {"deck_id": deck_id}).fetchall()

    return decklist

def remove_card_from_deck(card_id, deck_id):
    sql = text("""DELETE FROM cards_in_decks WHERE deck_id=:deck_id
                AND card_id=:card_id""")
    db.session.execute(sql, {"deck_id": deck_id, "card_id": card_id})
    db.session.commit()
    return True
