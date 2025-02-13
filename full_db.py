import sqlite3
import os
import random


def open_db():
    db = sqlite3.connect('database.db')
    c = db.cursor()
    return db, c

def close_db(db):
    db.commit()
    db.close()

def clear_db():
    tables = ['Genre', 'Music', 'Music_genre', 'Person', 'Playlist', 'Playlist_content', ]
    db, c = open_db()
    for table in tables:
        c.execute(f'DELETE FROM {table}').fetchall()
    close_db(db)