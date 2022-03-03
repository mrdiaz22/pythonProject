# Short script of a smart light switch that switches the lights off at daytime and on at nighttime.

# Create a variable that stores if it's daytime or nighttime.
# Create another variable that stores the function of the light switch.

# Let say is nighttime and set the value to 'False' to daytime.
# Let turn on the lights by saying is not daytime.

daytime = False
lights_on = not daytime

# Output a descriptive string followed by the value of the variables created.
print("Daytime?")
print(daytime)

print("Are the lights on?")
print(lights_on)

# Repeat the example but reversed.
nighttime = True
lights_off = not nighttime

print("Nighttime?")
print(nighttime)

print("Are the lights off?")
print(lights_off)
