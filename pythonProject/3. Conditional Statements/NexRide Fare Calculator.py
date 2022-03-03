# Calculating the price of the rides.

# Using 'if', 'elif', 'else' conditionals to calculate a paidride fare depending on the type of the ride chose.
# Use in-app credits for purchases as well.

# Creating variables:

ride_type = "White"
credits = 5

ride_price = ["Standard: 20.52","NexRide: 25.5", "White Car: 40.68"]
Total = 0

print("Choose a ride:")
print(ride_price)

# Create two variables that accept user input.
Input_1 = input("Enter first input:")

# Store the results of the operations in new variables, and display the results.
first_input = int(Input_1)

# if statement to verify what type of ride the user chose:

if ride_type == "NextRide":
    ride_price = 25.5
elif ride_type == "White":
    ride_price = 40.68
else:
    ride_price = 20.52

# Display the ride price depending on the ride type the user chose:

print("Ride price:")
print(ride_price)

# if statement to adjust the fare price depending on credits available to pay:

if credits > 0:
    Total = ride_price - credits

# Display the Total payment for the ride:
    print("Total:")
    print(Total)
