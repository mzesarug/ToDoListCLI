from Date import Date
from Task import Task
from TaskList import TaskList
from FileManager import FileManager
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static

class TaskMaster(App):
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Welcome to TaskMaster!", classes="centered")
        yield Button("Add Task", id="add_task_button", classes="button")
        yield Button("View Tasks", id="view_tasks_button", classes="button")
        yield Button("Save Tasks", id="save_tasks_button", classes="button")
        yield Button("Load Tasks", id="load_tasks_button", classes="button")
        yield Button("Clear Tasks", id="clear_tasks_button", classes="button")

if __name__ == "__main__":
    app = TaskMaster()
    app.run()

