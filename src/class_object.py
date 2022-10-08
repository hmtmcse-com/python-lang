# Define a class
class Person:
    first_name: str = "Touhid"
    last_name: str = "Mia"

    def get_name(self):
        return self.first_name + " " + self.last_name


# Create Object & Access function
# Object creation
person = Person()

# Access object function
name = person.get_name()
print(name)


# ----------------------------------------------------------------------------------------------------------------------

# Define a class
class Person:
    first_name: str
    last_name: str

    # Constructor
    def __int__(self, first_name, last_name, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    # Method without parameter and with return
    def get_name(self):
        return self.first_name + " " + self.last_name

    # Method with parameter
    def print_phone(self, phone):
        print("Phone number " + phone)

    # Method with parameter default value
    def print_age(self, age=0):
        print("My age is " + str(age))

    # Private method
    def _private_method(self):
        print("This is private method")

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
