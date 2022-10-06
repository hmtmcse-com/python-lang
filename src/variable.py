# ----------------------------------------------------------------------------------------------------------------------

# Variable declare & assign value
string_variable = "This is String Data"
integer_variable = 100
float_variable = 100.10
boolean_variable = True


# ----------------------------------------------------------------------------------------------------------------------
# Multiple assignment
car, country, model = "Rolls-Royce", "United Kingdom", "Phantom"
print(car + " " + country + " " + model)


# ----------------------------------------------------------------------------------------------------------------------
# Multiple variable Same value assignment
weekend = public_holiday = eid_day = "Monday"
print(weekend + " " + public_holiday + " " + eid_day)


# ----------------------------------------------------------------------------------------------------------------------
# List value into variable
car, country, model = ["Rolls-Royce", "United Kingdom", "Phantom"]
print(car + " " + country + " " + model)


# ----------------------------------------------------------------------------------------------------------------------
# Local variable example
def print_my_name():
    name = "Touhid Mia"
    print("My name is " + name)


# Call the function
print_my_name()

# Call the local variable
# print(name)


# ----------------------------------------------------------------------------------------------------------------------
# Global variable example

name = "Touhid Mia"  # Global variable


def print_my_name():
    print("Function: My name is " + name)


# Call the function
print_my_name()

# Call the global variable
print("Outside : " + name)


# ----------------------------------------------------------------------------------------------------------------------
# Global variable example
def print_my_name():
    global my_name
    my_name = "Touhid Mia"
    print("My name is " + my_name)


# Call the function
print_my_name()

# Call the local (global) variable
print(my_name)

# ----------------------------------------------------------------------------------------------------------------------
