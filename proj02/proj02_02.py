# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
count_of_numbers = raw_input("How many Fibonacci numbers do you want to generate? ")
num = 0
count1 = 0
count2 = 1
count3 = count1 + count2
while num < int(count_of_numbers):
    print count1 + count2
    count3 = count1 + count2
    count2 = count1
    count1 = count3
    num = num + 1
