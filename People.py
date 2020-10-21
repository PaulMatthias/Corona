class People():
    """
    Describes the single People in a node
    """
    def __init__(self, name, home, work, sicknessStatus):
        self.name =  name
        self.homeNode = home
        self.workNode = work
        self.sicknessStatus = sicknessStatus
        
    def print(self):
        print(self.name, self.home, self.sicknessStatus)