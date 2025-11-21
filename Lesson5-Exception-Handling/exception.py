"""
Lesson 5: Exception Handling - Practice Exercises
"""
# Common exception types 
# 1 zero division error 
# print(10/0) 
# 2 Type error
# print(5+"5")
# 3 Value error
# print(int("bt"))
# 4 Name error
# print(school)

# try:
#     result = 10/0
# except:
#     print("Cant divide by 0")

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Cant divide by 0")
# except ValueError:
#     print("Thats not a number")


# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Cant divide by 0")
# except ValueError:
#     print("Thats not a number")
# else: 
#     print(f"Result: {result}")
# finally:
#     print("Operation Complete")


# ==========================
# Practice 1: Safe Division
# Instructions: Create a function that divides two numbers safely
# ==========================
# def safe_divide(a, b):
#     try:
#         result = a / b
#         return result
#     except Exception as error:
#         print("An error occured: {error}")

# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# ==========================
# Practice 2: Safe Input
# Instructions: Create a function that safely gets an integer from user
# ==========================
def get_age():
    try:
        age = int(input("Enter your age:" ))
        return age
    except ValueError:
        print("Please enter a number")
        return 0
user_age = get_age()
print(f"Your are {user_age} years old")

# ==========================
# Challenge 1: Safe Calculator
# Instructions: Build a calculator that handles invalid input and division by zero
# ==========================
def get_valid_grade():
    while True:
        try:
            grade = float(input)("Enter your grade: ")
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0-100")
        except ValueError:
            print("Error: Enter a valid grade")


# ==========================
# Challenge 2: Grade Input Validator
# Instructions: Keep asking for a grade until a valid number between 0-100 is entered
# ==========================
valid_grade = get_valid_grade()