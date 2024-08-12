import pytest
from pyls import list_files, format_file_info

def test_list_files():
    files = list_files(".")
    assert isinstance(files, list), "The result should be a list"
    assert all(isinstance(f, str) for f in files), "Each item in the list should be a string"

def test_format_file_info_simple():
    output = format_file_info("test_file.py")
    assert output == "test_file.py", "Simple format should return the file name"

def test_format_file_info_long_format():
    output = format_file_info("test_file.py", long_format=True)
    assert "test_file.py" in output, "Long format should include the file name"

def test_format_file_info_suffix():
    output = format_file_info("test_file.py", show_suffix=True)
    assert output == "test_file.py", "Non-executable file should not have a suffix"

    output = format_file_info("test_dir", show_suffix=True)
    assert output == "test_dir/", "Directory should have a '/' suffix"

def test_format_file_info_long_and_suffix():
    output = format_file_info("test_file.py", long_format=True, show_suffix=True)
    assert "test_file.py" in output, "Combined format should include file name and long format details"
