#main method
def main():
    #stores user's name in the variable 
    name = (input("What is your name? "))
    new_name = name.replace(" ", "")
    # validates if user inputted strings as name or something else
    if((new_name.isalpha() == False) or (new_name.isnumeric() == True)):
        print("Sorry, the name cannot have any numbers present, Try again")
    else:
        print("Howdy!, " + name + ", Welcome to the Python World")


if __name__ == "__main__":
    main()