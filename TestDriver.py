# The purpose of this file is to freely instantiate objects and test them
from Task import Task
from Date import Date
from TaskList import TaskList

date = Date(2023, 12, 31, 23, 59)
date2 = Date(2024, 12, 31, 23, 59)
date3 = Date(2022, 12, 31, 23, 59)
print(date)
print(date2)    
print(date3)

task = Task(date, "Test Task", "This is a test task", "High")
task2 = Task(date2, "Test Task", "This is a test task", "High")
task3 = Task(date3, "Test Task", "This is a test task", "High")
print(task)
print(task2)
print(task3)

taskList = TaskList()
taskList.add_task(task)
taskList.add_task(task2)
taskList.add_task(task3)

print("after adding into task list, printing list")
for task in taskList.get_tasks():
    print(task)

for task in taskList.get_tasks():
    print(task)

taskList.remove_task(task2)

"removing task2 with 2024 date"
for task in taskList.get_tasks():
    print(task)

for task in taskList.get_tasks():
    print(task)