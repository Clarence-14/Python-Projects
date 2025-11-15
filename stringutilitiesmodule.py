# A custom module with functions to count vowels and check if a string is a palindrome, then use it in a main program.

def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if a string is a palindrome (ignoring case and spaces)."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def reverse_string(text):
    """Return the reversed version of the string."""
    return text[::-1]

def count_consonants(text):
    """Count the number of consonants in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

# --- Interactive part ---
if __name__ == "__main__":
    user_input = input("Enter a string: ")

    # Test count_vowels
    vowels_count = count_vowels(user_input)
    print(f"Number of vowels: {vowels_count}")

    # Test is_palindrome
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    # Test reverse_string
    reversed_text = reverse_string(user_input)
    print(f"Reversed string: {reversed_text}")

    # Test count_consonants
    consonants_count = count_consonants(user_input)
    print(f"Number of consonants: {consonants_count}")
