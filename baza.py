def ustvari_tabele(conn):
    with conn:
        conn.execute(
            """
            create table if not exists
            uporabnik(
                uid integer primary key,
                username text,
                name text
            )
            """
        )

def napolni_nujne_podatke(conn):
    with conn:
        conn.execute("""
                     insert into uporabnik
                     (username, name) values
                     ("uporabnisko", "ime")
                     """)

def pripravi_vse(conn):
    ustvari_tabele(conn)
    napolni_nujne_podatke(conn)