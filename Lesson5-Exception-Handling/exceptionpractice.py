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
        
x = "text"
y = 20
try:
    output = y + x
except TypeError:
    output = 0
finally:
print("Processing complete")
print(output)

Processing complete 0

def format_message(code,text):
    try:
        return f"[{code}] {text}"
    except: 
        return"[ERROR] invalid"

val1 = 85
val2 = 10
try:
    temp = val1 / val2
except ZeroDivisionError:
    temp = 0
else:
    temp = int(temp) * 2
finally:
print("Calculation done")

calculation done 16


def safe_average(a, b):
    try:
        return (a + b) / 2
    except ZeroDivisionError:
        return 0

    
config = 55.0
def process_value(input_val):
    try:
        result = (input_val - config) * 10
        return result
    except TypeError:
        return 0
    finally:
print("Process complete")
print(process_value(60))

process complete 50


flag = True
try:
    value = 100 * flag
except TypeError:
    value = 0

else:
    value = value + 10
    print(value)

0