import pandas as pd
def console_input():
    """returns input text from the console."""
    return input("Enter your text: ")
def read_with_help(file_path):
    """reads and returns content from a file."""
    with open(file_path, 'r') as file:
        return file.read()
def read_from_file_with_pandas(file_path):
    """reads and returns the first table from html file as a dataframe."""
    tables = pd.read_html(file_path)
    return tables[0] if tables else None