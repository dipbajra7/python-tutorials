#type conversion

birth_year_string = "1994"
print(type(birth_year_string)) # prints data type
year = 2023
age = year - int(birth_year_string) #string to int
print(age);

flag_string = "True"
flag = bool(flag_string)
print(flag)

number = 123
string_number = str(number)
print(string_number)