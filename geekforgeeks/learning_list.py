import numpy as np

def list_append():
    a = [2, 'Hello', 'Hello World']

    print(a)

    a.append(20)

    print(a)


def numpy_example():

    single_dim = np.array([1,2,3,4,5])

    print(single_dim * 2)

    multi_dim = np.array([[1,2],[3,4],[5,6]])
    print(multi_dim * 2)

# numpy_example()

def hanker_rank_list_operations():
    N = int(input())

    lst = []

    for _ in range(N):
        command = input().strip().split()

        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == 'remove':
            lst.remove(int(command[1]))
        elif command[0] == 'append':
            lst.append(int(command[1]))
        elif command[0] == 'sort':
            lst.sort()
        elif command[0] == 'pop':
            lst.pop()
        elif command[0] == 'reverse':
            lst.reverse()
        else:
            print(lst)
    # lst.append(1)
    # lst.append(2)
    # lst.insert(0,5)
    # lst.insert(1,10)
    # lst.insert(0,6)
    # print(lst)
    # lst.remove(6)
    # lst.append(9)
    # lst.append(1)
    # lst.sort()    
    # print(lst)
    # lst.pop()
    # lst.reverse()
    # print(lst)
    


hanker_rank_list_operations()