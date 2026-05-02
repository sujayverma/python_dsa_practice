def fun(n):
    
    if n == 0:
        return
    print('Gfg')
    fun(n-1)


# fun(3)

class RecursiveLearning():
    def __init__(self):
        pass

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
    


        

recursive = RecursiveLearning()
# print(recursive.sum_of_natural_numbers(5,2))
# print(recursive.fun1(8))
# print(recursive.fact(5))
recursive.binary(21)
print('')
recursive.star(5)
print('')