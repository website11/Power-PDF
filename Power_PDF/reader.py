
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        return file.read()