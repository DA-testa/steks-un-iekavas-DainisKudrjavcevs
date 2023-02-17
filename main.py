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
    input_type = input()
    text = input()
    mismatch = find_mismatch(text)

    if(mismatch) != None:
        print(mismatch)
    else:
        print("Success")


if __name__ == "__main__":
    main()
