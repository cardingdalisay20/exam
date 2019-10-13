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