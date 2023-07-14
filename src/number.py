import re


def main():
    numbers = input("Enter 5 numbers of your choice with(,): ").split(",")
    if (len(numbers) < 5 or len(numbers) > 5):
        print("sorry, you entered more or less than 5 numbers")
    else:
        for n in numbers:
            clean_num = re.sub(r"\s+", "", n)
            if (clean_num.isnumeric() is False):
                print("Whoops, one or more string you entered is not number")
                print(f"invalid input: {clean_num}")
                exit(0)
        if (clean_num.isnumeric() is True):
            num = list(map(int, numbers))
            print(num)
            # checks for the minimum number and prints it

            min_number = min(num)
            print(f"\nThe lowest number is {min_number}")

            # checks for the maximum number and prints it
            max_number = max(num) 
            print(f"The largest number is {max_number}")


if __name__ == "__main__":
    main()
