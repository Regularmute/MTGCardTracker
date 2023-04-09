from sqlalchemy import text
from flask import session
from db import db

def invite_user_to_collection(collection_id, guest_id):
    sql = text("""INSERT INTO collection_invitations (collection_id, guest_id)
                VALUES (:collection_id, :guest_id)""")
    db.session.execute(sql, {"collection_id": collection_id, "guest_id": guest_id})
    db.session.commit()
    return True
