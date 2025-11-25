# def calculate_kd(kills, deaths):
#     try:
#        kd = kills / deaths
#        return kd
#     except ZeroDivisionError:
#         print(f"Cant calculate kd")
#         return 0
    
# print(calculate_kd(20,5))
# print(calculate_kd(15,0))


# def process_donation(amount):
#     if amount <= 0:
#         raise ValueError("Donation must be positive")
#     print(f"Thanks for ${amount}")

# try:
#     process_donation(25)
#     process_donation(-5)
#     print("All donations processed")
# except ValueError as e:
#     print(f"Error: {e}")


# def create_gamertag(tag):
#     if tag == "":
#         raise ValueError("Tag cannot be empty")
#     if len(tag) > 15:
#         raise ValueError("Tag cannot be more than 15 characters")
#     if ' ' in tag:
#         raise ValueError("Tag contains spaces")
#     return tag
# try:
#     print(create_gamertag("ShadowNinja"))
#     print(create_gamertag("has spaces"))
# except ValueError as e:
#     print(f"Error: {e}")

def split_bill(total_text, people):
    try:
        total = float(total_text)
        each = total / people
        return f"${each: .2f} per person"
    except ValueError:
        return "Enter a valid total"
    except ZeroDivisionError:
        return "Need atleast 1 person"
    
print(split_bill("fifty", 4))
print(split_bill("20.00", 0))
print(split_bill("20.00", 4))
    

