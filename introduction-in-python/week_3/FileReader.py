class FileReader:
    """Класс FileReader помогает читать из файла"""

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except IOError:
            return ""
