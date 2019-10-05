class User:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.full_name = ''
        self.address = ''
        self.contact_number = ''

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
