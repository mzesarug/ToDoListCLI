class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.hour = 0
        self.minute = 0

    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = 0

    def __init__(self, year, month, day, hour, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month       
    
    def getDay(self):
        return self.day
    
    def getHour(self):
        return self.hour    
    
    def getMinute(self):
        return self.minute
    
    def setYear(self, year):
        self.year = year

    def setMonth(self, month):
        self.month = month 

    def setDay(self, day):
        self.day = day  

    def setHour(self, hour):
        self.hour = hour    

    def setMinute(self, minute):
        self.minute = minute

    def __eq__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.year == other.year and
                self.month == other.month and
                self.day == other.day and
                self.hour == other.hour and
                self.minute == other.minute)
    
    def __lt__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.year, self.month, self.day, self.hour, self.minute) < \
               (other.year, other.month, other.day, other.hour, other.minute)
    
    def __le__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.year, self.month, self.day, self.hour, self.minute) <= \
               (other.year, other.month, other.day, other.hour, other.minute)
    
    def __gt__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.year, self.month, self.day, self.hour, self.minute) > \
               (other.year, other.month, other.day, other.hour, other.minute)
    
    def __ge__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.year, self.month, self.day, self.hour, self.minute) >= \
               (other.year, other.month, other.day, other.hour, other.minute)
    
    def __ne__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return True
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"