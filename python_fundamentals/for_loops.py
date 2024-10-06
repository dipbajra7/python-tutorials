customers = ["jake", "john", "ryan"]
for customer in customers:
    print(customer)

for number in range(10):
    print(number)
print('######')
for number in range(5,10):
    print(number)
print('######')
for number in range(5,10,2):
    print(number)
print('######')


cart_prices = [10,20,30]
total = 0
for price in cart_prices:
    total = total + price
print(f"total is {total}")

x = 0
y = 0
while x != 3:
    for x in range(4):
        for y in range(4):
            print(f"{x},{y}")


###############################

numbers = [5,2,5,2,2]

for number in numbers:
    print(number * 'x')

###############################

print('###############################')
numbers = [5,2,5,2,2]
for number in numbers:
    output = ''
    for i in range(number):
        output+='x'
    print(output)


print('###############################')
numbers = [2,2,2,2,6]
for number in numbers:
    output = ''
    for i in range(number):
        output+='x'
    print(output)