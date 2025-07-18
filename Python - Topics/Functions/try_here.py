# just created a function
# def my_func(x):
#     return 5 * x
# result = my_func(67)

# print(result)

# function which has declared but does not have any logic
# def my_func():
    # pass

# def even_num(i = 0):
#     for i in range(1,11):
#         if i % 2 == 0:
#             print(i, end = " ")
# even_num()

# def odd_even(i = 0):
#     for i in range (1, 11):
#         if i % 2 != 0:
#                print(i, end = " ")
# even_num()          
# odd_even()

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# multiply(2,3,4,5)
def save_user(**user):
    
    return(user)

info = save_user(id = 664, name = "amit kumar", course = "python ai", age = "21")


