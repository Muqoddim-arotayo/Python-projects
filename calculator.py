print('CALCULATOR')
print('list of operations: +, -, /, *, %, **')
operation = input('input the opetaion to be carried out >>> ')
first_value = input('input your first value >>> ')
if first_value.isdigit() :
    second_value = input('input your second value >>> ')
    if second_value.isdigit() :
        if operation == '+' :
            answer = int(first_value) + int(second_value)
            print(f'Answer = {answer}')
        elif operation == '-' :
            answer = int(first_value) - int(second_value)
            print(f'Answer = {answer}')
        elif operation == '/' :
            answer = int(first_value) / int(second_value)
            print(f'Answer = {answer}')
        elif operation == '*' :
            answer = int(first_value) * int(second_value)
            print(f'Answer = {answer}')
            print(f'Answer = {answer}')
        elif operation == '%' :
            answer = int(first_value) % int(second_value)
            print(f'Answer = {answer}')
        elif operation == '**' :
            answer = int(first_value) **int( second_value)
            print(f'Answer = {answer}')
        else :
            print('operation not identified')
    else :
        print('input a valid numer')
else :
    print('input a valid number')

