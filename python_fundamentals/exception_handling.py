number = 0
try:
    number = int(input("enter number "))
    result = number / 0
except ValueError:
    print('invalid value')
except Exception:
    print('some other exception')

print(number)