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

