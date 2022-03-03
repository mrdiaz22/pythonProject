# Short code that verifies outliers in data.

# Creating a variable and setting it 'True' or 'False, by verifying if a number is an outlier in the dataset.

# Create variables to decide the outliers with a minimum and maximum limit.
minimum_limit = 45
maximum_limit = 90

# Boolean will keep track of whether the outlier is in or out of range.
outlier = True
number = 25

# if statement that verifies if the quantity is greater than maximum limit:
if number >= maximum_limit:
    outlier = True

# if statement that verifies if the outlier is lower than the minimum limit:
if number < minimum_limit:
    outlier = True

# if statement that verifies if outlier is True:
if outlier == True:
    print(f"{number} is an outlier.")

# Boolean will keep track of whether the outlier is in or out of range.
outlier = False
number = 50

# if statement that verifies if the quantity is greater than maximum limit:
if number >= maximum_limit:
    outlier = False

# if statement that verifies if the outlier is lower than the minimum limit:
if number < minimum_limit:
    outlier = False

# if statement that verifies if the number is not an outlier:
if not number:
    outlier = False

# if statement that verifies if outlier is True or False:
if outlier == True:
    print(f"{number} is an outlier.")

if outlier == False:
    print(f"{number} is not an outlier.")

