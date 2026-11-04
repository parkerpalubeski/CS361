class API:
    def __init__ (self, file_name):
        self.file_name = file_name
        self.file_pointer = None

    def open(self):
        self.file_pointer = open_file(self.file_name)