class Package:

    def __init__(self):
        self.package_name = ''
        self.location = ''
        self.duration_hours = ''
        self.price_per_head = ''
        self.inclusion = []

    def setPaxName(self):
        self.package_name = input("Package Name:")

    def setTourLoc(self):
        self.location = input("Tour Location: ")

    def setDuration(self):
        self.duration_hours = input("Number of Hours: ")

    def setRate(self, rate):
        self.pax_rate = input("Rate/Pax: ")

    def setInclusion(self):
        self.inclusion = input("Inclusions:")