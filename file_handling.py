# with open('file1') as f2:
#     print(f2.name)
#     print(f2.mode)
#     print(f2.readable())
#     print(f2.writable())
# with open('file1', 'w') as f1:
#     print(f1.writelines('\n how are you guys'))
#     print(f1)
#     print(f1.write('hai'))


# 'will be added to existing data'
# with open('file1', 'a') as f1:
# print(f1)
# print(f1.writable())
# print(f1.write('its diverse landscapes to its friendly, welcoming people'))
# print(f1.writelines('\nhere a lot that Canada has to offer'))
#     print(f1.writelines(['\ni ', 'like ', 'canada']))
#     print(f1.writelines((' once ', 'have ', 'to', ' visit', ' here')))

# with open('file1') as f1:
# 'to check the file is closed'
#     print(f1.closed)
# 'to close the file'
#     f1.close()
#     print(f1.closed)


# '4.create  a file'
# with open('file2', 'x') as f2:
#     print(f2)

# with open('file3', 'w') as f2:
#     print(f2)
#
# with open('file4', 'a') as f2:
#     print(f2)


# import os
# print(os.remove('file2'))
# print(os.remove('file3'))
# print(os.remove('file4'))


'tell and seek'

# with open('file1', 'r') as f:
#     print(f)
# 'tell --> to know where is cursor'
#     print(f.tell())
# print(f.read(30))
# print(f.tell())
'seek --> to change the cursor from actual position'
# f.seek(40)
# print(f.read(10))
# print(f.tell())


# with open(r'C:\Users\Krishna\OneDrive\Desktop\Resume Template\New folder\KrishnaPrasad_Resume', 'r') as f:
#     print(f)

import csv

# Open the CSV file for reading
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Skip the header row (optional)
    # next(csv_reader)

    # Loop through each row in the CSV file
    for row in csv_reader:
        name, age, location = row
        print(f"Name: {name}, Age: {age}, Location: {location}")
