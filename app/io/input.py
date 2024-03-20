import pandas as pd
def console_input():
    return input("Enter your text: ")
def read_with_help(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def read_from_file_with_pandas(file_path):
    return pd.read_csv(file_path)
