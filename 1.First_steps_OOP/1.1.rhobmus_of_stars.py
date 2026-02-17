def print_lines_up(size):
    for row in range(1, size):
        print(" " * (size - row) + "* " * row)

def print_lines_down(size):
    for row in range(size, 0, -1):
        print(" " * (size - row) + "* " * row)

def print_rhombus(size):
    print_lines_up(size)
    print_lines_down(size)

n = int(input())

print_rhombus(n)