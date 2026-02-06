import geopy
from geopy import distance

import mysql.connector
conn = mysql.connector.connect(host='127.0.0.1',port=3306,database='flight_game',user='root',password='pass03',autocommit=True)

def get_airport_coordinates(icao1, icao2):
        sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s OR ident = %s"
        cur = conn.cursor()
        cur.execute(sql, (icao1.upper(), icao2.upper(),))
        coordinates = cur.fetchall()
        cur.close()
        return coordinates

def run_airport_distance():
        icao1 = input("Enter the ICAO code of the first airport: ")
        icao2 = input("Enter the ICAO code of the second airport: ")
        coordinates = get_airport_coordinates(icao1, icao2)
        if len(coordinates) == 2:
            dist_km = distance.distance(coordinates[0], coordinates[1]).km
            print(f"Distance between {icao1.upper()} and {icao2.upper()} is {dist_km:.2f} kilometers")
        else:
             print("No coordinates found")

run_airport_distance()