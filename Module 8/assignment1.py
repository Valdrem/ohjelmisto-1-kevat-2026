import mysql.connector
conn = mysql.connector.connect(host='127.0.0.1',port= 3306,database='flight_game',user='root',password='pass03',autocommit=True)

icao_code = input("Enter the ICAO code of an airport: ")

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor = conn.cursor()
cursor.execute(sql, (icao_code.upper(),))
rs = cursor.fetchall()

if len(rs) > 0:
    print(f"Airport name: {rs[0][0]} \nLocation: {rs[0][1]}")
else:
    print(f"No airport found with ICAO code {icao_code.upper()}")