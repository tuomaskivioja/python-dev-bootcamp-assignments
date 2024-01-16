def is_palindrome(s):
    """
    Check if the given string is a palindrome.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the string is equal to its reverse
    left, right = 0, len(cleaned_s) - 1
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
input_string = "A man, a plan, a canal, Panama"
print(f"Is '{input_string}' a palindrome? {is_palindrome(input_string)}")
