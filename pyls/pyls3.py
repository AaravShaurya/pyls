#Issue 1

import os
import sys
import stat
from datetime import datetime

def list_files(directory="."):
    """
    Lists files and directories in the given directory.
    
    Args:
        directory (str): The directory to list the files and directories from.
        
    Returns:
        list: A list of file and directory names.
    """
    assert isinstance(directory, str), "directory must be a string"
    
    try:
        return os.listdir(directory)
    except Exception as e:
        print(f"Error listing files in directory {directory}: {e}", file=sys.stderr)
        return []

if __name__ == "__main__":
    files = list_files()
    for file in files:
        print(file)

#Issue 2

def format_file_info(file_name, long_format=False, show_suffix=False):
    """
    Formats file information based on provided options.
    
    Args:
        file_name (str): The name of the file or directory.
        long_format (bool): Whether to include long format details like last modified date and size.
        show_suffix (bool): Whether to add a suffix indicating directory or executable files.
    
    Returns:
        str: The formatted file information.
    """
    assert isinstance(file_name, str), "file_name must be a string"
    assert isinstance(long_format, bool), "long_format must be a boolean"
    assert isinstance(show_suffix, bool), "show_suffix must be a boolean"
    
    output = file_name
    
    if show_suffix:
        if os.path.isdir(file_name):
            output += '/'
        elif os.access(file_name, os.X_OK) and not os.path.isdir(file_name):
            output += '*'
    
    return output

