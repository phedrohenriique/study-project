# CREATING DICTIONARIES
my_dict = {"name": "Alice", "age": 25}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25}

# ADDING OR UPDATING KEY, VALUE PAIRS
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# ACCESSING VALUES
print(my_dict["name"])  # Output: Alice
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("country", "Not Found"))  # Output: Not Found

# REMOVING ITEMS
my_dict.pop("city")
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}

my_dict["city"] = "New York"  # Adding back for example
my_dict.popitem()
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}

del my_dict["age"]
print(my_dict)  # Output: {'name': 'Alice'}

my_dict.clear()
print(my_dict)  # Output: {}

# ITERATING THROUGH A DICTIONARY
for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

# HANDLING DUPLICATES
my_dict = {"name": "Alice", "name": "Bob"}
print(my_dict)  # Output: {'name': 'Bob'}

my_dict = {"name": "Alice", "nickname": "Alice"}
print(my_dict)  # Output: {'name': 'Alice', 'nickname': 'Alice'}


# CHECKING EXISTENCE OF KEYS
print("name" in my_dict)  # Output: True
print("age" in my_dict)   # Output: False

# MERGING DICTIONARIES
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "age": 26}
dict1.update(dict2)
print(dict1)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# CHECKING LENGTH
print(len(my_dict))  # Output: Number of key-value pairs