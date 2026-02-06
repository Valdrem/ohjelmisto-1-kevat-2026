import mysql.connector
conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='pass03',
    autocommit=True
)

def get_airports_by_country(country):
    sql = "SELECT name, type FROM airport WHERE iso_country = %s ORDER BY type"
    cur = conn.cursor()
    cur.execute(sql, (country.upper(),))
    rs = cur.fetchall()
    cur.close()
    return rs


def run_country_program():
    country = input("Enter the country code (e.g., FI for Finland): ")
    rs = get_airports_by_country(country)
    if len(rs) > 0:
        print(f"\n\nAirports in {country}:")
        for row in rs:
            print(f"{row[1]} {row[0]} airports")
    else:
        print(f"No airports found for country code '{country}'.")

run_country_program()