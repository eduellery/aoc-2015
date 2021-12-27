def read_as_string(filename: str) -> str:
    result = ''
    with open(filename) as file:
        while line := file.readline().rstrip():
            result += line
    return result
