"""
Google Code Jam Problem 2
Author: Sander Shi
Date: 04/06/2019
"""


def flip(path):
    """
    This function takes a path of 'S' and 'E' and outputs
    the symmetric path.
    """
    new_path = "".join(["E" if i == "S" else "S" for i in path])
    return new_path


def main():
    # The number of test cases
    T = int(input())

    # Calculate for each test case
    for i in range(T):
        n = int(input())
        path = input()
        alternative_path = flip(path)
        print("Case #{}: {}".format(i + 1, alternative_path))


if __name__ == "__main__":
    main()
