"""
Google Code Jam Problem 1
Author: Sander Shi
Date: 04/06/2019
"""


def get_nums(n):
    """
    This function takes a number n and returns two numbers
    a and b that add up to n such that a and b do not contain
    the digit 4 in them.
    """
    string_num = str(n)
    a = ""
    b = ""
    for i in string_num:
        digit = int(i)
        if digit != 4:
            a += i
            b += "0"
        else:
            a += "1"
            b += "3"
    return (int(a), int(b))


def main():
    # The number of test cases
    T = int(input())

    # Calculate for each test case
    for i in range(T):
        n = int(input())
        (a, b) = get_nums(n)
        print("Case #{}: {} {}".format(i + 1, a, b))


if __name__ == "__main__":
    main()
