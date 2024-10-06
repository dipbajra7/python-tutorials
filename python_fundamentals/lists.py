numbers = [1,26,4,3,7,93,9,0]
list_size = numbers.__len__()

largest_number = 0
for index in range(list_size):
    if(numbers[index] > largest_number):
        largest_number = numbers[index]
    
print(largest_number)


##### 2d list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])

print('----------------------------')
for row in matrix:
    for data in row:
        print(data)

print('----------------------------')
numbers = [1,2,3,5,4,6]
numbers.append(7)
numbers.sort()
numbers.reverse()
print(numbers)
print(4 in numbers) # returns true
print(60 in numbers) #prints false
numbers.count(3) # returns 1 counts the number of 3s in the list

print('----------------------------')
#remove duplicates in a list.

numbers = [1,2,2,3,4,4,5,6,7,7,8,9]
for number in numbers:
    if numbers.count(number) > 1 :
        numbers.remove(number)
print(numbers)


print('----------------------------')
#remove duplicates in a list manually
numbers = [1,2,2,3,4,4,5,6,7,7,8,9]
new_numbers= []

for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
print(new_numbers)