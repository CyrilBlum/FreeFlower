from sqlite3 import *

# Verbindung zur DB game.db öffnen
with connect("game.db") as con:
    # Datenbank-Cursor (=Lese/Schreibestift) holen
    cursor = con.cursor()
    
    # SQL-Code zur Erstellung der Tabelle
    sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user VARCHAR(40),
            password VARCHAR(40) 
        )
    """
    
    # SQL ausführen
    cursor.execute(sql)

    print("Table users was created!")