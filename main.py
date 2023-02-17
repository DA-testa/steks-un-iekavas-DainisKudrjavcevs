# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            last_opening_bracket = opening_brackets_stack.pop()
            if not are_matching(last_opening_bracket.char, next):
                return i + 1
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position + 1
    return "Success"

def main():
    input_type = input("Choose input type (F for file, I for input): ")
    if input_type == "F":
        filename = input("Enter filename: ")
        with open(filename, "r") as file:
            text = file.read().strip()
    elif input_type == "I":
        text = input("Enter brackets: ").strip()
    else:
        print("Invalid input type")
        return
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
