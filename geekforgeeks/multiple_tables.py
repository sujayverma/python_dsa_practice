def multiplication_of_num(n):

    if n <= 0:
        print(0)
        return
    
    for i in range(1, 11):
        print(f'{n} * {i} = {n*i}')


def recursive_multiple_tables(n, i = 1):
    if i == 11:
        return
    
    print(f'{n} * {i} = {n*i}')
    i = i + 1
    recursive_multiple_tables(n, i)


num = 5
recursive_multiple_tables(num)