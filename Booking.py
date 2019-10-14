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
        query = "update reservations set package_id = {0}, guest_id = {1},  head_count = {2}, amount_due = {3}, receipt_number = {4}, payment_status = '{5}' where booking_id = {6};"\
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