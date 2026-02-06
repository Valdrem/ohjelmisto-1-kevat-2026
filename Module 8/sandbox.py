import mysql.connector

def get_airport():
    sql = f"SELECT name, ident FROM airport WHERE iso_country = 'FI' LIMIT 50"
    print(sql)
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    if cursor.rowcount > 0 :
        print(rs)
        for row in rs:
            print(f"Airport name: {row[0]}, {row[1]}.")
    return

conn = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='pass03',
         autocommit=True
         )

get_airport()