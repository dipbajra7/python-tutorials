def greet_soumya(s): 
    print(f"hello Soumya {s}")



greet_soumya("baby")
#keyword argument

def print_name(first_name, last_name):
    print(f'hello {first_name} {last_name}')


print_name(last_name="Chiday", first_name="Soumya")


def add_two_numbers(a, b):
    return a + b


sum = add_two_numbers(1,2)
print(sum)