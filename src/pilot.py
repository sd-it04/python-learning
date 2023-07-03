print('Welcome to multiply function demo')


def multiply_by_2(num):
    return num*2


input_number = input("Enter a number: ")
output_number = multiply_by_2(int(input_number))

print(f'{input_number} multiply by 2 is {output_number}')
