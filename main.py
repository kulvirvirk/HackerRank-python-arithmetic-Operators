# Task
# Read two integers from STDIN and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Input Format
# The first line contains the first integer, . The second line contains the second integer, 

# Constraints
# a and b values are betten or equal to 1 to 10**10

# Print the three lines as explained above.

a = int(input('enter a:'))
b = int(input('enter b:'))
if ((a and b) >= 1) and ((a and b) <=10**10):
   print(a + b)
   print(a-b)
   print(a*b)

else: print('Value should be between 1 to 10**10, re run the program')