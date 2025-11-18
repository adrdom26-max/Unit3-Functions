# def safe_multiply(x, y):
#     try:
#         if isinstance (x(int,float)) and isinstance (y(int,float)):
#             return x * y
#     except TypeError:
#         print("Not valid number")
#         return 0 
# print(safe_multiply(5, 5))


def is_positive(value):
    try:
        return isinstance(value,int(float)) and value > 0
    except:
        return False
        
