# William MOon
# CIS 261
# Week 4 Lab 2 Country

#Function display Heading and Menu
def show_menu():
    print("Main Menu")
    print("----------------------------")
    print("list - List All Contries")
    print("add - Add a Country")
    print("del - Delete a Country")
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
def list(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.\n")
    else:
        print("There is no country with that code.\n")
 
#Function to Add to dictionary
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")

#Function do remove from dictionary
def remove(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code.\n")

#Function do remove from dictionary
def main():
    countries = {"GR": "Greece",
                 "US": "United States",
                 "NZ": "New Zeland"}
    
    show_menu()
    while True:        
        command = input("Command: ")
        command = command.lower()
        if command == "list":
            list(countries)   
        elif command == "add":
            add(countries)
        elif command == "del":
            remove(countries)  
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()


