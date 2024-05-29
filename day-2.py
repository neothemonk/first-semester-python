"""
Pentagonal Number
Write a function that takes a positive integer num and
calculates how many dots exist in a pentagonal shape
around the center dot on the Nth iteration.

In the image below, you can see the first iteration is
only a single dot. On the second, there are 6 dots.
On the third, there are 16 dots, and on the fourth
there are 31 dots.

https://edabit-challenges.s3.amazonaws.com/pentagonal_number.png

Return the number of dots that exist in the whole pentagon on the Nth iteration.
"""


def main(num):
    print(pentagonal_number(num))


def pentagonal_number(num):
    """Takes a positive integer num and returns how many dots can surround
     that dot in that "num" th iteration"""
    if num == 1:
        # This is the base case in which it just returns 1 because only 1 dot can surround 1 dot in 1st iteration.
        return num
    # else, it just returns the sum of the function one num behind and num times 5 minus 5. it is because every more
    # iteration the surrounding dots are 5 more than the previous iteration.
    return pentagonal_number(num - 1) + (num * 5 - 5)
    # if num == 2:
    #     return pentagonal_number(num-1)+(num*5-5)
    # elif num == 3:
    #     return pentagonal_number(num-1)+(num*5-5)
    # elif num == 4:
    #     return pentagonal_number(num-1)+(num*5-5)
    # elif num == 5:
    #     return pentagonal_number(num-1)+(num*5-5)


if __name__ == '__main__':
    main(2)
