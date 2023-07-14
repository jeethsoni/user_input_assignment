import re


def main():

    even = []
    odd = []
    numbers = input("Enter 10 numbers of your choice: ").split(",")
    len_num = len(numbers)

    if ((len_num < 10) or (len_num > 10)):
        print("oops, you enetered less or more than 1o numbers, sorry")
    else:
        for n in numbers:
            new_num = re.sub(r"\s+", "", n)
            if (new_num.isnumeric() is False):
                print("Oops, you didn't enter a number")
                print(f"invalid input: {new_num}")
                exit(0)

        if (new_num.isnumeric() is True):
            conver_number = list(map(int, numbers))
            for num in conver_number:
                if (num % 2 == 0):
                    even.append(num)
                    even.sort()
                else:
                    odd.append(num)
                    odd.sort()

            print("")
            print(f"Here are your odd numbers: {odd}")
            print(f"Here are your even numbers: {even}")


if __name__ == "__main__":
    main()
