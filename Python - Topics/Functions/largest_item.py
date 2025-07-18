# Find the largest item from list
# x = [4, 6, 8, 24, 12, 2]
# Expected Output: 24

def largest():
    x = [4, 6, 8, 24, 12, 2]
    for number in range(0, len(x) - 1):
        result = max(x)
        return result

largest_item = largest()
print(f"The largest item from the list is: {largest_item}")

