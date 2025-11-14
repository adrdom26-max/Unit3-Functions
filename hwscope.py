val = 10
def update(val):
    val += 5
return val
print(update(val))
print(val)

# both print 15

def multiply(n):
    return n * 3
def add(x):
    return x + 4
result = add(multiply(2))
print(result)

# result = 10

def outer_func(a):
    b = 3
    def inner_func(c):
        return a + b + c
    return inner_func(2)

print(outer_func(5))

# result = 10

counter = 1

def increment_counter():
    global counter       
    counter += 3         
    return counter       

print(increment_counter())  
print(counter)

# both print 4

score = 50

def reset():
    global score
    score = 0
    return score

print(reset())  
print(score)

# both = 0



def square_plus_one(n):
    return n * n + 1



def register_user(name, age):
    return f"User {name}, {age} years old, registered"



my_list = []  

def update_global_list(item):
    global my_list       
    my_list.append(item) 
    return my_list



def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 3