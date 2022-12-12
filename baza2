import sqlite3 

db = sqlite3.connect("baza.sqlite3")

with db as cursor:
    cursor.execute("""
                   Create table if not exists
                   user (uid integer primary key,
                   email text,
                   name text
                   )
                   """)
    
    
folk = [
    ("abc@gmail.com","ime 1"),
    ("abc@gmail.com","ime 2"),
    ("abc@gmail.com","ime 3"),
    ("abc@gmail.com","ime 4"),
    ("abc@gmail.com","ime 5"),
]

with db as cursor:
    # for (email,name) in folk:
    #     cursor.execute(f"""
    #                    insert into user (email,name)
    #                    values(?,?)""",(email,name)
    #                    )
    for (email,name) in folk:
        cursor.execute(f"""
                       insert into user (email,name)
                       values (:now_mail,:user_name)""",
                      {"now_mail":email, "user_name":name}
                       )
        

def napolni_uporabnike():
    with db as cursor:
    # for (email,name) in folk:
    #     cursor.execute(f"""
    #                    insert into user (email,name)
    #                    values(?,?)""",(email,name)
    #                    )
        for (email,name) in folk:
            cursor.execute(f"""
                       insert into user (email,name)
                       values (:now_mail,:user_name)""",
                      {"now_mail":email, "user_name":name}
                       )
            

with db as conn:
    cursor = conn.cursor()
    cursor.execute("select * from user")
    print(cursor.fetchall())
    cursor.execute("select * from user")
    print(cursor.fetchone())