"""
This challenge is based on the classic video game "Snake".
Assume the game screen is an n * n square, and the snake starts
the game with length 1 (i.e., just the head) positioned in the
top left corner.
For example, if n = 7 the game looks something like this:
https://edabit-challenges.s3.amazonaws.com/glbiwtu.png
In this version of the game, the length of the snake doubles
each time it eats food (e.g., if the length is 4, after eating it becomes 8).
Create a function that takes the side n of the game screen and returns
the number of times the snake can eat before it runs out of space on the game screen.
Examples:
snakefill(3) ➞ 3
snakefill(6) ➞ 5
snakefill(24) ➞ 9
Notes:
The given number will always be a positive integer (there are no exceptions to handle).
"""


def snakefill(n: int) -> int:
    """
    the function returns how many times a snake can eat (each time it eats he doubles in length) until its size
    exceeds the number of total cells.
    :param n: (positive int) the length of one side of the game screen.
    :return: how many times can snake eat until its length exceeds the number of total cells in the game screen.
    """
    # since the game screen is a square, the number of total cells in the game screen is
    # just n times n.
    total_cells = n * n
    # the num_of_iter is just how many times the snake ate until became too long.
    num_of_iter = 0
    # the starting length of the snake is by default 1.
    snake_length = 1
    # the loop only executes if the resulting length of the snake is less than the total cells.
    while (snake_length * 2) < total_cells:
        # each time the snake eats, it doubles in length.
        snake_length *= 2
        # at the end, we also keep track of how many times the snake eats.
        num_of_iter += 1
    return num_of_iter


def main(n):
    print(snakefill(n))


if __name__ == '__main__':
    main(3)
