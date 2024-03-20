import pandas as pd
def console_input():
    """returns input text from the console."""
    return input("Enter your text: ")
def read_with_help(file_path):
    """reads and returns content from a file."""
    with open(file_path, 'r') as file:
        return file.read()
def read_from_file_with_pandas(file_path):
    """reads and returns a csv file as a dataframe."""
    return pd.read_csv(file_path)
