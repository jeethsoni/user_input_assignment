"""
A python script to check user's feelings for programming.

@usage python3 programming_check.py "yes" or "no"
"""


def main():
    # user inputs yes or no to the question
    user_input = input("Do you like programming? (yes/no): ").lower()

    # if and else statement as per users choice
    if (user_input == "yes"):
        print("Woohoo, 0's and 1's will be happy knowing you like programming")
    elif (user_input == "no"):
        print("Boooo!, It's okay programming is not for everyone.")
    else:
        print("invalid input, please try again")


if __name__ == "__main__":
    main()
