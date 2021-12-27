from typing import List


def read_as_string(filename: str) -> str:
    result = ''
    with open(filename) as file:
        while line := file.readline().rstrip():
            result += line
    return result


def read_as_string_list(filename: str) -> List[str]:
    with open(filename) as file:
        return file.readlines()
