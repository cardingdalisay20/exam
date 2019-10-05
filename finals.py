from user import User
from package import Package
from booking import Booking
import os


def ask(args):
    if args == 1:
        register()
    elif args == 2:
        createPackage()
    elif args == 3:
        bookTour()
    elif args == 4:
        checkBooking()
    elif args == 5:
        updateBooking()
    elif args == 6:
        cancelBooking()
    elif args == 7:
        exit()

# displays the main menu
def menu():
    print("****************************")
    print("* 1. REGISTER CUSTOMER     *")
    print("* 2. CREATE TOUR PACKAGE   *")
    print("* 3. BOOK A TOUR           *")
    print("* 4. CHECK BOOKING         *")
    print("* 5. UPDATE BOOKING        *")
    print("* 6. CANCEL BOOKING        *")
    print("* 7. EXIT                  *")
    print("****************************")

# registers customer
def register():
    os.system('clear')
    model = User()

    model.setFname(raw_input("First Name: "))
    model.setLname(raw_input("Last Name: "))
    model.setAddress(raw_input("Address: "))
    model.setContact(raw_input("Contact Number: "))
    model.setFullname()

    print(model.full_name)

# create tour packages
def createPackage():
    print("create package")

# book tour packages
def bookTour():
    print("book tour")

# check existing booking record
def checkBooking():
    print("check booking")

# update existing booking record
def updateBooking():
    print("update booking")

# cancel existing booking record
def cancelBooking():
    print("cancel booking")

# initializes the program
def start():
    os.system('clear')
    menu()
    try:
        args = int(input("PLEASE CHOOSE YOUR OPTION: "))
        ask(args)
    except ValueError:
        print("\n")
        print("ERROR! PLEASE CHOOSE THE CORRECT OPTION FROM THE MENU!")
        menu()

start()