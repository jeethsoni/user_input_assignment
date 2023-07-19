"""
A python script that takes 5 numbers from user and print largest and lowest.

@usage python3 number.py "1,2,3,4,5"
"""
import re
import sys


def main():

    # takes 5 numbers input from the user
    numbers = input("Enter 5 numbers of your choice with(,): ").split(",")

    # if and else statement
    if len(numbers) == 5:
        for n in numbers:
            clean_num = re.sub(r"\s+", "", n)  # removes white space that user enter # noqa: E501
            if clean_num.isnumeric() is False:
                print("Whoops, one or more string you entered is not number")
                sys.exit(f"invalid input: {clean_num}")

        num = list(map(int, numbers))  # converts string to integer
        # checks for the minimum number and prints it
        min_number = min(num)
        print(f"\nThe lowest number is {min_number}")

        # checks for the maximum number and prints it
        max_number = max(num)
        print(f"The largest number is {max_number}")

    else:
        print("sorry, you entered more or less than 5 numbers")


if __name__ == "__main__":
    main()
