# Write Python code to iterate through the first 10 numbers 
# and, in each iteration, print the sum of the current and previous number.

previous_num = 0
for i in range(1,11):
    sum = previous_num + i
    print(f"Previous Number is: {previous_num}, Current Number is: {i}, Sum is: {sum}")
    previous_num = i