# Generate a Python list of all the even numbers between 4 to 30
def even():
   even_nums = []
   for i in range(4, 31):
      if i % 2 == 0:
        even_nums.append(i)
        return i 
      
even_nums = even()
print(f"Even numbers from 4 to 30 are: {even_nums}")
