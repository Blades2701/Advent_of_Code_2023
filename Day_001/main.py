import os


def main():
    part1()


def part1():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    content = read_input(current_dir + '/Input.txt')  # need to split the string on \
    lines: list[str] = content.split()
    numbers: list[int] = []
    find_digit(lines, numbers)
    print(sum(numbers))
    # 54597 ! Part 1


def find_digit(lines, numbers):
    for line in lines:
        number: int = 0
        # looking from the front
        for letter in line:
            if letter.isdigit():
                number = int(letter) * 10
                break

        # for loop in reverse
        for letter in reversed(line):
            if letter.isdigit():
                number = int(letter) + number
                break

        numbers.append(number)


def read_input(file_path: str):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


if __name__ == '__main__':
    main()

# Problem phrase prendre premier et dernier chiffre dans phrase - Addition à la fin
