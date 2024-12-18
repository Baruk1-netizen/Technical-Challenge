def capitalize_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words back into a string
    result = ' '.join(capitalized_words)
    
    return result

# Prompt the user for input
user_input = input("Enter a string: ")

# Call the function and print the result
print("Result string:", capitalize_words(user_input))
