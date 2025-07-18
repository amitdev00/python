
# def addfunc(list1):
#     add = 0
#     for i in list1:
#         add = add + i    
#     return add
           
# def averagefunc(list1):
#     average = addfunc(list1) / len(list1)
#     return average

# def max_val(list1):
#     count = 0
#     index = len
#     for i in list1:
#         if i > 
        

# def min_val(list1):
#     min_value = min(list1)
#     return min_value


# list1 = [1, 2, 3, 4, 5]

# result = addfunc(list1)
# print("Result:-", result)

# average = averagefunc(list1)
# print("Average:-", average)

# maximum_value = max_val(list1)
# print(f"Maximum Value:- {maximum_value}")

# minimum_value = min_val(list1)
# print(f"Minimum Value:- {minimum_value}")


def min(list_a):
    first = list_a[0]
    for item in list_a[1:]:
        if item < first:
            first = item
    return first

list_a = [5645, 654, 23 , 787, 56]
result = min(list_a)
print("Minimum Value:- ",result)


# def find_min_value(numbers):
#     min_value = numbers  # Assume the first element is the smallest
#     for number in numbers[1:]:  # Iterate through the rest of the elements
#         if number < min_value:  # Compare each number with the current minimum
#             min_value = number  # Update the minimum if a smaller number is found
#     return min_value

