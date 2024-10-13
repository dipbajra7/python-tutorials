import math

def binary_search(number_search, numbers:list):
    numbers.sort()
    numbers2 = numbers
    index_size = len(numbers)-1
    count = 0
    i = 0
    not_found = True
    while(not_found):
        count+=1
        i = math.floor(index_size/2)
        if(number_search == numbers[i]):
            print(f'search ----> found {number_search} at index {numbers2.index(number_search)} in {count} tries')
            not_found =False
            break
        elif(number_search > numbers[i]):
            numbers = numbers[i+1:index_size+1]
            index_size = len(numbers)-1
        else:
            numbers = numbers[0:i]
            index_size = len(numbers)-1
      


def sequential_search(search_number, numbers:list):
    #sequential/liner/simple search
    numbers.sort()
    search = search_number
    count = 0
    for number in numbers:
        count+=1
        if(search == number):
            print(f'sequential -----> found {search} at index {numbers.index(search)} in {count} tries')
            break





entered_number = int(input('enter number: '))
numbers = list(range(1,101))
binary_search(entered_number, numbers)
# for i in numbers:  
#     search(i, numbers)

# print('================================================')

for i in range(1,101):
    sequential_search(i, numbers)






