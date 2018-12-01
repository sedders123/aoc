import os

root_dir = os.path.abspath(os.path.dirname(__file__))

for dir_name, subdirs, files in os.walk(root_dir):
    for subDir in subdirs:
        if subDir.startswith("."):
            subdirs.remove(subDir)
    # Not sure why mypy is special case
    if ".mypy_cache" in subdirs:
        subdirs.remove(".mypy_cache")
    for file_name in files:
        if not file_name.startswith("test_"):
            continue
        os.chdir(dir_name)
        os.system(f"nosetests {dir_name}/{file_name}")
