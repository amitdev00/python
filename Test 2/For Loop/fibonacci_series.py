# Write a program to print Fibonacci series

number_of_times = 20
first, second = 0, 1


for i in range( number_of_times):
    first, second = second, first + second
    print(first, end = " ")