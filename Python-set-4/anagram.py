# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"



def is_anagram(str1, str2):
    # Remove whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check lengths
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count character occurrences
    char_count = {}

    # Count characters in str1
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrement characters in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  # Character doesn't exist in str1

    # Check if all character counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True

# Example usage:
str1="cinema"
str2="iceman"

if is_anagram(str1, str2):
    print("True")
else:
    print("False")