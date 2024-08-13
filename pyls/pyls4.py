import os
import sys
import stat
from datetime import datetime
import pytest
import argparse

#Issue 1

def list_files(directory="."):
    """
    Look inside a folder to see what files are there.
    
    Args:
        directory (str): The folder you want to check out. Defaults to the current one.
        
    Returns:
        list: All the files and folders inside.
    """
    assert isinstance(directory, str), "Directory name should be a string"
    
    try:
        return os.listdir(directory)
    except Exception as e:
        print(f"Oops, couldn't list files in {directory}: {e}", file=sys.stderr)
        return []

#Issue 2
#Issue 3

def format_file_info(file_name, long_format=False, show_suffix=False):
    """
    Gives out file info in the format you want.
    
    Args:
        file_name (str): The name of the file or folder you want information about.
        long_format (bool): Set this to True for more details.
        show_suffix (bool): Set this to True to show if its a dictionary or executable.
    
    Returns:
        str: A string with the file info.
    """
    assert isinstance(file_name, str), "file_name should be a string"
    assert isinstance(long_format, bool), "long_format should be a bool"
    assert isinstance(show_suffix, bool), "show_suffix should be a bool"
    
    output = file_name
    
    if long_format:
        try:
            file_stats = os.stat(file_name)
            last_modified = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            size = file_stats.st_size if os.path.isfile(file_name) else 0
            output = f"{last_modified} {size:10} {file_name}"
        except Exception as e:
            print(f"Sorry, couldn't get stats for {file_name}: {e}", file=sys.stderr)
            return file_name
    
    if show_suffix:
        if os.path.isdir(file_name):
            output += '/'
        elif os.access(file_name, os.X_OK) and not os.path.isdir(file_name):
            output += '*'
    
    return output

#Issue 4
#Issue 5

def main(args):
    """
    The main function that reads your command-line arguments and acts accordingly.
    
    Args:
        args (list): A list of arguments you pass in from the command line.
    """
    parser = argparse.ArgumentParser(description="A basic version of the 'ls' command.")
    parser.add_argument("-F", action="store_true", help="Show if it's a directory or executable with a suffix.")
    parser.add_argument("-l", action="store_true", help="Show detailed info for each file.")
    args = parser.parse_args(args)
    
    files = list_files()
    for file in files:
        print(format_file_info(file, long_format=args.l, show_suffix=args.F))

if __name__ == "__main__":
    main(sys.argv[1:])

#Issue 6

def test_list_files():
    # Quick test to see if list_files works
    files = list_files()
    assert "example.txt" in files

def test_format_file_info():
    # Quick test to see if format_file_info works
    formatted_info = format_file_info("example.txt", long_format=True)
    assert "example.txt" in formatted_info
