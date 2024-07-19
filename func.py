def multiply(*num):
    result = 1
    for n in num:
        result *= n
    return result

print(multiply(3,5,2))