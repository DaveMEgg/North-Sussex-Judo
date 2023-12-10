def get_valid_user_input(prompt, valid_options):
    while True:
        try:
            user_input = input(prompt)
            if user_input in valid_options:
                return user_input
            else:
                raise ValueError(f"Invalid input. Please choose from {', '.join(valid_options)}, ensuring you start with a capital letter")
        except ValueError as e:
            print(e)

training_plan_prices = {
    "Beginner": 25.00,
    "Intermediate": 30.00,
    "Elite": 35.00
}
private_coaching_hourly_rate = 9.50
competition_entry_fee = 22.00
weight_categories = {
    "Heavyweight": float('inf'),
    "Light-Heavyweight": 100,
    "Middleweight": 90,
    "Light-Middleweight": 81,
    "Lightweight": 73,
    "Flyweight": 66
}

# Input athlete information
athlete_name = input("Enter athlete's name: ")

while True:
    try:
        training_plan = input("Enter training plan (Beginner/Intermediate/Elite): ")
        if training_plan in {"Beginner", "Intermediate", "Elite"}:
            break  # Break the loop if the input is valid
        else:
            raise ValueError("Invalid training plan. Please choose from Beginner, Intermediate, or Elite, ensuring we start with a capital letter")
    except ValueError as e:
        print(e)

while True:
    try:
        current_weight = float(input("Enter current weight in kg: "))
        break  # Break the loop if the input is successfully converted to float
    except ValueError:
        print("Invalid input. Please enter a valid number for current weight.")

while True:
    try:
        competition_weight_category = input("Enter competition weight category: ")
        if competition_weight_category in weight_categories:
            break
        else:
            raise ValueError("Invalid weight category. Please choose from Heavyweight, Light-Heavyweight, Middleweight, Light-Middleweight, Lightweight, or Flyweight, ensuring you start with a capital letter")
    except ValueError as e:
        print(e)

while True:
    try:
        competitions_this_month = int(input("Enter the number of competitions entered this month: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of competitions.")

private_coaching_hours_input = ""

while True:
    try:
        private_coaching_hours = int(input("Enter the number of hours of private coaching: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of private coaching hours.")

# Calculate training cost based on training plan
if training_plan in training_plan_prices:
    training_cost = training_plan_prices[training_plan] * 4
else:
    print("Invalid training plan selected. Please choose from Beginner, Intermediate, or Elite.")
    exit(1)

# Calculate competition cost
competition_cost = competition_entry_fee * competitions_this_month

# Calculate private coaching cost
private_coaching_cost = private_coaching_hourly_rate * private_coaching_hours

# Calculate total cost
total_cost = training_cost + competition_cost + private_coaching_cost

# Compare current weight with competition weight category
weight_comparison = "in"
if current_weight < weight_categories.get(competition_weight_category, 0):
    weight_comparison = "below"
elif current_weight > weight_categories.get(competition_weight_category, float('inf')):
    weight_comparison = "above"

# Output athlete's information and calculations
print("\nAthlete's Name:", athlete_name)
print("Itemized list of costs for the month:")
print("- Training Cost: £{:.2f}".format(training_cost))
print("- Competition Cost: £{:.2f}".format(competition_cost))
print("- Private Coaching Cost: £{:.2f}".format(private_coaching_cost))
print("- Total Cost for the Month: £{:.2f}".format(total_cost))
print("Comparison of current weight to competition weight category: Current weight is", weight_comparison, "the", competition_weight_category, "category.")