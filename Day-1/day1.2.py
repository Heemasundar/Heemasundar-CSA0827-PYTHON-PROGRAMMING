def sumsquare(l):
    odd_sum = 0
    even_sum = 0
    for num in l:
        if num % 2 == 0:
            even_sum += num ** 2
        else:
            odd_sum += num ** 2
    return [odd_sum, even_sum]

# Getting input from the user
num_elements = int(input("Enter the number of elements: "))
input_list = []
for i in range(num_elements):
    element = int(input("Enter the element: "))
    input_list.append(element)

# Calling the function with the input list
result = sumsquare(input_list)
print("Sum of squares of odd numbers:", result[0])
print("Sum of squares of even numbers:", result[1])
