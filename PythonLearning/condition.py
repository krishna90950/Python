'convert program to lower to upper'

# Str_1 = input("Enter a string")
#
# if Str_1.islower():
#     print("string is lower case and its converted to upper")
#     print(Str_1.upper())
# elif Str_1.isupper():
#     print("string is upper case and its converted to lower")
#     print(Str_1.lower())
# else:
#     print("Mixed characters both upper and lower")

'check if vowel or not, if vowel create a dictionary with vowel and ascii value'
# Str_1 = input("Enter a string")
# if Str_1 in ('aeiouAEIOU'):
#     print("String is Vowel")
#     Str_2 = ord(Str_1)
#     Di_2 = dict([(Str_1,Str_2)])
#     print(Di_2)
# else:
#     print("String is not a vowel")
'Check the word is palindrome or not'
# Str_1 = input("Enter a string")
# if Str_1:
#     Str_2 = Str_1[::-1]
#     print(Str_2, type(Str_2))
#     if Str_2 == Str_1:
#         print("String is palindrome")
#     else:
#         print("String is not palindrome")
'Check the integer is palindrome or not'
# num_1 = int(input("Enter a string"))
# if num_1:
#     Str_3 = str(num_1)
#     Str_4 = Str_3[::-1]
#     if Str_4 == Str_3:
#         num_2 = int(Str_4)
#         print(num_2, type(num_2))
#         print("int is palindrome")
#     else:
#         print("String is not palindrome")
'Check the year is leap year or not'
# yr_1 = int(input("Enter a year"))
# if yr_1 % 4 == 0:
#     print("its a leap year")
# else:
#     print("its not a leap year")
'Check the given character is number or alphabet or special character'
# inp_1 = input("Enter the value")
# if inp_1.isnumeric():
#     print(f'{inp_1}  is numeric')
# elif inp_1.isalpha():
#     print(f'{inp_1} is alphabet')
# elif inp_1.isalnum():
#     print(f'{inp_1} is alphanumeric')
# else:
#     print(f'{inp_1} is special character')
'Check if the given number is perfect square or not'
'Check if the given mark is pass (above 35), fail (below 35) or first class (above 60)'
#
# Mark_1 = int(input("Enter the mark"))
# if Mark_1 >= 60 :
#     print("First class")
# elif Mark_1 >= 35 and Mark_1 < 60:
#     print("Pass")
# elif Mark_1 < 35 :
#     print("Fail")
'Check if the given string is starts with vowels or not'
# Str_6 = input("Enter the string")
# Str_7 = 'aeiouAEIOU'
# if Str_6[0] == Str_7[0]:
#     print(f"string starts with vowel letter '{Str_7[0]}'")
# elif Str_6[0] == Str_7[1]:
#     print(f"string starts with vowel letter '{Str_7[1]}'")
# elif Str_6[0] == Str_7[2]:
#     print(f"string starts with vowel letter '{Str_7[2]}'")
# elif Str_6[0] == Str_7[3]:
#     print(f"string starts with vowel letter '{Str_7[3]}'")
# elif Str_6[0] == Str_7[4]:
#     print(f"string starts with vowel letter '{Str_7[4]}'")
# elif Str_6[0] == Str_7[5]:
#     print(f"string starts with vowel letter '{Str_7[5]}'")
# elif Str_6[0] == Str_7[6]:
#     print(f"string starts with vowel letter '{Str_7[6]}'")
# elif Str_6[0] == Str_7[7]:
#     print(f"string starts with vowel letter '{Str_7[7]}'")
# elif Str_6[0] == Str_7[8]:
#     print(f"string starts with vowel letter '{Str_7[8]}'")
# elif Str_6[0] == Str_7[9]:
#     print(f"string starts with vowel letter '{Str_7[9]}'")
# else:
#     print(f"string does not starts with any of the vowel letters {Str_7}")

'Check if the given string is ends with vowels or not'
# Str_8 = input("Enter the string: ")
# Str_9 = 'aeiouAEIOU'
# if Str_8[len(Str_8) - 1] == Str_9[0]:
#     print(f"string ends with vowel letter '{Str_9[0]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[1]:
#     print(f"string ends with vowel letter '{Str_9[1]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[2]:
#     print(f"string ends with vowel letter '{Str_9[2]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[3]:
#     print(f"string ends with vowel letter '{Str_9[3]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[4]:
#     print(f"string ends with vowel letter '{Str_9[4]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[5]:
#     print(f"string ends with vowel letter '{Str_9[5]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[6]:
#     print(f"string ends with vowel letter '{Str_9[6]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[7]:
#     print(f"string ends with vowel letter '{Str_9[7]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[8]:
#     print(f"string ends with vowel letter '{Str_9[8]}'")
# elif Str_8[len(Str_8) - 1] == Str_9[9]:
#     print(f"string ends with vowel letter '{Str_9[9]}'")
# else:
#     print(f"string does not ends with any of the vowel letters {Str_9}")
'Check if the list has even no of elements'

# Lis_3 = []
# t = list(input("Enter list elements: "))
# Lis_3.extend(t)
# print(Lis_3, len(Lis_3))
# val_4 = len(Lis_3)
# if val_4 % 2 == 0:
#     print("The elements in list are even")
# else:
#     print("The element in list are not even")

# d_2 = dict(a=1, b=2, c=3, d=4, e=5)
# k = d_2.keys()
# print(k, len(k))
# if len(k) % 2 == 0:
#     print("dictionary has even number of keys")
# else:
#     d_2['add'] = 'j'
#     print("dictionary has odd number of keys added one key value combination to make it even")
#     print(d_2, len(d_2))
' in a number check if the first number is odd or even'
# Lis_6 = list(input("Enter the number: "))
# if int(Lis_6[0]) % 2 == 0:
#     print(f"First number is even {Lis_6[0]}")
# else:
#     print(f"First number is not even {Lis_6[0]}")
' in a number check if the second last number is odd or even'
# Lis_6 = list(input("Enter the number: "))
# print(len(Lis_6))
# if int(Lis_6[len(Lis_6)-2]) % 2 == 0:
#     print(f"second last number is even {Lis_6[len(Lis_6)-2]}")
# else:
# print(f"second last number is not even {Lis_6[len(Lis_6)-2]}")
'Check if the list has even number of elements'
# Li_1 = ['a', 3.4, (1, 2), ['hi', 9, 'l'], "Hello"]
# a = len(Li_1)
# if a % 2 == 0:
#     print(f"List contains {a} elements which is even")
# else:
#     print(f"List contains {a} elements which is odd")
'Program to check if the given datatype is string of data type'
'Program to check a data is float data type '
# Str_10 = isinstance(4.5, float)
# print(Str_10)
'Program to check the list is empty or not'
# Lis_1 = ['a', 1, 3.4]
#
# if len(Lis_1) == 0:
#     print(f"list has {len(Lis_1)} elements")
# else:
#     print(f"list has {len(Lis_1)} elements")

n1 = int(input())
Sq = n1 ** 0.5
if Sq * Sq == n1:
    print("Yes")
else:
    print ("no")