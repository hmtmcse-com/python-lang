# ----------------------------------------------------------------------------------------------------------------------
# Access element by index
tuple_data = ("Touhid Mia", 28, True, 28.5)
name = tuple_data[0]
print(name)

# ----------------------------------------------------------------------------------------------------------------------
# Access element by negative index
tuple_data = ("Touhid Mia", 28, True, 28.5, True)
last_item = tuple_data[-1]
print(last_item)

# ----------------------------------------------------------------------------------------------------------------------
# Access multiple element by range of index
tuple_data = ("Touhid Mia", 28, True, 28.5, True)
multiple_item = tuple_data[1:3]  # [start:end]
print(multiple_item)

# ----------------------------------------------------------------------------------------------------------------------
# Access multiple element by range of index (without end)
tuple_data = ("Touhid Mia", 28, True, 28.5, True)
multiple_item = tuple_data[1:]
print(multiple_item)


# ----------------------------------------------------------------------------------------------------------------------
# Access multiple element by range of index (without start)
tuple_data = ("Touhid Mia", 28, True, 28.5, True)
multiple_item = tuple_data[:3]
print(multiple_item)


# ----------------------------------------------------------------------------------------------------------------------
# Access multiple element by range of negative index
tuple_data = ("Touhid Mia", 28, True, 28.5, True)
multiple_item = tuple_data[-3:-1]
print(multiple_item)


# ----------------------------------------------------------------------------------------------------------------------
# Check list value is exist on it
tuple_data = ("Touhid Mia", 28, True, 28.5, True)
if "Bangladesh" in tuple_data:
    print("Yes key exist")
else:
    print("Key not exist")


# ----------------------------------------------------------------------------------------------------------------------
# Declare Tuple for access data element
tuple_data = ("Touhid Mia", 28, True, 28.5, True)

# Print each element of list by loop
for item in tuple_data:
    print("Item : " + str(item))

# ----------------------------------------------------------------------------------------------------------------------
# Tuple add item using append function
tuple_data = ("Touhid Mia", 28, True, 28.5, True)
tuple_data.add("I have a child as well")
print(tuple_data)


