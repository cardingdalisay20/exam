from record import Record

class User:
    def __init__(self):
        self.user_id = ''
        self.first_name = ''
        self.last_name = ''
        self.full_name = ''
        self.address = ''
        self.contact_number = ''

    def __repr__(self):
        return "User: {}".format(self.full_name)

    def setFname(self, args):
        self.first_name = args

    def setLname(self, args):
        self.last_name = args

    def setAddress(self, args):
        self.address = args

    def setContact(self, args):
        self.contact_number = args

    def setFullname(self):
        self.full_name = self.first_name + ' ' + self.last_name

    def save(self):
        query = "insert into users(first_name, last_name, address, contact_number)" \
                "VALUES('{0}','{1}','{2}','{3}');".format(self.first_name, self.last_name, self.address, self.contact_number)
        Record.runQuery(query)

    @staticmethod
    def getbyID(userID):
        query = "select * from users where user_id = ('{}');".format(userID)
        userRecord = Record.fetchRecord(query)
        return userRecord








