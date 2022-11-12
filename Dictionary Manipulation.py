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
while True:
    menu_options()
    user_input = int(input("What do you want to do? "))

# Adding Option 1
    if user_input == 1:
        print("")
        user_name = str(input("Please Enter your Full Name: "))
        user_address = input("Please Enter your Address: ")
        try:
            user_age = int(input("Please Enter your Age: "))
            user_pernum = int(input("Please Enter your Contact Number: "))

        except ValueError:
            print("")
            print("No, No, No, No. Invalid Input User.")
            break

        else:
            # Adding of inputted data to dictionary
            contact_info[user_name] = {
                "Age: ": user_age,
                "Address: ": user_address,
                "Number: ": user_pernum
            }
            print("")
            print("All of the information that you have entered is saved.")

# Adding of Option 2
    elif user_input == 2:
        user_search = str(input("Please Enter the Full Name of whom you seek: "))
        if user_search in contact_info:
            for key, value in contact_info[user_search].items():
                print(key, value)

        else:
            print("That person doesn't exist in my database.")
            break

# Adding of Option 3
    elif user_input == 3:
        print("")
        confirmation = str(input("Do you wish to exit? (y/n): "))
        if confirmation == "y":
            print("")
            print("Thank you for using the program!!!")
            break
        else:
            continue

# Adding of Else Statement
    else:
        print("I am sorry, your input command is invalid.")
        break

# Adding of Additional Question
    print("")
    add_question = str(input("Would you like to continue? (y/n) "))
    if add_question == "y":
        continue
    else:
        print("")
        print("Thank you for using the program!!!")
        break