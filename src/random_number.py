#importing random module
import random

def main():
    #asks user for a range for random number
    start_range = input("Enter a starting range: ")
    end_range = input("Enter an ending range: ")
    
    if((start_range.isdigit() == True) and (end_range.isdigit() == True)):
        start_number = int(start_range)
        end_number = int(end_range)
        #stores random number in the variable as per users choice
        rand_num = random.randrange(start_number, end_number)

        #prints the random number 
        print(rand_num)
    else:
        print("sorry, you didn't enter an integer")

if __name__ == "__main__":
    main()