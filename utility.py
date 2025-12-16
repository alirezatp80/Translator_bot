import re
import sqlite3


def detect_lang(text:str):
    fa_count = 0
    en_count = 0
    
    for i in text:
        if re.search(r'[\u0600-\u06FF]',i):
            fa_count+=1
        if re.search(r'[A-Za-z]' , i):
            en_count+=1
    if fa_count>en_count:
        return 'fa'
    elif en_count>fa_count:
        return 'en'
    else:
        return 'en-fa'
    
def create_db():
    with sqlite3.connect('users.db') as connection :
        cursor = connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS users(
                           id INTEGER PRIMARY KEY,
                           username TEXT , 
                           lang_def TEXT
                           
                       );
                       """)
        
def insert_user(ID , USERNAME , LANG_DEF):
    user = select_user(ID)
    if not user:
        with sqlite3.connect('users.db') as connection :
            cursor = connection.cursor()
            cursor.execute("""
                           INSERT INTO users ( id , username , lang_def) VALUES (? , ? , ?);
                           """,(ID,USERNAME,LANG_DEF))
        
    
        
def select_user(user_id):
    with sqlite3.connect('users.db') as connection :
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT * FROM users WHERE id = ?;
                       """,(user_id,))

        return cursor.fetchone()
def select_all():
    with sqlite3.connect('users.db') as connection :
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT * FROM users;
                       """)
        return cursor.fetchall()
def set_language(id_user , lang):
    
    with sqlite3.connect('users.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                           Update users SET lang_def = ? WHERE id = ?;
                           """ , (lang , id_user))
    connection.commit()