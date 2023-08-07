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



def sum_of_integers_in_string(input_string):
    numbers = []
    current_number = ""
    for char in input_string:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ""
    if current_number:
        numbers.append(int(current_number))

    return sum(numbers)

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    total_sum = sum_of_integers_in_string(user_input)
    print("Sum of integers in the string:", total_sum)



def remove_repeated_characters(input_string):
    result_string = ""
    for char in input_string:
        if char not in result_string:
            result_string += char
    return result_string

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    modified_string = remove_repeated_characters(user_input)
    print("Original string:", user_input)
    print("Modified string:", modified_string)




def count_occurrences(input_string, character_to_count):
    count = 0
    for char in input_string:
        if char == character_to_count:
            count += 1
    return count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    char_to_count = input("Enter the character to count: ")

    occurrences = count_occurrences(user_input, char_to_count)
    print(f"The character '{char_to_count}' appears {occurrences} times in the string.")




def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    user_input1 = input("Enter the first string: ")
    user_input2 = input("Enter the second string: ")

    if are_anagrams(user_input1, user_input2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")





def custom_sort(input_string):
    alphabets = []
    numerics = []

    for char in input_string:
        if char.isalpha():
            alphabets.append(char)
        elif char.isdigit():
            numerics.append(char)

    sorted_string = ''.join(sorted(alphabets) + sorted(numerics))
    return sorted_string

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    sorted_string = custom_sort(user_input)
    print("Sorted string:", sorted_string)









    





