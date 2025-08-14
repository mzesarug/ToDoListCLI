class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = 0
        self.__minute = 0

    def __init__(self, year, month, day, hour):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour
        self.__minute = 0

    def __init__(self, year, month, day, hour, minute):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour
        self.__minute = minute

    def getYear(self):
        return self.__year
    
    def getMonth(self):
        return self.__month       
    
    def getDay(self):
        return self.__day
    
    def getHour(self):
        return self.__hour    
    
    def getMinute(self):
        return self.__minute
    
    def setYear(self, year):
        self.__year = year

    def setMonth(self, month):
        self.__month = month 

    def setDay(self, day):
        self.__day = day  

    def setHour(self, hour):
        self.__hour = hour    

    def setMinute(self, minute):
        self.__minute = minute

    def __eq__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.__year == other.__year and
                self.__month == other.__month and
                self.__day == other.__day and
                self.__hour == other.__hour and
                self.__minute == other.__minute)
    
    def __lt__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.__year, self.__month, self.__day, self.__hour, self.__minute) < \
               (other.__year, other.__month, other.__day, other.__hour, other.__minute)
    
    def __le__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.__year, self.__month, self.__day, self.__hour, self.__minute) <= \
               (other.__year, other.__month, other.__day, other.__hour, other.__minute)
    
    def __gt__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.__year, self.__month, self.__day, self.__hour, self.__minute) > \
               (other.__year, other.__month, other.__day, other.__hour, other.__minute)
    
    def __ge__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return False
        return (self.__year, self.__month, self.__day, self.__hour, self.__minute) >= \
               (other.__year, other.__month, other.__day, other.__hour, other.__minute)
    
    def __ne__(self, other):
        if not isinstance(other, Date):
            print("Error: Comparison with non-Date object")
            return True
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}-{self.__hour:02d}:{self.__minute:02d}"
    
    def getDateUntilDay(self):
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}"
    
    def getDateUntilHour(self):
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}-{self.__hour:02d}"
    
    def getDateFull(self):
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}-{self.__hour:02d}:{self.__minute:02d}"