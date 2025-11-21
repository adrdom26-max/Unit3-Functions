# def safe_level_up(xp, hours_studied):
#     try:
#         return xp // hours_studied
#     except ZeroDivisionError:
#         hours_studied = 0
#         print("No grind no glory")
#         return xp // 10


# print(safe_level_up(1000,5))
# print(safe_level_up(500,0))
# print(safe_level_up(750,3))


# def activate_knowledge_crystal(code):
#     try:
#         int(code)
#         return code
#     except ValueError:
#         return 1
#     finally:
#         print("Cyrtsal Energy Surge")

# print(activate_knowledge_crystal("42"))

def count_members(members):
    count = 1
    found_non_separator = False

    for char in members:
        if char == ",":
            count += 1
        else:
            found_non_separator = True

    if not found_non_separator:
        print("Squad Disbanded")
        return 0
    
    return count


def join_study_squad(members):
    if members == "":
        print("Squad Disbanded")
        return 0
    else:
        return count_members(members)
    
print(count_members("Alice,Bob,Charlie"))
print(count_members(",,,,,"))



   