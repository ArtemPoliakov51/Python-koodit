import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True,
    )
rep = input("Syötä lentoaseman ICAO-koodi: ").upper()

def print_countries(rep):
    sql = "SELECT name, municipality FROM airport"
    sql += f"WHERE ident = '{rep}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Lentoaseman nimi on {row[0]} ja se on sijaintikunnassa {row[1]}")
            return

print_countries(rep)