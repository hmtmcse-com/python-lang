from abc import ABC, abstractmethod


# Person Abstract class
class Person(ABC):

    @abstractmethod
    def details(self):
        pass


# Implement Abstract class
class Customer(Person):

    def details(self):
        print("Implemented abstract method")


# Create Child class object
customer = Customer()

# Call the abstract method
customer.details()
