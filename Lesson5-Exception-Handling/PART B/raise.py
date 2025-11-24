# def set_volume(level):
#     """Set volume (0-100)"""
#     if level < 0:
#         raise ValueError("Volume cannot be negative")
#     if level > 100:
#         raise ValueError("Volume cannot exceed 100")
    
#     volume = level
#     print(f"Volume set to {volume}")

# try:
#     set_volume(50)
#     set_volume(-20) # Does not work
# except ValueError as error:
#     print(f"Error: {error}")

# """

# which exception should I raise 
# ValueError - Invalid number or format
# TypeError - Wrong data type provided
# RuntimmError - General error in function

# """


# def create_username(name):
#     """
#     Create a valid username
#     Rules:
#         Must be atleast 3 characters
#         Cannot be more than 20
#         Cannot be empty
#     """

#     if name == "" or not name:
#         raise ValueError("Username cannot be empty")
#     if len(name) > 20:
#         raise ValueError("Username cannot be more than 20 characters")
#     if len(name) < 3:
#         raise ValueError("Username cannot be less than 3 characters")

#     username = name.lower()
#     print(f"Username created: {username}")
#     return username

# try:
#     user = create_username("GamerPro")
#     print(f"Success: {user}")
# except ValueError as error:
#     print(f"Error: {error}")

# try:
#     user = create_username("")
#     print(f"Success: {user}")
# except ValueError as error:
#     print(f"Error: {error}")

# try:
#     user = create_username("AD")
#     print(f"Success: {user}")
# except ValueError as e:
#     print(f"Error: {error}")


def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    result = a / b
    return result

try:
    print(divide(10,2))
    print(divide(10,0))
except ValueError as e:
    print(f"Error: {e}")