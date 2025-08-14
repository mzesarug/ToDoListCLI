class Task:

    def __init__(self, deadline, name, description, category):
        self.__deadline = deadline
        self.__name = name
        self.__description = description
        self.__category = category
        self.__isFinished = False

    def __eq__(self, other):
        if not isinstance(other, Task):
            print("Error: Comparison with non-Task object")
            return False
        return (self.__deadline == other.__deadline and
                self.__name == other.__name and
                self.__description == other.__description and
                self.__category == other.__category and
                self.__isFinished == other.__isFinished)
    
    def markAsFinished(self):
        self.__isFinished = True

    def isFinished(self):
        return self.__isFinished
    
    def setDeadline(self, deadline):
        self.__deadline = deadline

    def getDeadline(self):
        return self.__deadline
    
    def setName(self, name):
        self.__name = name  

    def getName(self):
        return self.__name
    
    def setDescription(self, description):
        self.__description = description   

    def getDescription(self):
        return self.__description
    
    def setCategory(self, category):
        self.__category = category

    def getCategory(self):
        return self.__category

    def __str__(self):
        return f"Task(name={self.name}, description={self.description}, completed={self.completed}, category={self.category}, deadline={self.deadline})"