import sqlite3
import baza

conn = sqlite3.connect("baza.sqlite3")

baza.pripravi_vse(conn)

class Model:
    
    def dobi_vse_uporabnike(self):
        with conn:
            cur = conn.execute("""
                         select * from uporabnik
                         """)
            return cur.fetchall()