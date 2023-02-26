# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return left + right in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_bracket in enumerate(text):
        if next_bracket in "([{":
            opening_brackets_stack += next_bracket

        if next_bracket in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1], next_bracket):
                return i+1
            opening_brackets_stack = opening_brackets_stack[:-1]

    else: return "Success" if not opening_brackets_stack else i+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
