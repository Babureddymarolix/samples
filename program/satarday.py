def remove_characters(input_string, characters_to_remove):
    # Create an empty string to store the result
    result = ""

    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is not in the characters_to_remove list
        if char not in characters_to_remove:
            # If not, add it to the result string
            result += char

    return result

# Example usage:
input_string = "Hello, World!"
characters_to_remove = " ,!"  # We want to remove spaces, commas, and exclamation marks

result_string = remove_characters(input_string, characters_to_remove)
print(result_string)  # Output will be "HelloWorld"


