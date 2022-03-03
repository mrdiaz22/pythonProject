# Short script that verifies if there are data points on a certain dataset.

# Creating variables that store the minimum points needed and current data points balance.
points_minimum = 50
data_points = 35

# if statement to verify if we reach the minimum number of data points or not.
if data_points >= points_minimum:
    print("We have enough points!")
if data_points < points_minimum:
    print("Collect more data!")

points_minimum = 50
data_points = 200

if data_points >= points_minimum:
    print("We have enough points!")
if data_points < points_minimum:
    print("Collect more data!")
