"""
Filename: average_calculator.py
Author: <Givens,CJ>
Created: <DATE>
Instructor: Holtslander
"""

Numbers = []
while True:
    op = input("Please select your desired operation by typing the number, then pressing \"enter\"\n"
               "1) Add a Number to the list\n")
               "2) Remove a number from the list.\n")
               "3) Compute the average value of the list.\n")
               "4) Print the list\n")
               "5) Exit the program. !WARNING! all data will be erased!\n")

    if op == "1":
        num = input ("Please put in a number")
        Numbers.append (num)
    elif op == "2":
        num = input ("Please put in a number")
        Numbers.remove(num)
    elif op == "3"
        
    
    elif op == "5":
        break
    else: 
        print(f"{op} is not a supported operation! Try again.")
print("Thank you for using this average calculator!")


