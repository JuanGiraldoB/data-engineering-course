# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Access dictionary views
keys_view = my_dict.keys()
values_view = my_dict.values()
items_view = my_dict.items()

# Print initial views
print("Initial keys:", list(keys_view))
print("Initial values:", list(values_view))
print("Initial items:", list(items_view))

# Modify the dictionary
my_dict['d'] = 4  # Add a new key-value pair
my_dict['a'] = 10  # Modify a value

# Print updated views
print("\nUpdated keys:", list(keys_view))
print("Updated values:", list(values_view))
print("Updated items:", list(items_view))
