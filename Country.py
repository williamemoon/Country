# William MOon
# CIS 261
# Week 4 Lab 2 Country

#Function display Heading and Menu
def show_menu():
    print("Main Menu")
    print("----------------------------")
    print("search - Country Name form Country Code")
    print("add - Add a Country and Country Code")
    print("del - Delete a Country and Country Code")
    print("exit - Exit the program")
    print(" ")

#Function to list countries
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

#Function to view country by code
def show(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.")
        print(" ")
    else:
        print("There is no country with that code.")
        print (" ")
 
#Function to Add to dictionary
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.")
        print (" ")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.")
        print (" ")

#Function do remove from dictionary
def remove(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.")
        print (" ")
    else:
        print("There is no country with that code.")
        print (" ")

#Function do remove from dictionary
def main():
    countries = {"GR": "Greece",
                 "US": "United States",
                 "NZ": "New Zeland"}
    
    show_menu()
    while True:        
        command = input("Command: ")
        command = command.lower()
        if command == "search":
            show(countries)   
        elif command == "add":
            add(countries)
        elif command == "del":
            remove(countries)  
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
            print (" ")


if __name__ == "__main__":
    main()


