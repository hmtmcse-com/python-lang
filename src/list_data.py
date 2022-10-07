# ----------------------------------------------------------------------------------------------------------------------
# Define a list
mix_list = []

# Assign value to a list
mix_list = ["Touhid Mia", 28, True, 28.5]

# ----------------------------------------------------------------------------------------------------------------------
# Declare List for access data element
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# ----------------------------------------------------------------------------------------------------------------------
# Access element by index
name = list_data[0]
print(name)

# Access element by negative index
last_item = list_data[-1]
print(last_item)

# Access multiple element by range of index
multiple_item = list_data[1:3]
print(multiple_item)

# Access multiple element by range of index (without end)
multiple_item = list_data[1:]
print(multiple_item)

# Access multiple element by range of index (without start)
multiple_item = list_data[:3]
print(multiple_item)

# Access multiple element by range of negative index
multiple_item = list_data[-3:-1]
print(multiple_item)

# Check list value is exist on it
if "Bangladesh" in list_data:
    print("Yes key exist")
else:
    print("Key not exist")

# ----------------------------------------------------------------------------------------------------------------------
# Declare List for access data element
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# Print each element of list by loop
for item in list_data:
    print("Item : " + str(item))

# ----------------------------------------------------------------------------------------------------------------------
# List add item using append function
list_data.append("I have a child as well")
print(list_data)

# List add item into specific index using insert function
list_data.insert(5, "I have a beautiful wife")
print(list_data)

# Merge 2 list
primary_color = ["Red", "Yellow", "Blue"]
secondary_color = ["Orange", "Green", "Violet"]


print(">>> Before extend Secondary color")
print(primary_color)

primary_color.extend(secondary_color)
print(">>> After extend Secondary color")
print(primary_color)

# ----------------------------------------------------------------------------------------------------------------------
# Update list item using index
list_data[0] = "Mia Bhai"
print(list_data)

# Update list multiple item using index
list_data[0:1] = ["Name", "Country"]
print(list_data)

# ----------------------------------------------------------------------------------------------------------------------
# Existing List
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# Remove List Item using name
list_data.remove("Bangladesh")
print(list_data)

# ----------------------------------------------------------------------------------------------------------------------
# Existing List
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# Remove List Item using Specified Index by pop function
list_data.pop(0)
print(list_data)

# ----------------------------------------------------------------------------------------------------------------------
# Existing List
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# Remove List last item by pop function
list_data.pop()
print(list_data)

# ----------------------------------------------------------------------------------------------------------------------
# Existing List
list_data = ["Touhid Mia", "Bangladesh", 28, 5.10, True]

# Remove list all item using clear function
list_data.clear()
print(list_data)


