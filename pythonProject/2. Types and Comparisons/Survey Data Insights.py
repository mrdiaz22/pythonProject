# Short program that labels data acquire through a fitness app's user survey.
# Using string comparisons, check the user's survey answers regarding activity frequency and intensity, label them, and display te results.

# The user does sports every day.
frequency = "daily"
intensity = "high"

# Create a variable that stores the result of the comparison between frequency and intensity, and display the result.
highly_active = frequency == "daily"
print("Highly active user:")
print(highly_active)

# Label the user as doing high-intensity sports.
high_intensity = intensity == "high"
print("High intensity sports:")
print(high_intensity)