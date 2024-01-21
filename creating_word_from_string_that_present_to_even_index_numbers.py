# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user 
# Display characters that are present at an even index number.


def display_even_index_characters(input_str):
    even_index_characters = [input_str[i] for i in range(0, len(input_str), 2)]
    return even_index_characters

user_input = input("Enter the word: ")

result = display_even_index_characters(user_input)
print("Characters at even index numbers:", ', '.join(result))
