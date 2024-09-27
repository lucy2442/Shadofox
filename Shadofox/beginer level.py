# Task 1: Create a variable pi and store the value 22/7 in it.
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))


for_value = 4
print("Value of for_value:", for_value)


P = 10000  # Principal amount in currency
R = 5  # Rate of interest (percentage)
T = 3  # Time period in years


simple_interest = (P * R * T) / 100
print("Simple Interest for 3 years:", simple_interest)
#*************************************************************************************************

'''Task 2 NUMBERS'''
#1. Formatted String using format function
def format_example(number, format_type):
    formatted = format(number, format_type)
    return formatted

result = format_example(145, 'o')
print("Formatted result:", result)

#2. Area of the Pond and Total Water Calculation

def calculate_water_in_pond(radius, water_per_sq_meter):
    pi = 3.14
    pond_area = pi * (radius ** 2)


    total_water = pond_area * water_per_sq_meter


    return int(total_water)



radius = 84  # meters
water_per_sq_meter = 1.4  # liters

total_water_in_pond = calculate_water_in_pond(radius, water_per_sq_meter)
print("Total amount of water in the pond (liters):", total_water_in_pond)

#3. Speed Calculation

def calculate_speed(distance, time_minutes):

    time_seconds = time_minutes * 60

    speed = distance / time_seconds


    return int(speed)
distance = 490  # meters
time_minutes = 7  # minutes

speed = calculate_speed(distance, time_minutes)
print("Speed in meters per second:", speed)

#************************************************************************************************

'''Task 3 IF CONDITION'''


def check_same_country(city1, city2):
    # Check the country of each city using if-else
    if (city1 == "Mumbai" or city1 == "Chennai") and (city2 == "Mumbai" or city2 == "Chennai"):
        print("Both cities are in India")
    elif (city1 == "Sydney" or city1 == "Melbourne") and (city2 == "Sydney" or city2 == "Melbourne"):
        print("Both cities are in Australia")
    elif (city1 == "Dubai" or city1 == "Abu Dhabi") and (city2 == "Dubai" or city2 == "Abu Dhabi"):
        print("Both cities are in UAE")
    elif (city1 == "New York" or city1 == "Los Angeles") and (city2 == "New York" or city2 == "Los Angeles"):
        print("Both cities are in USA")
    elif (city1 == "London" and city2 == "London"):
        print("Both cities are in the UK")
    elif (city1 == "Paris" and city2 == "Paris"):
        print("Both cities are in France")
    elif (city1 == "Berlin" and city2 == "Berlin"):
        print("Both cities are in Germany")
    else:
        print("They don't belong to the same country")


city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")


check_same_country(city1, city2)

#**************************************************************************************************

'''Task 4 IF CONDITION'''

#1. BMI Category Program

# Function to calculate BMI and determine the category
def determine_bmi_category(height, weight):

    bmi = weight / (height ** 2)

    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi_category = determine_bmi_category(height, weight)
print(f"Your BMI Category is: {bmi_category}")


#. City-to-Country Program

# Function to determine the country of a city
def determine_country(city):
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    if city in australia:
        return f"{city} is in Australia"
    elif city in uae:
        return f"{city} is in UAE"
    elif city in india:
        return f"{city} is in India"
    else:
        return f"{city} is not in our database"
city_name = input("Enter a city name: ")
country = determine_country(city_name)
print(country)


#*******************************************************************************************

'''Task 5 Loops'''
#1. Simulating Rolling a Six-Sided Die
import random

count_6 = 0
count_1 = 0
consecutive_6s = 0

previous_roll = None

for i in range(20):
    roll = random.randint(1, 6)

    # Count the number of 6s
    if roll == 6:
        count_6 += 1

        if previous_roll == 6:
            consecutive_6s += 1

    if roll == 1:
        count_1 += 1

    previous_roll = roll
print(f"Number of times you rolled a 6: {count_6}")
print(f"Number of times you rolled a 1: {count_1}")
print(f"Number of times you rolled two consecutive 6s: {consecutive_6s}")


# 2.Workout Routine: Jumping Jacks


total_jumping_jacks = 100
set_size = 10
completed_jacks = 0


for i in range(0, total_jumping_jacks, set_size):
    completed_jacks += set_size
    print(f"Completed {completed_jacks} jumping jacks.")


    response = input("Are you tired? (yes/no): ").lower()

    if response in ["yes", "y"]:

        skip_response = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip_response in ["yes", "y"]:
            print(f"You completed a total of {completed_jacks} jumping jacks.")
            break
    else:

        remaining_jacks = total_jumping_jacks - completed_jacks
        print(f"{remaining_jacks} jumping jacks remaining.")
else:

    print("Congratulations! You completed the workout.")

