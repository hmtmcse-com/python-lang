# Definition of a function
def first_function():
    print("Hi, This is my first function.")


# Called the defined function
first_function()

# ----------------------------------------------------------------------------------------------------------------------


# Definition of a function with 2 parameter
def sum_two_number(first_number: int, second_number):
    print(first_number + second_number)


# Called the defined function
sum_two_number(10, 10.50)


# ----------------------------------------------------------------------------------------------------------------------


# Definition of a function with 2 parameter and return value
def sum_two_number(first_number: int, second_number):
    return first_number + second_number


# Called the defined function
sum_of_2 = sum_two_number(20, 10.50)
print(sum_of_2)


# ----------------------------------------------------------------------------------------------------------------------


# Definition of a function with argument default
def i_am_a(designation="Programmer"):
    print("I am a " + designation)


# Called the defined function
print("Call the function without pass argument : ", end="")
i_am_a()

print("Call the function with pass argument : ", end="")
i_am_a("Doctor")


# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

# Definition of a function with multiple argument
def my_info(first_name, last_name, email):
    print(first_name + " " + last_name + " " + email)


# Called the defined function
my_info(email="hmtmcse.com@gmail.com", last_name="Mia", first_name="Touhid")


# ----------------------------------------------------------------------------------------------------------------------

# Definition of a function with unlimited argument
def my_info(*args):
    print(args[0] + " " + args[1] + " " + args[2])


# Called the defined function
my_info("hmtmcse.com@gmail.com", "Mia", "Touhid", "Some other")


# ----------------------------------------------------------------------------------------------------------------------

# Definition of a function with unlimited keyword argument
def my_info(**kwargs):
    print(kwargs["first_name"] + " " + kwargs["last_name"] + " " + kwargs["email"])


# Called the defined function
my_info(email="hmtmcse.com@gmail.com", last_name="Mia", first_name="Touhid")


# ----------------------------------------------------------------------------------------------------------------------

def empty_function():
    pass


# ----------------------------------------------------------------------------------------------------------------------
