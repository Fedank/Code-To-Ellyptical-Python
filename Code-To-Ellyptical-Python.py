
'''
Structure:
exec(%c * n_characters % (tuple containing ASCII numbers for each character in order))
'''

# Read from file
file_path = input("File path (WARNING: the file will be modified irreversibly into ellyptical python): ")
with open(file_path, 'r') as file:
    lines = file.readlines()
    string = ''.join(lines)

# Convert the code to ellyptical python
result = "("

for c in string:
    result += (ord(c) * "--(...==...)")
    result += ","
result = result.strip(",")
result += ")"

# Add the exec() part to actually make it execute
write_to_file = "exec('%c' * " + str(len(string)) + " % " + result + ")"

# Overwrite original file
with open(file_path, 'w') as file:
    file.write(write_to_file)
