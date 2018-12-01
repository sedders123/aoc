import sys
import os
import runpy
from typing import Optional

task_map = {"1": "one", "2": "two", "3": "three"}


def get_root_dir(year: str, day: Optional[str]) -> str:
    root_dir = os.path.abspath(os.path.dirname(__file__))
    if day:
        if len(day) == 1:
            day = "0" + day
        root_dir = os.path.join(root_dir, year, day)
    else:
        root_dir = os.path.join(root_dir, year)

    return root_dir


def task_matches_file_name(task: str, file_name: str) -> bool:
    if file_name.startswith(task):
        return True
    if (task in task_map) and file_name.startswith(task_map[task]):
        return True
    return False


def run(year: str, day: Optional[str] = None, task: Optional[str] = None) -> None:
    root_dir = get_root_dir(year, day)
    for dir_name, subdirs, files in os.walk(root_dir):
        for file_name in files:
            if task and not task_matches_file_name(task, file_name):
                continue
            if file_name.startswith("test_") or not file_name.endswith(".py"):
                continue
            os.chdir(dir_name)
            exec(open(f"{dir_name}/{file_name}").read())


if __name__ == "__main__":
    arg = sys.argv[1]
    if len(arg) == 4:
        run(arg)
    else:
        parts = arg.split("-")
        if len(parts) == 2:
            year = parts[0]
            day = parts[1]
            run(year, day)
        if len(parts) == 3:
            year = parts[0]
            day = parts[1]
            task = parts[2]
            run(year, day, task)
