
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def convert_to_2d_array(s):
    return [list(map(str, line.split())) for line in s.splitlines()]

s = read_file('tests/unit_tests/data/' + 'case0_input.txt')
print(convert_to_2d_array(s))