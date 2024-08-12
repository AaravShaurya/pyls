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
    
    if long_format:
        try:
            file_stats = os.stat(file_name)
            last_modified = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            size = file_stats.st_size if os.path.isfile(file_name) else 0
            output = f"{last_modified} {size:10} {file_name}"
        except Exception as e:
            print(f"Error retrieving stats for {file_name}: {e}", file=sys.stderr)
            return file_name
    
    return output
