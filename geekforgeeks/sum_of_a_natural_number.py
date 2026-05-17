def sum_natural_number(n):
    sum = 0
    if n == 0:
        return 0
    
    for i in range( n + 1):
        sum = sum + i

    return sum

def recursive_sum(n):

    if n <= 0:
        return 0
    
    
    return n + recursive_sum(n-1)

def formula_sum(n):

    sum = (n * (n + 1)) // 2
    return sum

num = 10
print(f'The Sum of {num} is {formula_sum(num)}')