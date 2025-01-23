# CS 1101 - Week 09 - Exercise 11


# Converter Function
def getF(celsius):
    return ((celsius * 9) / 5) + 32


# Main Function
if __name__ == "__main__":
    celsius = float(input("\nEnter Temperature in Celsius : "))
    fahrenheit = getF(celsius)
    print(f"{celsius}{chr(176)}C = {fahrenheit}{chr(176)}F")
