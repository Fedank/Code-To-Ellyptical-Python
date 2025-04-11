
'''
Struttura
exec()
'%c' * numero di caratteri totali % tuple contenente il numero ASCII di ogni lettera
'''

file_path = input("File path (WARNING: the file will be modified irreversibly into ellyptical python): ")
with open(file_path, 'r') as file:
    lines = file.readlines()
    string = ''.join(lines)

result = "("

for c in string:
    result += (ord(c) * "--(...==...)")
    result += ","
result = result.strip(",")
result += ")"

write_to_file = "exec('%c' * " + str(len(string)) + " % " + result + ")"

with open(file_path, 'w') as file:
    file.write(write_to_file)
