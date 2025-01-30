from pathlib import Path

import pytest


# How many lines test_version_eq_version_info will check before assuming there is no __version__ / __version_info__
# This is a time saving mesure so that you don't have to go through every line of every file.
# If a file has a docstring then it will ignore that and check [VEVI_LINE_AMOUNT] lines after it.
VEVI_LINE_AMOUNT = 20

# Directories where code is that can be checked.
CODE_DIRS = ["tests", "melar"]
# Ignored subdirectories
IGNORED_SUBDIRS = ["__pycache__"]
# Gets parent parent directory (contains melar, tests, etc)
base_dir = Path(__file__).resolve().parent.parent


# Finds all files ending in .py in the folder that are in CODE_DIRs and returns them except IGNORED_SUBDIRS
# as a list of list with each element having the filename and its parent directories-
@pytest.fixture()
def get_code_files_path():
    py_files = []
    for subdir in CODE_DIRS:
        for file in (base_dir / subdir).rglob("*.py"):
            if not any(i in file.parts for i in IGNORED_SUBDIRS):
                py_files.append(file)

    return py_files


def test_version_version_info(get_code_files_path):
    """Checks that all files that have __version__ also has __version_info__ and that they equal each other.

    It also checks that there exists either 1 or 0 of both in the file.
    This only checks the first 20 (VEVI_LINE_AMOUNT) lines of code since __version__ and __version_info__ will be located quite high up.
    If file has a docstring on top it skips that and reads the 20 lines after the docstring.
    """
    py_files = get_code_files_path

    for i in py_files:
        with open(i, "r") as file:

            lines = []

            if file.readline(3) == "\"\"\"":
                try:
                    for line in file:
                        next(file)
                        if line.startswith("\"\"\""):
                            break

                    # now appends the next 20 lines after the docstring to a list.
                    current_line_after_docstring = 0
                    for line in file:
                        if current_line_after_docstring > 19:
                            break
                        current_line_after_docstring += 1
                        lines.append(line)

                except StopIteration:
                    continue

            # There will only be 1 __version__ / __version_info__ so you can just get the first one.
            # If there would be more then it will raise an exeption.
            find_ver = [i for i in lines if "__version__" in i]
            find_ver_info = [i for i in lines if "__version_info__" in i]
            assert len(find_ver) <= 1, f"More than one __version__ in file \n{i}"
            assert len(find_ver_info) <= 1, f"More than one __version_info__ in file \n{i}"
            assert len(find_ver_info) == len(
                find_ver), f"__version__ or __version_info__ exists but __version_info__ or  __version__ does, in \n{i}"

            # Checks that find_ver is not a null array.
            # Since we already checked that __version__ and __version_info__ are equal
            # that means that if find_ver is a null array then find_ver_info is also a null array.

            if find_ver != []:
                # If one or both of them are not null
                if find_ver != [] and find_ver[0] or find_ver_info[0]:
                    # Removes the part that is not the value
                    # If only one of them has

                    find_ver = find_ver[0].split("\"" or "\'")[1]
                    find_ver_info = "(" + find_ver_info[0].split("(")[1]

                    # Convert the string of the __version_info__ tuple to a tuple.
                    find_ver_info = eval(find_ver_info)

                    # Checks if the version is the same as the joined tuple of version info.
                    # If __version_info__ was 1 digit then it will raise a type error
                    # It should always be a tuple of 3 digits.
                    assert find_ver == ".".join(str(digit) for digit in find_ver_info)
