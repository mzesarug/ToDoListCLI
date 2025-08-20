import heapq


class TaskList:

    def __init__(self):
        self.__tasks = []
        self.__taskMap = {}
        self.__counter = 0
        self.__deletedTask = '<deleted>'

    def addTask(self, task):
        # we cannot have duplicates, the priority queueu will automatically delete them if trying to add an exact duplicate
        if task in self.__taskMap:
            self.removeTask(task)
        count = self.__counter
        self.__counter += 1
        entry = [task.getDeadline(), count, task]
        self.__taskMap[task] = entry
        heapq.heappush(self.__tasks, entry)

    def removeTask(self, task):
        entry = self.__taskMap.pop(task)
        entry[-1] = self.__deletedTask

    def pop_task(self):
        while self.__tasks:
            deadline, count, task = heapq.heappop(self.__tasks)
            if task is not self.__deletedTask:
                if task in self.__taskMap:
                    del self.__taskMap[task]
                return task
        # raise KeyError('task list is empty')
        print("Error: Task list is empty")

    def getTasks(self):
        return [entry[2] for entry in self.__tasks if entry[2] != self.__deletedTask]

    def clearTasks(self):
        self.__tasks.clear()

    def __str__(self):
        return "\n".join(str(entry[2]) for entry in self.__tasks if entry[2] != self.__deletedTask) if self.__tasks else "No tasks available."

