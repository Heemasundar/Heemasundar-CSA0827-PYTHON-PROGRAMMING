class Solution:
    def isNumber(self, s: str) -> bool:
        # Define states
        states = [
            {},  # Start state
            {'digit': 1, 'dot': 2, 'sign': 3},  # Integer state
            {'digit': 2},  # Decimal state
            {'digit': 1},  # Exponent state
            {'digit': 1}   # End state
        ]
        
        # Define input types
        input_types = {
            'digit': lambda x: x.isdigit(),
            'dot': lambda x: x == '.',
            'sign': lambda x: x == '+' or x == '-'
        }
        
        # Initialize current state
        current_state = 1
        
        # Iterate through the characters of the string
        for char in s:
            # Determine input type
            input_type = None
            for key, func in input_types.items():
                if func(char):
                    input_type = key
                    break
            
            # If input type not found, return False
            if input_type is None:
                return False
            
            # If next state not defined for current input type, return False
            if input_type not in states[current_state]:
                return False
            
            # Update current state
            current_state = states[current_state][input_type]
        
        # Check if the final state is valid
        return current_state in {1, 2, 4}

# Test cases
solutions = Solution()
print(solutions.isNumber("2"))  # True
print(solutions.isNumber("0089"))  # True
print(solutions.isNumber("-0.1"))  # True
print(solutions.isNumber("+3.14"))  # True
print(solutions.isNumber("4."))  # True
print(solutions.isNumber("-.9"))  # True
print(solutions.isNumber("2e10"))  # True
print(solutions.isNumber("-90E3"))  # True
print(solutions.isNumber("3e+7"))  # True
print(solutions.isNumber("+6e-1"))  # True
print(solutions.isNumber("53.5e93"))  # True
print(solutions.isNumber("-123.456e789"))  # True
print(solutions.isNumber("abc"))  # False
print(solutions.isNumber("1a"))  # False
print(solutions.isNumber("1e"))  # False
print(solutions.isNumber("e3"))  # False
print(solutions.isNumber("99e2.5"))  # False
print(solutions.isNumber("--6"))  # False
print(solutions.isNumber("-+3"))  # False
print(solutions.isNumber("95a54e53"))  # False
