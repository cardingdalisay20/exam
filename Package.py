class Package:

    def __init__(self):
        self.event_name = ''
        self.location = ''
        self.duration_hours = ''
        self.head_rate = ''
        self.inclusion = []

    def __repr__(self):
        return "<Package: {}>".format(self.event_name)

    def setEventName(self, args):
        self.event_name = args

    def setLocation(self, args):
        self.location = args

    def setDuration(self, args):
        self.duration_hours = args

    def setRate(self, args):
        self.head_rate = args

    def addInclusion(self, args):
        self.inclusion.append(args)