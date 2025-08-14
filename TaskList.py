import heapq

class TaskList:

    __deletedTask = '<deleted>'

    def __init__(self):
        self.__tasks = []
        self.__taskMap = {}
        self.__counter = 0

    def add_task(self, task):
        count = self.__counter
        self.__counter += 1
        entry = (task.getDeadline(), count, task)
        self.__taskMap[task] = entry
        heapq.heappush(self.__tasks, entry)

    def remove_task(self, task):
        entry = self.__taskMap.pop(task)
        entry[-1] = self.deletedTask

    def pop_task(self):
        while self.__tasks:
            deadline, count, task = heapq.heappop(self.__tasks)
            if task is not self.__deletedTask:
                del self.__taskMap[task]
                return task
        raise KeyError('task list is empty')

    def get_tasks(self):
        returnList = []
        while self.__tasks:
            returnList.append(self.pop_task())
        for task in returnList:
            self.add_task(task)

        return returnList
                

    def clear_tasks(self):
        self.tasks.clear()

    def __str__(self):
        return "\n".join(self.tasks) if self.tasks else "No tasks available."