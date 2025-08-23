class FileManager:
    def __init__(self):
        pass

    def readListFromFile(self, filePath):
        try:
            with open(filePath, 'r') as file:
                items = file.readlines()
                return [item.strip() for item in items if item.strip()]
        except FileNotFoundError:
            print(f"Error: The file {filePath} does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []
        
    # Note* this will also overwrite all tasks on file, we can add an append function later if needed
    def writeListToFile(self, filePath, items):
        try:
            with open(filePath, 'w') as file:
                for item in items:
                    file.write(f"{item}\n")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    def clearFile(self, filePath):
        try:
            open(filePath, 'w').close()
        except Exception as e:
            print(f"An error occurred while clearing the file: {e}")

