# loop
# three types - while, do while, for
# three things are improtant in loops - 1. initialization, 2. condition, 3. incrementation
# intialization - from where to start
# condtion - 
# incrementation - 


prime_numbers = [2, 3, 5, 7]

# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)
# Output: bytearray(b'\x02\x03\x05\x07')

# callable function
x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))