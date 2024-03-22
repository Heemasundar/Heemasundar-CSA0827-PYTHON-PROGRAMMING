def modify_string(S):
    modified_string = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Count the frequency of each character in the string
    frequency = {}
    for char in S:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Modify the string by replacing each character
    for char in S:
        if char.islower():
            # Get the circular distance from 'a' and adjust it based on the character's frequency
            circular_distance = (ord(char) - ord('a') + frequency[char]) % 26
            modified_string += alphabet[circular_distance]
        else:
            # If the character is not a lowercase alphabet, keep it unchanged
            modified_string += char
    
    return modified_string

# Test case
S = "ghee"
print("Modified string:", modify_string(S))
