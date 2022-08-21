my_str = "Hello this Is an Example With cased letters"

# To take input from user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the words

print("The sorted words are")
for word in words:
    print(word)