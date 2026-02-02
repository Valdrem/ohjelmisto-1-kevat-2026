guide = "\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit"

print(guide)
u_response = input("Please choose an option (1-3): ")

airports = {}

while u_response != "3":
    if u_response == "1":
        new_airport_icao = input("Enter the ICAO code: ")
        new_airport = input("Enter the airport name: ")
        airports[new_airport_icao] = new_airport
        print(f"Airport {new_airport} with ICAO code {new_airport_icao} has been added.")

    elif u_response == "2":
        icao_code = input("Enter the ICAO code: ")
        if icao_code in airports:
            print(f"The airport with ICAO code {icao_code} is {airports[icao_code]}.")
        else:
            print(f"No airport found with ICAO code {icao_code}.")

    print(guide)
    u_response = input("Please choose an option (1-3): ")

print("Thank you for using the Airport Data Management system. Goodbye!")