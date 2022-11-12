print("********************PROGRAMMED BY***************************")
print("*****************Kevin Joseph G. Concepcion*****************")
print("******************BSCOE 2-2*********************************")

# Declaring Empty Dictionary
contact_info = {}

# Adding of Menu
def menu_options():
    print("")
    print("============== MENU ================")
    print("1 -> Add an Item")
    print("2 -> Search")
    print("3 -> Exit (y/n)")
    print("")

# Adding of Question for User Input
user_input = int(input("What do you want to do? "))

# Adding Option 1
if user_input == 1:
    print("")
    user_name = str(input("Please Enter your Full Name: "))
    user_age = int(input("Please Enter your Age: "))
    user_address = str(input("Please Enter your Address: "))
    user_pernum = int(input("Please Enter your Contact Number: "))
    # Adding of inputted data to dictionary
    contact_info[user_name] = {
        "Age: ": user_age,
        "Address: ": user_address,
        "Number: ": user_pernum
    }
    print("All of the information that you have entered is saved.")

# Adding of Option 2
if user_input == 2:
    user_search = str(input("Please Enter the Full Name of whom you seek: "))
    if user_search in contact_info:
        for key, value in contact_info[user_search].items():
            print(key, value)

    else:
        print("That person doesn't exist in my database.")

# Adding of Option 3
if user_input == 3:
    print("")
    print("Thank you for using the program!!!")
    break

