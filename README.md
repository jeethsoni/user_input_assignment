# User Input Assignment
*Author: Jeet Soni*

*Date: 07/13/2023*

---
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

### **1) Write a python script to ask a user their name and display the name with a welcome message. You must validate input values.**



A simple program that prints a welcome message with your name! Well, you might think, for first python script this should be easy. Right? Well no, I went deeper to ensure that my very first program runs smoothy and makes sense to the world :)

Questions like What if someone uses something other than alphabets for their string? 

Well, that won't be a problem. I used python in-built functions isaplha() and isnumeric() to ensure that user only enter aphabets for their names. If user decides to enter their full name then the program will join the 2 strings , check for the alphabets and then proceed. 

### **2) Write a python script to ask the user a question if they like programming. Depending on the answer, print a creative message.**

Me peronally, I love programming. This question for people who will use my program. This is a simple yes or no. No hard feeling if you say no lol.

#### Steps

* First, I used an input function to ask question and stored it in a variable.
* I used lower() function to make their answers lowecase 
* I used if-elif-else statements to to print depending on their answer. 

Btw, I ran the program myself and guess what my answer was :)

### **3) Write a python script to ask the user to enter 5 numbers. Print the lowest and largest numbers entered by the user.**

A little math program that compares 5 numbers provided by the user and gives them lowest and the largest number. 

I asked user for input for 5 numbers but I ran into a little problem how to get user to input all 5 numbers in same line. It took me a while then I came across split() function and how to implement it. I love how it works. 

I wanted to make this solid so if user enters less or more than 5 numbers the program won't work. I used the for loop to check every item in the list and then 

I also used regular expression from re module to strip any whitespace so the numbers are organized and it doesn't throw any errors. I then used map() function to convert the numbers from string to integer. Then it will print the lowest and largest number.

### **4) Write a python script to ask the user to enter 10 numbers. Print and output with even and odd numbers in separate lists.

Wanna know your odds and evens? Well, you have come to the right place. I made a little math project that takes 10 numbers and print out odd and even list. 

After I get the 10 numbers from user. I checked if there are exatly just 10 numbers nothing else. I used a for loop to loop throug each item in the list and also fix the white spaces so the program is organzied. I used basic algorithm if the number is divisible by 2 to check for odd or even. If it's divisible by 2 and remainder is 0 then it's even otherwise it's odd. I added these numbers in the odd and even list as it iterates through each item in the list. I also used sort() function to sort the list. Then viola, it prints the list on your screen. 


### **5) Write a python script to ask the user for a range. Print a random number in the range specified by the user.**

A very simple random number program that print random numbers as per user's starting and ending range. It will print the random number in that range. Cool right?

I used input() function for user to provide start and end range. Then I checked if the user is entering digits using isdigit() function. If the value returns true then proceed else do the opposite. Finally, it will print the rnadom number if everything checks out.

Open for any suggestion

Enjoy :)

Jeet Soni


