# Demonstrate short-circuiting with logical operators.

for i in range(1,30):
    if i % 2 != 0: 
        print(i, end = " ")
        continue
      
