def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate the area between the two lines
        area = min(height[left], height[right]) * (right - left)
        # Update max_area if the calculated area is greater
        max_area = max(max_area, area)
        
        # Move the pointer with the smaller height inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test case
array = [1, 5, 4, 3]
print("Input:", array)
print("Maximum area of water that can be contained:", max_area(array))
