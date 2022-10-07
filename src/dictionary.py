# ----------------------------------------------------------------------------------------------------------------------
# Define a dictionary
string_dictionary = {}

# Assign value to a dictionary
string_dictionary = {
    "name": "Touhid Mia",
    "country": "Bangladesh",
    "age": 28,
}


# ----------------------------------------------------------------------------------------------------------------------
# Declare Dictionary for access data element
dictionary_data = {
    "name": "Touhid Mia",
    "country": "Bangladesh",
    "age": 28,
    "height": 5.10,
    "isBeard": True,
}

# Access element by key
name = dictionary_data["name"]
print(name)


# Access element by get function
name = dictionary_data.get("name")
print(name)

# Access dictionary all keys
all_keys = dictionary_data.keys()
print(all_keys)

# Access dictionary all values
all_keys = dictionary_data.values()
print(all_keys)

# Access dictionary items as tuples of list
list_of_tuples = dictionary_data.items()
print(list_of_tuples)

# Check dictionary key is exist on it
if "name" in dictionary_data:
    print("Yes key exist")
else:
    print("Key not exist")

# Print each element of dictionary by loop
for key in dictionary_data:
    value = dictionary_data[key]  # Access value using key
    print("Key : " + key + ", Value : " + str(value))

# ----------------------------------------------------------------------------------------------------------------------
# Dictionary add item using key
dictionary_data["isMarried"] = True
print(dictionary_data)

# Dictionary add item using update function
dictionary_data.update({"hasChild": True})
print(dictionary_data)


# ----------------------------------------------------------------------------------------------------------------------
# Dictionary update item using key
dictionary_data["age"] = 30
print(dictionary_data)

# Dictionary update item using update function
dictionary_data.update({"country": "Canada"})
print(dictionary_data)

# ----------------------------------------------------------------------------------------------------------------------
# Dictionary remove item using key and pop function
dictionary_data.pop("age")
print(dictionary_data)

# Dictionary remove item using key and del
del dictionary_data["country"]
print(dictionary_data)

# Dictionary remove last inserted item by popitem function
dictionary_data.popitem()
print(dictionary_data)

# Dictionary remove all item using clear function
dictionary_data.clear()
print(dictionary_data)
