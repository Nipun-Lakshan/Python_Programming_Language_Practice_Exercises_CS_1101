# Introduction to File
'''
File Name           : Bridge Problem - Exercise 03 - Python Version
Registration Number : 2023s20371
Index Number        : s17618
'''

# Modules Imported Through Python Standard Library
import math

# Constants
BRIDGE_KM_COST = 60  # Building Cost of Bridge For 1 Km in LKR Million
ROAD_KM_COST = 40  # Building Cost of Road For 1 Km in LKR Million
WATER_WIDTH = 6  # Width Of The Water
MAX_ROAD_LEN = 8  # Max Length Of The Road


# Header String Printing Function
def print_header():
    print("\n================================")
    print("Building a Bridge - Minimum Cost")
    print("================================\n")


# Bridge Length Finding Function
def getBridgeLen(x):
    return math.sqrt((WATER_WIDTH**2) + (x**2))


# Cost Calculating function
def calculate_cost(x, bLen):
    return (ROAD_KM_COST * (MAX_ROAD_LEN - x)) + (BRIDGE_KM_COST * bLen)


# Printing Final Result Function
def printDetails(x, bLen):
    cost = (ROAD_KM_COST * (MAX_ROAD_LEN - x)) + (BRIDGE_KM_COST * bLen)
    print("X: 0" + str(round(x, 2)) + "0 Km, Bridge: 0" + str(round(bLen, 2)) +
          " Km, Road: 0" + str((MAX_ROAD_LEN - x)) + "0 Km, Cost: " +
          str(round(cost, 2)) + " M")


# Main Function
if __name__ == "__main__":

    # Variables
    minimum_cost = 700
    minimum_cost_index = -1

    # Calling Header String Print Function
    print_header()

    # Run a Loop From X = 0 to X = 8 in 20 Steps
    for i in range(0, 21):

        # Assigning Value For X
        x = ((MAX_ROAD_LEN / 20) * (i))

        # Calling Function to Find the Bridge Length
        bLen = getBridgeLen(x)

        # Calling The Function to Calculate the Cost
        cost = calculate_cost(x, bLen)

        # Finding Minimum Cost
        if (minimum_cost > cost):
            minimum_cost_index = i
            minimum_cost = cost

# Print Minimum Cost
x = ((MAX_ROAD_LEN / 20) * (minimum_cost_index))
bLen = getBridgeLen(x)
cost = printDetails(x, bLen)
