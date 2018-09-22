#
# Name: William Cuttrell
# mean.py
#
# Purpose: The program will calculate the average, rms average, and standard deviation
# of a set of numbers provided by the user.
#
# Certificate of authenticity:
# I certify that this lab is entirely my own work.
#
# Input: 1)The number of values in a set, 2)Actual values of the set
# Output: The average, rms average, and standard deviation for the set

#Define the program 'mean'
def mean():

#Import math function
    import math

    #Print a description of the function
    print("This program will calculate the average, rms average, and standard")
    print("deviation of a set numbers")
    print("")


    #Prompt the user to input the number of values in the set
    n = eval(input("Enter the number of values in the set:"))

    #Use for loop to create a list 'X'
    X=[]
    #Repeat the loop for every value in the set
    for i in range(n):
        #Prompt user for each value in the set, to substitute 'xi'
        xi=eval(input("Enter a value: "))
        #Store the values in list 'X'
        X.append(xi)


    #Use for loop to find the sum of all values in 'X'
    total=0
    for i in X:
        total = total+i

    #Divde the sum by the number of values to get the mean
    avg = total/n

    #Print the mean
    print("The average for this set is: ",round(avg,3))


    #Use a similar for loop to find the sum of all values squared in 'X'
    total=0
    for i in X:
        total = total+i**2

    #Plug this value into the formula for rms average
    rmsAvg = math.sqrt(total/n)

    #Print the rms average
    print("The rms average for this set is: ",round(rmsAvg,3))


    #Using a for loop, find the sum of all values subtracted from the mean, squared
    rsum=0
    for i in X:
        rsum = rsum + (avg-i)**2

    #Plug in the sum into the formula for standard deviation
    sd = math.sqrt(rsum/(n-1))

    #Print the standard deviation
    print("The standard deviation for this set is: ",round(sd,3))








#define main function as mean
def main():

    mean()

#execute
main()