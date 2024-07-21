def multiply(numbers):
    number_list = numbers.split(',')
    number_int_list = [int(n) for n in number_list]
    result = 1
    for n in number_int_list:
        result *= n
    return result

numbers = input('Dime todos los numeros que quieres multiplicar (separados por comas):')

print(f"El resultado es: {multiply(numbers)}")