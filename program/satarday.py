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




