def my_local_function():
    x = 10
    print(f"Local scope: x = {x}")

my_local_function()
x = 10 
print(f"Local scope: x = {x}")


print("**************************************************************************")



y =20
def anothoer_global_function():
    print(f"Global scope, y = {y}")

anothoer_global_function()
print(f"Global scope, y = {y}")

print("---------------------------------------------------------------------------------")

x = 10  # x is a global variable

def my_function():
    global x  # Declare x as global to modify it inside the function
    x = 20  # Modify the global variable
    print(f"Inside the function, x = {x}")

print(f"Before calling the function, x = {x}")
my_function()
print(f"After calling the function, x = {x}")
