from sqlalchemy import text
from flask import session
from db import db

def invite_user_to_collection(collection_id, guest_id):
    sql = text("""INSERT INTO collection_invitations (collection_id, guest_id)
                VALUES (:collection_id, :guest_id)""")
    db.session.execute(sql, {"collection_id": collection_id, "guest_id": guest_id})
    db.session.commit()
    return True

def find_guest_in_collection_id(guest_id, collection_id):
    sql = text("""SELECT guest_id, collection_id FROM collection_invitations
                WHERE guest_id=:guest_id AND collection_id=:collection_id""")
    return db.session.execute(
        sql, {"guest_id": guest_id, "collection_id": collection_id}).fetchall()

def find_collections_by_guest(guest_id):
    sql = text("""SELECT collection_id FROM collection_invitations
                WHERE guest_id=:guest_id""")
    return db.session.execute(sql, {"guest_id": guest_id})
