import math

#space complexity O(n)
def binary_search3(number_search, numbers: list):
  
    start_index = 0
    end_index = len(numbers)-1

    if numbers is None or (start_index - end_index) <= 0:
        print('number not found in the list')
        return
    
    midpoint = math.floor((start_index + end_index)//2)
    if(number_search == numbers[midpoint]):
        print(f'search ----> found {number_search}')
        
    elif(number_search > numbers[midpoint]):
        binary_search3(number_search, numbers[midpoint+1:])

    else:
        binary_search3(number_search, numbers[:midpoint-1])




binary_search3(44, list(range(0,11)))