#
# Name: William Cuttrell
# mortgage.py
#
# Purpose: To calculate the amounts of a loan to be payed across several intervals given the initial loan,
# the number of months to pay, and the interest rate.
#
# Certificate of authenticity:
# I certify that this lab is entirely my own work.
#
# Input: Interest, time to pay in months, principle (initial) loan amount
# Output: Monthly payment, total payment, total interest paid


#define the program
def main():

# print the purpose of the program
    print("This program calculates your monthly loan payment, total payment,")
    print("and total interest paid for that loan.")
    print("")

# input the three variables needed to be defined in order to calculate our amounts
    principle = eval(input("Enter the initial loan amount in dollars (exclude $ sign): "))
    months = eval(input("Enter the number of months to pay: "))
    interest = eval(input("Enter the percent interest (example: '6%' as '6'): "))

# carry out the calculation by first defining the rate
    rate = interest/1200

# calculate the amount payed by the month
    monthly = (principle*rate*((1+rate)**months))/((1+rate)**months-1)
# calculate the total cost of the loan
    total = (principle*rate*months)/(1-(1+rate)**(0-months))
# subtract the intial amount from the total amount to find the interest paid
    netInterest = total- principle

# present each result accordingly
    print("")
    print("Your monthly payment for this loan is: $",monthly)
    print("Your lifetime payment for this loan is: $",total)
    print("The net amount of interest paid for this loan is $",netInterest)
    print("")

# execute program
main()

