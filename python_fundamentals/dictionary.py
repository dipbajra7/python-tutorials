customer = {
    "name": "Dave",
    "age":30,
    "phone": "123445566790"

}

print(customer["name"])
#print(customer["email"]) # throws error because there is no email key
print(customer.get("email")) # returns none. handles error
print(customer.get("email", "test@test.com")) # can also provide new key value
customer["name"] = "Dave Smith"

print(customer)

print('----------------------------')
numbers = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}

number = str(input("Enter numbers in digits"))

for num in number:
    print(numbers.get(num))
