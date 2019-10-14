import os
from user import User
from package import Package
from record import Record
from booking import Booking

# validating the menu choices
def check(args):
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
        check_db()
    elif args == 8:
        exit()

# menu for adding inclusions yes or no
def option(message):
    key = raw_input("{}? [Y]es/[N]o: " . format(message))
    return key

# displays the main menu
def menu():
    print("****************************")
    print("* 1. REGISTER CUSTOMER     *")
    print("* 2. CREATE EVENT          *")
    print("* 3. BOOK A TOUR           *")
    print("* 4. CHECK BOOKING         *")
    print("* 5. UPDATE BOOKING        *")
    print("* 6. CANCEL BOOKING        *")
    print("* 7. CHECK DB CONNECTION   *")
    print("* 8. EXIT                  *")
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

    choice = option("Would you like to save changes")
    if choice == "Y":
        model.save()
        print("User records successfully saved!")
    else:
        start()
    choice = option("Would you like to register another user")
    if choice == "Y":
        register()
    else:
        start()

# create tour packages
def createPackage():
    os.system('clear')
    event = Package()
    event.setEventName(raw_input("Event Name: "))
    event.setLocation(raw_input("Event Location: "))
    event.setDuration(raw_input("Duration in Hrs: "))
    event.setRate(raw_input("Rate per Head: "))
    event.addInclusion(raw_input("Inclusion: "))

    choice = option("Would you like to save changes")
    if choice == "Y" or "y":
        event.save()
        print("Event records successfully saved!")
    else:
        start()
    choice = option("Would you like to create another event")
    if choice == "Y" or "y":
        createPackage()
    else:
        start()

# book tour packages
def bookTour():
    User.printUserRecords()
    print("PLEASE SELECT FROM USER RECORDS")
    user_id = int(raw_input("User ID: "))
    userModel = User.getbyID(user_id)

    Package.printPackageRecords()
    print("PLEASE SELECT FROM EVENT PACKAGES")
    event_id = int(raw_input("Event ID: "))
    packageModel = Package.getbyID(event_id)
    head_count = int(raw_input("Number of participants: "))
    amount = packageModel.head_rate
    totalAmount = head_count * amount

    choice = option("Do you have a deposit slip")
    if choice == "Y" or "y":
        receipt_number = int(raw_input("Deposit receipt number: "))
        payment_status = 'paid'
    else:
        receipt_number = ''
        payment_status = 'unpaid'

    bookModel = Booking()
    bookModel.package_id = packageModel.event_id
    bookModel.guest_id = userModel.user_id
    bookModel.head_count = head_count
    bookModel.amount_due = totalAmount
    bookModel.receipt_number = receipt_number
    bookModel.payment_status = payment_status

    choice = option("Would you like to save changes")
    if choice == "Y":
        bookModel.save()
        print("User successfully booked!")
    else:
        start()
    choice = option("Would you like to book another user")
    if choice == "Y":
        bookTour()
    else:
        start()

# check existing booking record
def checkBooking():
    Booking.printBookingRecords()

    choice = option("Would you like to exit to main menu")
    if choice == "Y":
        start()
    else:
        exit()

def updateBooking():
    Booking.printBookingRecords()
    print("PLEASE SELECT FROM BOOKING RECORDS")
    booking_id = int(raw_input("Book ID: "))

    Package.printPackageRecords()
    print("PLEASE SELECT FROM EVENT RECORDS")
    event_id = int(raw_input("Event ID: "))

    User.printUserRecords()
    print("PLEASE SELECT FROM USER RECORDS")
    guest_id = int(raw_input("User ID: "))
    userModel = User.getbyID(guest_id)
    head_count = int(raw_input("Number of participants: "))
    packageModel = Package.getbyID(event_id)
    amount = packageModel.head_rate
    totalAmount = head_count * amount

    choice = option("Do you have a deposit slip")
    if choice == "Y" or "y":
        receipt_number = int(raw_input("Deposit receipt number: "))
        payment_status = 'paid'
    else:
        receipt_number = ''
        payment_status = 'unpaid'

    bookModel = Booking()
    bookModel.booking_id = booking_id
    bookModel.package_id = packageModel.event_id
    bookModel.guest_id = userModel.user_id
    bookModel.head_count = head_count
    bookModel.amount_due = totalAmount
    bookModel.receipt_number = receipt_number
    bookModel.payment_status = payment_status

    choice = option("Would you like to save changes")
    if choice == "Y":
        bookModel.update()
        print("Record successfully updated!")
    else:
        start()

    choice = option("Would you like to update another booking")
    if choice == "Y":
        updateBooking()
    else:
        start()


# cancel existing booking record
def cancelBooking():
    print("cancel booking")

def check_db():
    Record.checkConnection()

    # initializes the program
def start():
    os.system('clear')
    menu()
    try:
        args = int(input("PLEASE CHOOSE YOUR OPTION: "))
        check(args)
    except ValueError:
        print("\n")
        print("ERROR! PLEASE CHOOSE THE CORRECT OPTION FROM THE MENU!")
        menu()

start()