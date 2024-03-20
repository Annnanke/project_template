from app.io.input import console_input, read_with_help, read_from_file_with_pandas
from app.io.output import console_output, write_to_file


def main():
    # Reading input from the console
    console_text = console_input()
    console_output(console_text)
    write_to_file(console_text, 'data/console_input.txt')

    # Reading content from a file using Python's built-in functionality
    file_content = read_with_help('data/sample.txt')
    console_output(file_content)
    write_to_file(file_content, 'data/read_output.txt')

    df = read_from_file_with_pandas('data/sample.csv')
    df_string = df.to_string()
    console_output(df_string)
    write_to_file(df_string, 'data/read_pandas_output.txt')


if __name__ == '__main__':
    main()
