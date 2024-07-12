
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.count = 0

    def add_participant(self):
        self.count += 1
        
    def get_count(self):
        return self.count
    
event1 = Event("AnimeExpo", "10-11=-25")
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()
event1.add_participant()


print(event1.get_count())
        
    
        