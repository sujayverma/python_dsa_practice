import sys
def fun(n):
    
    if n == 0:
        return
    print('Gfg')
    fun(n-1)


# fun(3)

class RecursiveLearning():
    def __init__(self):
        self.LIMIT=1000
        self.fp = 15

    def sum_of_natural_numbers(self, x, y):
        if x == 0:
            return y
        else:
            return self.sum_of_natural_numbers(x-1, x+y)
        
    def fun1(self, n):
        if n <= 1:
            return 0
        else:
            return 1 + self.fun1(n//2)
        
    def fact(self,n):

        if n <= 1:
            return 1
        return n * self.fact(n-1)
    
    def binary(self, n):

        if(n == 0):
            return 
    
        self.binary(n // 2)
        print(n % 2, end="")

    def fun(self, x):
    
        if(x > 0):
            x -= 1
            self.fun(x) 
            print(x , end=" ")
            x -= 1
            self.fun(x) 
            
    def star(self,n):
        i = 0
        if (n > 1):
            self.star(n - 1)
        for i in range(n):
            print(" * ", end="")

    def hundreds(self, n):
        if n <= 0:
            return
        if n > self.LIMIT:
            return
        print(n, end=' ')
        self.hundreds(2 * n)
        print(n, end=' ')

    def array_recursive(self, a, n):
        if(n == 1):
            return a[0]
        else:
            x = self.array_recursive(a, n - 1)
        if(x > a[n - 1]):
            return x
        else:
            return a[n - 1]
        
    def double_recursion(self, i): 

        if (i % 2 == 1) :
            i += 1
            return (i - 1)
        else :
            return self.double_recursion(self.double_recursion(i - 1))
        
    def complex(self,n):
        if (n <= 2):
            self.fp = 1
            return 1

        t = self.complex(n - 1)
        f = t + self.fp
        self.fp = t
        return f
    
    def minIndex(self, arr, s, e):
    
        sml = sys.maxsize
        mindex = 0
        
        for i in range(s, e):
            if (sml > arr[i]):
                sml = arr[i]
                mindex = i
                
        return mindex
    
    def array_indexing(self, arr, start_index, end_index):
    
        if (start_index >= end_index):
            return
            
        # minIndex() returns index of minimum value in
        # array arr[start_index...end_index]
        min_index = self.minIndex(arr, start_index, end_index)
        arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
        self.array_indexing(arr, start_index + 1, end_index)

    


        

recursive = RecursiveLearning()
# print(recursive.sum_of_natural_numbers(5,2))
# print(recursive.fun1(8))
# print(recursive.fact(5))
# recursive.binary(21)
# print('')
# recursive.star(5)
# print('')
# recursive.hundreds(100)
# arr = [12, 10, 30, 50, 100]
arr = [64, 25, 12, 22, 11]
n = len(arr)
recursive.array_indexing(arr, 0, n)
print(*arr)