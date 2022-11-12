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
    user_name = input("Please Enter your Full Name: ")
    user_age = input("Please Enter your Age: ")
    user_address = input("Please Enter your Address: ")
    user_pernum = input("Please Enter your Contact Number: ")
    print("Saved")
