# user inputs yes or no to the question
def main():
    user_input = input("Do you like programming? (yes/no): ").lower()

    # if and else statement as per users choice
    if(user_input == "yes"):
        print("Woohoo, 0's and 1's will be happy knowing you like programming :)") 
    elif(user_input == 'no'):
        print("Boooo!, That's lame")
    else:
        print("invalid input, please try again")

if __name__ == "__main__":
    main() 