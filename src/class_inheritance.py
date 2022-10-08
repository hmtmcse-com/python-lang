# Parent class
class Person:

    # Constructor
    def __init__(self, first_name, last_name, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print_details(self):
        details = self.first_name + " " + self.last_name
        if self.email:
            details = " " + self.email
        print(details)

    def parent_method(self):
        print("Called Parent class method")


# Child class
class Customer(Person):

    # Child class method access parent property
    def print_email_address(self):
        print("Customer email is : " + self.email)

    # Called parent class method
    def called_parent_method(self):
        super().parent_method()


# Create Child class object
customer = Customer("Touhid", "Mia", "hmtmcse.com@gmail.com")

# Called parent class method from child object
customer.print_details()

# Called child class method
customer.print_email_address()

# Called child class method which access parent method
customer.called_parent_method()


