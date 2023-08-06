def is_palindrome(string):
    # Remove any spaces and convert the string to lowercase
    string = string.replace(" ", "").lower()
    # Compare the string with its reverse
    return string == string[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")




def remove_character(input_string, character_to_remove):
    result_string = ""
    for char in input_string:
        if char != character_to_remove:
            result_string += char
    return result_string

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    char_to_remove = input("Enter the character you want to remove: ")

    modified_string = remove_character(user_input, char_to_remove)
    print("Original string:", user_input)
    print("Modified string:", modified_string)



def is_vowel_or_consonant(char):
    vowels = "aeiouAEIOU"

    if len(char) != 1:
        return "Invalid input. Please enter a single character."

    if char.isalpha():
        if char in vowels:
            return f"{char} is a vowel."
        else:
            return f"{char} is a consonant."
    else:
        return "Invalid input. Please enter an alphabet character."

if __name__ == "__main__":
    user_input = input("Enter a character: ")
    result = is_vowel_or_consonant(user_input)
    print(result)



    def count_characters(input_string):
      alphabets = 0
      digits = 0
      specials = 0

    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            specials += 1

    return alphabets, digits, specials

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    alphabets_count, digits_count, specials_count = count_characters(user_input)

    print("Number of alphabets:", alphabets_count)
    print("Number of digits:", digits_count)
    print("Number of special characters:", specials_count)


def remove_spaces(input_string):
    return input_string.replace(" ", "")

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    modified_string = remove_spaces(user_input)
    print("Original string:", user_input)
    print("Modified string:", modified_string)


    





