import math

# space complexity of O(n). everytime the list is spliced into smaller lists.
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




# space complexity of O(1) or constant space. the list is not spliced and only the index moves
def binary_search2(number_search, numbers:list):
    count = 0
    start_index = 0
    end_index = len(numbers)-1
    not_found = True
    while(not_found):
        count+=1
        midpoint = math.floor((start_index + end_index)//2)
        if(number_search == numbers[midpoint]):
            print(f'search ----> found {number_search} at index {numbers.index(number_search)} in {count} tries')
            not_found =False
            break
        elif(number_search > numbers[midpoint]):
            start_index = midpoint + 1

        else:
            end_index = midpoint - 1
      


numbers = list(range(1,101))
binary_search2(99, numbers)

entered_number = int(input('enter number: '))
numbers = list(range(1,101))
binary_search(entered_number, numbers)
# for i in numbers:  
#     search(i, numbers)

# print('================================================')

for i in range(1,101):
    sequential_search(i, numbers)
