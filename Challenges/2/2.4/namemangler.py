# Mangle the name by reversing it or borgifying it
def modified_name(choose, name):
    # Split the name into first and last in an array
    split_name = name.split()
    # Reverse the array of name components so the array is [last, first]
    reversed_name_components = list(reversed(split_name))
    # Rejoin the array of name components
    new_name1 = ' '.join(reversed_name_components)
    # Store the mangled name
    name = new_name1
    print(new_name1)
    if choose:
        # Split the name into last and first in an array
        split_name2 = new_name1.split()
        # Reverse the array of name components so the array is [last, first]
        reversed_name_components2 = list(reversed(split_name2))
        # Add borg to the end of the array
        reversed_name_components2.append("Borg")
        # Rejoin the array of name components
        new_name2 = ' '.join(reversed_name_components2)
        print(new_name2)
        name = new_name2
    return name

name = "Johanna Jackson"
mod_name = modified_name(False, name)
print(mod_name)
print(f"New name: {mod_name}")
mod_name2 = modified_name(False, name)
print(mod_name2)
print(f"New name: {mod_name2}")