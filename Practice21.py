# CS 1101 - Week 09 - Exercise 03
temperature = [0, 100, 37]
print("")
for i in range(0, 3):
    print(f"Temperature in Celsius : {temperature[i]}")
    fahrenheit = (((temperature[i] * 9) / 5) + 32)
    print(f"{temperature[i]} {chr(176)}C = {fahrenheit} {chr(176)}F")
