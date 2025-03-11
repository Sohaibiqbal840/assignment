
# Accept temperature input from the user
temperature = float(input("Enter temperature in centigrade: "))

# Check the temperature range and display the message
if temperature < 0:
    print("FREEZING")
elif 0 <= temperature <= 15:
    print("COLD")
elif 16 <= temperature <= 30:
    print("WARM")
elif 31 <= temperature <= 40:
    print("HOT")
else:
    print("VERY HOT")
