import os
import sys
import stat
from datetime import datetime

def list_files(show_details=False, add_suffix=False):
    for entry in os.listdir('.'):
        entry_path = os.path.join('.', entry)
        entry_stat = os.stat(entry_path)

        # Default display
        if not show_details:
            if add_suffix:
                if stat.S_ISDIR(entry_stat.st_mode):
                    entry += '/'
                elif os.access(entry_path, os.X_OK):
                    entry += '*'
            print(entry)
        
        # Detailed listing
        if show_details:
            last_modified = datetime.fromtimestamp(entry_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            size = entry_stat.st_size if stat.S_ISREG(entry_stat.st_mode) else 0

            if add_suffix:
                if stat.S_ISDIR(entry_stat.st_mode):
                    entry += '/'
                elif os.access(entry_path, os.X_OK):
                    entry += '*'

            print(f"{last_modified} {size} {entry}")

def print_help():
    help_text = """Usage: pyls [options]
Options:
  -F        Append indicator (one of */=@|) to entries
  -l        Use a long listing format
  -h, --help  Display this help and exit
"""
    print(help_text)

def main():
    if len(sys.argv) == 1:
        list_files()
    elif len(sys.argv) == 2:
        if sys.argv[1] in ['-h', '--help']:
            print_help()
        elif sys.argv[1] == '-F':
            list_files(add_suffix=True)
        elif sys.argv[1] == '-l':
            list_files(show_details=True)
        elif sys.argv[1] == '-l' and sys.argv[1] == '-F':
            list_files(show_details=True, add_suffix=True)
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print_help()
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-l' and sys.argv[2] == '-F':
            list_files(show_details=True, add_suffix=True)
        elif sys.argv[1] == '-F' and sys.argv[2] == '-l':
            list_files(show_details=True, add_suffix=True)
        else:
            print(f"Unknown options: {sys.argv[1]} {sys.argv[2]}")
            print_help()
    else:
        print(f"Too many arguments.")
        print_help()

if __name__ == '__main__':
    main()
