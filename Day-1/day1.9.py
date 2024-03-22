def max_guests_within_T_hours(entries, exits, T):
    max_guests = 0
    current_guests = 0
    for i in range(T):
        current_guests += entries[i]  # Guest entering
        current_guests -= exits[i]    # Guest leaving
        max_guests = max(max_guests, current_guests)
    return max_guests

# Test case
entries = [10, 5, 15, 20]  # Number of guests entering at each hour
exits = [5, 10, 5, 3]      # Number of guests leaving at each hour
T = 4                      # Total number of hours
print("Maximum number of guests present within", T, "hours:", max_guests_within_T_hours(entries, exits, T))
