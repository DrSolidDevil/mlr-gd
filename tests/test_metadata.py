from pathlib import Path

import pytest

# How many lines test_version_eq_version_info, test_init_has_license and more.
# Will check before assuming there is no __version__ / __version_info__ / __license__ / Whateve it's looking for
# This is a time saving mesure so that you don't have to go through every line of every file.
# If a file has a docstring then it will ignore that and check [CHECK_LINE_AMOUNT] lines after it.
CHECK_LINE_AMOUNT = 20

# Directories where code is that can be checked.
CODE_DIRS = ["tests", "melar"]
# Ignored subdirectories
IGNORED_SUBDIRS = ["__pycache__"]
# Gets parent parent directory (contains melar, tests, etc)
base_dir = Path(__file__).resolve().parent.parent

# If all files should have the same version then enter the version here.
# If you don't want to check that all have the same version then have this be an empty string.
ALL_SAME_VERSION = "0.2.0"

# The license of this package
LICENSE = "BSD-3-Clause"

# A list of list with files to ignore the status of, if it has a status present.
# The list is formated: [ ["parentfolder", "filename"], ["parentfolder", "filename"] ]
IGNORED_STATUS = []

# A list of list with files to ignore checking if they have a license
# The list is formated: [ ["parentfolder", "filename"], ["parentfolder", "filename"] ]
IGNORED_LICENSE = [["tests", "__init__.py"]]


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


def parse_lines(f):
    """Checks the first [CHECK_LINE_AMOUNT] of file.

    If docstring is present then it checks first [CHECK_LINE_AMOUNT] of lines after docstring.
    Args:
        f: File to be parsed

    Returns:
        List of lines
    """
    with open(f, "r") as file:
        lines = file.readlines()
        if lines[0].startswith('"""'):

            after_docstring = lines.index('"""\n', 1)
            return lines[after_docstring + 1:after_docstring + 21]
        else:
            return lines[0:20]


def test_version_version_info(get_code_files_path):
    """Checks that all files that have __version__ also has __version_info__ and that they equal each other.

    It also checks that there exists either 1 or 0 of both in the file.
    This only checks the first 20 (CHECK_LINE_AMOUNT) lines of code since __version__ and __version_info__ will be located quite high up.
    If file has a docstring on top it skips that and reads the 20 lines after the docstring.
    """
    py_files = get_code_files_path

    for file in py_files:
        lines = parse_lines(file)

        # There will only be 1 __version__ / __version_info__ so you can just get the first one.
        # If there would be more than 1 it will raise an exception.
        find_ver = [i for i in lines if i.startswith("__version__")]
        find_ver_info = [i for i in lines if i.startswith("__version_info__")]
        assert len(find_ver) < 2, f"More than one __version__ in file"
        assert len(find_ver_info) < 2, f"More than one __version_info__ in file"
        assert len(find_ver_info) == len(
            find_ver), f"__version__ or __version_info__ exists but __version_info__ or  __version__ does"

        # Checks that find_ver is not a null array.
        # Since we already checked that __version__ and __version_info__ are equal
        # that means that if find_ver is empty then find_ver_info is also a empty.
        if find_ver:
            # If one or both of them are not null
            if find_ver[0] and find_ver_info[0]:
                # Removes the part that is not the value
                # If only one of them has
                print(find_ver)
                find_ver = find_ver[0].replace("'", '"').split('"')[1]
                find_ver_info = "(" + find_ver_info[0].split("(")[1]

                # Convert the string of the __version_info__ tuple to a tuple.
                find_ver_info = eval(find_ver_info)

                # Checks if the version is the same as the joined tuple of version info.
                # If __version_info__ was 1 digit then it will raise a type error
                # It should always be a tuple of 3 digits.
                print(find_ver)
                assert find_ver == ".".join(str(digit) for digit in find_ver_info)

                # If all files should have the same version.
                if ALL_SAME_VERSION:
                    assert find_ver == ALL_SAME_VERSION, f"Not all files have the same version ({ALL_SAME_VERSION})"


def test_init_has_license(get_code_files_path):
    """Checks that all __init__.py files has __license__

    Checks the first [CHECK_LINE_AMOUNT] of the document. Or lines after docstring.
    """

    py_files = get_code_files_path

    # Only include files with the name __init__.py
    py_files = [i for i in py_files if i.name == "__init__.py"]
    py_files = [i for i in py_files if [i.parent.name, i.name] not in IGNORED_LICENSE]

    for file in py_files:
        lines = parse_lines(file)
        # This finds lines that starts with __license__
        # It then replaces all single quotes with double quotes (for ease of use)
        # Then splits line with double quotes as the delimiter.
        # It then gets the second index since that one will be between quotes (assuming the quotes get closed)
        find_lic = [i.replace("'", '"').split('"')[1] for i in lines if i.startswith("__license__")]

        assert len(find_lic) != 0, f"No __license__ in file: {file}"
        assert len(find_lic) < 2, f"More than one __license__ in file: {file}"
        assert find_lic[0] == LICENSE, f"License is not correct in file {file}"


@pytest.mark.releasetest
def test_final_status(get_code_files_path):
    """Checks that all files (except those in IGNORED_STATUS) with __status__ is equal to "Production"

    This is for verifying that everything is ready for release.
    """

    py_files = get_code_files_path
    py_files = [i for i in py_files if [i.parent, i.name] not in IGNORED_STATUS]

    for file in py_files:
        lines = parse_lines(file)

        # There will only be 1 __version__ / __version_info__ so you can just get the first one.
        # If there would be more then it will raise an exeption.
        find_status = [i.replace("'", '"').split('"')[1] for i in lines if i.startswith("__status__")]

        if find_status:
            assert len(find_status) < 2, f"More than one __status__ in file: {file}"
            assert find_status[0] == "Production", f"__status__ is not \"Production\" in file: {file}"
