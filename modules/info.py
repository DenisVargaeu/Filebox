import os
from pathlib import Path
from system import clearscr as cl

def show_info(path):
    path = Path(path)
    print(f"File name: {path.name}")
    print(f"File suffix: {path.suffix}")
    print(f"File size: {path.stat().st_size} bytes")
    print(f"File last modified: {path.stat().st_mtime}")
    print(f"File last accessed: {path.stat().st_atime}")
    print(f"File creation time: {path.stat().st_ctime}")
    print(f"File absolute path: {path.resolve()}")
    print(f"File parent directory: {path.parent}")
    print(f"File is a directory: {path.is_dir()}")
    print(f"File is a file: {path.is_file()}")
    print(f"File is a symlink: {path.is_symlink()}")
    print(f"File is readable: {os.access(path, os.R_OK)}")
    print(f"File is writable: {os.access(path, os.W_OK)}")
def run (path):
    cl.clear_screen()
    path = Path(path)
    if path.exists():
        print(f"File exists! {path}")
        show_info(path)


    else:
        print(f"File does not exist! {path}")