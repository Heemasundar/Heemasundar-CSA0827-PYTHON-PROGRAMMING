def calculate_price(fresh_loaves, day_old_loaves):
    # Price of fresh loaf
    fresh_price = 185
    # Discount percentage for day-old loaf
    discount_percent = 60

    # Calculate total price for fresh loaves
    fresh_total_price = fresh_loaves * fresh_price
    # Calculate total price for day-old loaves after discount
    day_old_total_price = day_old_loaves * (fresh_price * (100 - discount_percent) / 100)

    # Calculate discount amount
    discount_amount = fresh_loaves * fresh_price - day_old_total_price

    return fresh_total_price, discount_amount, day_old_total_price

# Get input from the user
fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))

# Calculate prices
fresh_total_price, discount_amount, day_old_total_price = calculate_price(fresh_loaves, day_old_loaves)

# Display the results
print("Regular price for fresh bread: {:.2f} rupees".format(fresh_total_price))
print("Discount because it's day-old: {:.2f} rupees".format(discount_amount))
print("Total price: {:.2f} rupees".format(day_old_total_price))
