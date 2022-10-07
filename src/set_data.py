# ----------------------------------------------------------------------------------------------------------------------
# Define a list
set_data = {}

# Assign value to a set
set_data = {"Touhid Mia", 28, True, 28.5}
# ----------------------------------------------------------------------------------------------------------------------

# Declare Set for access data element
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}

# Print each element of list by loop
for item in set_data:
    print("Item : " + str(item))


# ----------------------------------------------------------------------------------------------------------------------
# Declare Set for access data element
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}

# Check set value is exist on it
if "Bangladesh" in set_data:
    print("Yes key exist")
else:
    print("Key not exist")

# ----------------------------------------------------------------------------------------------------------------------
# Declare Set
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}

# Set add item using add function
set_data.add("I have a child")
print(set_data)

# ----------------------------------------------------------------------------------------------------------------------
# Declare Set
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}
updated_set_data = {"I have a child", "I have a beautiful wife"}

# Set add item using update function
set_data.update(updated_set_data)
print(set_data)


print("-------------------- Remove ---------------------------------")
# ----------------------------------------------------------------------------------------------------------------------
# Declare Set
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}

# Set remove item using remove function
set_data.remove("Bangladesh")
print(set_data)

# ----------------------------------------------------------------------------------------------------------------------
# Declare Set
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}

# Set remove item using discard function
set_data.discard("Bangladesh")
print(set_data)

# ----------------------------------------------------------------------------------------------------------------------
# Declare Set
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}

# Set remove last item using pop function
set_data.pop()
print(set_data)

# ----------------------------------------------------------------------------------------------------------------------
# Declare Set
set_data = {"Touhid Mia", "Bangladesh", 28, 5.10, True}

# Set remove all item using clear function
set_data.clear()
print(set_data)


