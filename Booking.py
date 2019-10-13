import os
from user import User
from package import Package
from record import Record

class Booking:
    def __init__(self):
        self.booking_id= ''
        self.package_id = ''
        self.guest_id = ''
        self.head_count = ''
        self.amount_due = ''
        self.receipt_number = ''
        self.payment_status = ''


    def save(self):
        query = "insert into reservations(package_id, guest_id, head_count, amount_due, receipt_number, payment_status)" \
                "VALUES('{0}','{1}','{2}','{3}','{4}','{5}');".format(self.package_id, self.guest_id, self.head_count, self.amount_due, self.receipt_number, self.payment_status)
        Record.runQuery(query)

    def update(self):
        query = "update reservations set guest_id = {0}, head_count = {1},  amount_due = {2}, receipt_number = {3}, payment_status = {4} where booking_id = {5};"\
            .format(self.package_id, self.guest_id, self.head_count, self.amount_due, self.receipt_number, self.payment_status, self.booking_id)

        Record.runQuery(query)


    @staticmethod
    def getRecords():
        query = "select * from reservations;"
        reservationRecords = Record.fetchAllRecord(query)

        return reservationRecords

    @staticmethod
    def printBookingRecords():
        Records = Booking.getRecords()
        os.system('clear')
        print(
            "-------------------------------------------------------------------------BOOKING RECORDS----------------------------------------------------------------------------------")
        for row in Records:
            userModel = User.getbyID(row[2])
            eventModel = Package.getbyID(row[1])
            fullName = userModel.setFullname()
            eventName = eventModel.event_name
            print(
                '| Booking ID: {} | Event Name: {} | Guest Full Name: {} | Participants: {} | Amount Due: {} | Receipt Number: {} | Payment Status: {}|'.format(row[0], eventName, fullName, row[3], row[4], row[5], row[6]))
            print(
                "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")