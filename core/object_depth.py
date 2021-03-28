# Print nested dictionary keys with their depth and handle a python object also
def print_depth(data, i=0):

    key_items = []

    for key, value in data.items():
        temp = key + " " + str(i+1)
        key_items.append(temp)

        # check the value object or not
        if hasattr(value, '__dict__'):
            value = value.__dict__

        # Check the value dict or not
        if isinstance(value, dict):
            key_items.append(print_depth(value, i + 1))

    return '\n'.join(key_items)
