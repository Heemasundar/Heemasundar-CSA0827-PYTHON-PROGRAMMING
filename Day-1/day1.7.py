def count_sorted_strings(n):
    # Define vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize a memoization table to store results for subproblems
    memo = {}
    
    # Define a recursive function to compute the number of valid strings starting with a particular vowel
    def count_strings_starting_with_vowel(n, vowel):
        # Base case: If n is 1, there is only one valid string
        if n == 1:
            return 1
        
        # Check if the result is already computed
        if (n, vowel) in memo:
            return memo[(n, vowel)]
        
        # Initialize the count for valid strings starting with the current vowel
        count = 0
        
        # For each vowel after the current one, recursively compute the count of valid strings
        # starting with that vowel
        for i in range(vowels.index(vowel), len(vowels)):
            count += count_strings_starting_with_vowel(n - 1, vowels[i])
        
        # Memoize the result
        memo[(n, vowel)] = count
        
        return count
    
    # Initialize the total count
    total_count = 0
    
    # Sum up the counts for all vowels
    for vowel in vowels:
        total_count += count_strings_starting_with_vowel(n, vowel)
    
    return total_count

# Test case
n = 2
print("Number of strings of length", n, "that are lexicographically sorted:", count_sorted_strings(n))
