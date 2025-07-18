# Write a function that:
# Takes 3 words (strings) as input from the user.
# Stores them in a list, converts to a tuple, and prints the tuple.
# Prints the total number of words.
# Checks if any word starts with a capital letter.
# Takes a Unicode number as input and prints:
# The character it represents (chr()),
# Functions to use: input(), list(), tuple(), len(), any(), chr(), ascii(), int(), print()

def input_check():
    words = []
    for i in range(3):
        word = str(input(f"Enter the word: {i +1}"))
        words.append(word)

    words_tuple = tuple(words)

    total_words = len(words_tuple)
    print(f"The total words in the tuple is: {total_words}")

    capital_letter_words = any(word[0].isupper() for word in words_tuple)
    print(f"Any word which starts with capital letter is: {capital_letter_words}")

    unicode_number = int(input("Enter a unicode number value: "))
    print(f"Unicode character of value {unicode_number} is: {chr(unicode_number)}")


    return words

y = input_check()
print(y) 