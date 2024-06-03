"""
Write a function that returns True if two arrays, when combined,
form a consecutive sequence. A consecutive sequence is a sequence
without any gaps in the integers, e.g., 1, 2, 3, 4, 5 is a
consecutive sequence, but 1, 2, 4, 5 is not.
Examples:
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
consecutive_combo([44, 46], [45]) ➞ True
Notes:
The input lists will have unique values.
The input lists can be in any order.
"""


def consecutive_combo(list1: list, list2: list) -> bool:
    """This function takes two lists and returns true if those two lists form a consecutive
    sequence of numbers when combined into one list, otherwise false."""
    # first thing, I combined the two lists into one and sorted it so that the
    # numbers in the list - if appear to be
    # consecutive sequence of numbers - would be in a sorted order.
    combined_list = sorted(list1 + list2)
    # then, to check if indeed the numbers in the list are a consecutive sequence of numbers,
    # I used a for loop.
    for i in range(len(combined_list) - 1):
        # if there is an instance of a situation where to the current item 1 is added does not
        # equal to the next item in the list is found, it returns false.
        if combined_list[i] + 1 != combined_list[i + 1]:
            return False
    # otherwise, if such an instance is not found, it returns True.
    return True


def main() -> None:
    print(consecutive_combo([44, 46], [45]))


if __name__ == '__main__':
    main()
