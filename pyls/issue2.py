import os
import sys
import stat
from datetime import datetime

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
