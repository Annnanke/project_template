import pandas as pd
import os

from app.io.input import read_with_help, read_from_file_with_pandas

TESTS_DIR = 'tests'
os.makedirs(TESTS_DIR, exist_ok=True)

# html for testing
html_content = '''
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>24</td>
  </tr>
</table>
'''
with open(f'{TESTS_DIR}/test_table.html', 'w') as f:
    f.write(html_content)

def test_1():
    """Test 1: reading text from a file."""
    expected = 'Hello, world!'
    result = read_with_help(f'{TESTS_DIR}/test.txt')
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_2():
    """Test 2: reading text from a nonexistant file"""
    try:
        read_with_help(f'{TESTS_DIR}/nonexistent.txt')
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        assert True


def test_3():
    """Test 3: reading a html file with pandas"""
    expected_df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [30, 24]})
    result_df = read_from_file_with_pandas(f'{TESTS_DIR}/test_table.html')
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_4():
    """Test 4: reading nonexistant html file with pandas"""
    try:
        read_from_file_with_pandas(f'{TESTS_DIR}/nonexistent.html')
        assert False, "Expected a ValueError indicating no tables were found"
    except ValueError as e:
        assert "No tables found" in str(e), "Expected ValueError indicating no tables were found"

def test_5():
    """Test 5:  reading empty text file."""
    empty_file_path = f'{TESTS_DIR}/empty.txt'
    with open(empty_file_path, 'w') as f:
        pass  # Create an empty file
    result = read_with_help(empty_file_path)
    assert result == '', "Expected empty string for empty file"

def test_6():
    """Test 6: reading an empty html file"""
    empty_html_path = f'{TESTS_DIR}/empty.html'
    with open(empty_html_path, 'w') as f:
        f.write('<html><head></head><body></body></html>')
    try:
        result = read_from_file_with_pandas(empty_html_path)
        assert False, "Expected a ValueError indicating no tables were found"
    except ValueError as e:
        assert "No tables found" in str(e), "Expected ValueError indicating no tables were found"