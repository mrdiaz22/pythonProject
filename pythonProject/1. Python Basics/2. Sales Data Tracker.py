# Short script that tracks sales data for a jeans' retailer online shop.

# For this project we will compare 'jeans_sold' with 'sales_target' to see if the retailer hit their sales target.
# Then we will verify if there is jeans in stock.

# Create descriptive variables to store the values.
stock = 800
jeans_sold = 650
sales_target = 600

# Create a variable 'target_achieved' to store the comparison results, and use '<=' or '==' to verify if 'jeans_sold' has the same or higher value as 'sales_target'.
target_achieved = sales_target <= jeans_sold

# Print a descriptive string and the variables output.
print("Jeans sales target achievement:")
print(target_achieved)

# Create a variable to store the tracking of the remaining jeans in stock.
# Substract 'jeans_sold' from 'stock' and store the value in the new variable.
on_stock = stock - jeans_sold

# To be able to verify the jeans on stock anytime, create a variable to store a comparison.
# Make a comparison to see if there are jeans on stock, store the comparison into the created variable.
# Use '!=' to make sure the jeans on stock are not equal to 0.
available_stock = on_stock != 0

# To finish, print a descriptive string followed by the value of the stock available.
print("Jeans on stock:")
print(available_stock)


