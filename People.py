class People():
    """
    Describes the single People in a node
    """
    def __init__(self, name, home, sicknessStatus):
        self.name =  name
        self.home = home
        self.sicknessStatus = sicknessStatus
        
    def print(self):
        print(self.name, self.home, self.sicknessStatus)