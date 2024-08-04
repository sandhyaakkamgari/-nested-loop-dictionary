# Create a nested loop dictionary
outer_keys = ['a', 'b']
inner_keys = [1, 2]

nested_dict = {}

for outer_key in outer_keys:
    nested_dict[outer_key] = {}
    for inner_key in inner_keys:
        nested_dict[outer_key][inner_key] = outer_key + str(inner_key)

print(nested_dict)