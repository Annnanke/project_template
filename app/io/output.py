def console_output(text):
    print(text)
def write_to_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)
