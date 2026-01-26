username = input("Enter username: ")
password = input("Enter password: ")

attempt = 1

while username != "python" and password != "rules":
    if attempt < 5:
        print("Incorrect username or password. Please try again.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        attempt = attempt + 1
    else:
        print("Access denied")
        break
else:
    print("Welcome")