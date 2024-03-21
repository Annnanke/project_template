from app.io.output import console_output, write_to_file
import os

TESTS_DIR = 'tests'
OUTPUT_FILE_PATH = f'{TESTS_DIR}/output_test.txt'
os.makedirs(TESTS_DIR, exist_ok=True)

def capture_console_output(text):
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        console_output(text)
    return f.getvalue()

def test_console_output():
    """Test 1: prints text to the console."""
    text = "this is Console!"
    captured_output = capture_console_output(text)
    assert text in captured_output, "The text should be in the captured output."

def test_write_to_file():
    """Test 2: writes text to a specified file."""
    text = "this is  File!"
    write_to_file(text, OUTPUT_FILE_PATH)
    with open(OUTPUT_FILE_PATH, 'r') as file:
        file_content = file.read()
    assert text == file_content, "The written text should match the input text."

def test_write_empty_to_file():
    """Test 3: writes empty text to a file."""
    text = ""
    write_to_file(text, OUTPUT_FILE_PATH)
    with open(OUTPUT_FILE_PATH, 'r') as file:
        file_content = file.read()
    assert text == file_content, "The file should be empty."
