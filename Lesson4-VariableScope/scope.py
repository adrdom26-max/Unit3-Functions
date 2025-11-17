"""
Lesson 4: Variable Scope - Practice Exercises
"""

# ============================================================================
# Practice 1: Local Variables
# Instructions: Create a function that uses local variables for calculations
# ============================================================================
# def calculate_pizza_slices():
#     total_slices = 24
#     people = 6
#     slices_per_person = total_slices / people
#     return slices_per_person

# result = calculate_pizza_slices()
# print(f"Each person gets {result} slices!")
# print(people) local variable does not exist here

# ============================================================================
# Practice 2: Global Constants
# Instructions: Create global constants and a function that uses them
# ============================================================================
# TAX_Rate = 0.08
# SHIPPING_COST = 5.00

# def calculate_tax(price):
#     return price * TAX_Rate

# def calculate_total(price):
#     tax = calculate_tax(price)
#     total = price + tax + SHIPPING_COST
#     return total

# item_price = 50.0
# final_total = calculate_total(item_price)
# print(f"Price ${item_price:.2f}")
# print(f"Total: ${final_total:.2f}")

# ============================================================================
# Practice 3: Parameters Instead of Globals
# Instructions: Rewrite the code to use parameters instead of global variables
# ============================================================================
# Parameters are better to update global variables
# X Bad Example
score = 0 
def add_points():
    global score
    score += 10
    # Where does it run
    # Who changes score
    # Hard to debug
# Good example
def add_points():
    return score + 10
score = 0
score = add_points(score)



# ============================================================================
# Practice 4: Multiple Functions Sharing Data
# Instructions: Create two functions that work together using parameters/return
# ============================================================================



# ============================================================================
# Challenge 1: Shopping Cart System
# Instructions: Build a complete system using proper scope practices
# ============================================================================



# ============================================================================
# Challenge 2: Game Score Calculator
# Instructions: Calculate game score using constants and functions with proper scope
# ============================================================================
