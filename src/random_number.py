"""
A python script that takes range from user and prints random number

@usage python3 random_number.py "1" to "1000"
"""


# importing random module
import random
import sys


def main():
    # asks user for a range for random number
    start_range = input("Enter a starting range: ")
    end_range = input("Enter an ending range: ")

    if int(end_range) < int(start_range):
        sys.exit("End range cannot be less than starting range")

    if (start_range.isdigit() is True and end_range.isdigit() is True):
        start_number = int(start_range)
        end_number = int(end_range)
        # stores random number in the variable as per users choice
        rand_num = random.randrange(start_number, end_number)

        # prints the random number
        print(f"Your lucky random number is: {rand_num}")
    else:
        print("sorry, you didn't enter an integer")


if __name__ == "__main__":
    main()
