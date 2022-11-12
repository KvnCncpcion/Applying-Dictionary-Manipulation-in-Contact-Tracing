print("********************PROGRAMMED BY***************************")
print("*****************Kevin Joseph G. Concepcion*****************")
print("******************BSCOE 2-2*********************************")

# Declaring Empty Dictionary
contact_info = {}

# Adding of Menu
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
    # Adding of data to dictionary
    contact_info[user_name] = {
        "Age: ": user_age,
        "Address: ": user_address,
        "Number: ": user_pernum
    }
    print("All of the information that you have entered is saved.")



