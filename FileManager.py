class FileManager:
    def __init__(self):
        pass

    def readListFromFile(self, filePath):
        try:
            with open(filePath, 'r') as file:
                tasks = file.readlines()
                return [task.strip() for task in tasks if task.strip()]
        except FileNotFoundError:
            print(f"Error: The file {filePath} does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []
        
    def writeListToFile(self, filePath, tasks):
        try:
            with open(filePath, 'w') as file:
                for task in tasks:
                    file.write(f"{task}\n")
            print(f"Tasks successfully written to {filePath}.")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

