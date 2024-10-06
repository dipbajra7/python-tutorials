random_string = "Python's course for beginners"
random_string2 = 'Python course for "Beginners"'
print(random_string)
print(random_string2)

print(random_string[0]) #prints P
print(random_string2[-2]) #prints s
print(random_string[0:5]) #prints Pytho -- excludes the charater at 5th index
print(random_string[0:]) #prints Python's course for beginners. start index default is 0, end index default is entire string
print(random_string[:]) #prints Python's course for beginners. 
#using triple quotes
email = '''

Dear user

this is the email body


Thank you,
User2



'''

print(email)


#formatted string

first = 'James'
last = 'Bond'

message = f'{first} {last} is cool '
print(message)

print(len(first)) # length of characters in first

print(first.find('s')) # prints index 4

msg = "this is a message"
print('is' in msg) #java contains function on string, returns boolean
