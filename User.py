from record import Record
import os
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
        return self.full_name

    def save(self):
        query = "insert into users(first_name, last_name, address, contact_number)" \
                "VALUES('{0}','{1}','{2}','{3}');".format(self.first_name, self.last_name, self.address, self.contact_number)
        Record.runQuery(query)

    @staticmethod
    def getbyID(userID):
        query = "select * from users where user_id = ('{}');".format(userID)
        userRecord = Record.fetchSingleRecord(query)
        model = User()
        model.user_id = userRecord[0]
        model.first_name = userRecord[1]
        model.last_name = userRecord[2]
        model.address = userRecord[3]
        model.contact_number = userRecord[4]
        model.full_name = model.setFullname()

        return model

    @staticmethod
    def getRecords():
        query = "select * from users;"
        userRecords = Record.fetchAllRecord(query)

        return userRecords

    @staticmethod
    def printUserRecords():
        Records = User.getRecords()
        os.system('clear')

        print("-----------------------------------------------------USER RECORDS------------------------------------------------------------")
        for row in Records:
            print('| ID: {} | First Name: {} | Last Name: {} | Address: {} | Phone: {} |'.format(row[0],row[1],row[2],row[3],row[4]))
            print("-----------------------------------------------------------------------------------------------------------------------------")

















