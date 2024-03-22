def is_palindrome(x):
    # Convert integer to string
    x_str = str(x)
    # Compare string with its reverse
    return x_str == x_str[::-1]

# Test case
x = 121
print("Input:", x)
print("Is palindrome?", is_palindrome(x))
