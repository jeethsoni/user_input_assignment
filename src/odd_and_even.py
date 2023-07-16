"""
A python script that takes 10 numbers from user and print odd and even list

@usage python3 odd_and_even.py "1,2,3,4,5,6,7,8,9,10"
"""
import re


def main():

    # empty odd and even list
    even = []
    odd = []

    # input function for user to enter 10 numbers
    numbers = input("Enter 10 numbers of your choice: ").split(",")
    len_num = len(numbers)

    # if and else statement
    if (len_num == 10):
        for n in numbers:
            new_num = re.sub(r"\s+", "", n)  # removes whitespace from the list

            # if user enters anything other than numbers exit the program
            if (new_num.isnumeric() is False):
                print("Oops, you didn't enter a number")
                print(f"invalid input: {new_num}")
                exit(0)

        conver_number = list(map(int, numbers))  # converts 10 string to integer # noqa: E501
        # algorithm to check for even number
        for num in conver_number:
            if (num % 2 == 0):
                even.append(num)
            else:
                odd.append(num)

        # sorts the list and print the results
        even.sort()
        odd.sort()
        print("")
        print(f"Here are your odd numbers: {odd}")
        print(f"Here are your even numbers: {even}")
    else:
        print("oops, you enetered less or more than 1o numbers, sorry")


if __name__ == "__main__":
    main()
