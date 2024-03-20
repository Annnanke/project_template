def console_output(text):
    """prints text to the console."""
    print(text)
def write_to_file(text, file_path):
    """writes text to a specified file."""
    with open(file_path, 'w') as file:
        file.write(text)
