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
taskList.addTask(task)
taskList.addTask(task2)
taskList.addTask(task3)

print("after adding into task list, printing list")
for task in taskList.getTasks():
    print(task)

for task in taskList.getTasks():
    print(task)

taskList.removeTask(task2)

print("removing task2 with 2024 date")
for task in taskList.getTasks():
    print(task)

for task in taskList.getTasks():
    print(task)

print("clearing task list")
taskList.clearTasks()

for task in taskList.getTasks():
    print(task)