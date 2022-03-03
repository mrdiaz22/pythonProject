# A short program that analyzes a patient's heart rate.
# Using comparisons to check if the hart rate is too low or too high to alarm the patient about their health.

# Create a variable that stores the heart rate from the heart rate sensor.
heart_rate = 77

# Create variables that tell us if the heart rate is too high or too low.
# Using less than "<", and/or higher than ">".
too_low = heart_rate < 60
too_high = heart_rate > 100

# Display if the heart rate of the patient is low.
print("Heart rate low:")
print(too_low)

# Display if the heart rate of the patient is high.
print("Heart rate high:")
print(too_high)


