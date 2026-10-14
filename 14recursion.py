print("Recursion function:")


# function use to call itself.
# factorial of a number:
def fact(n):
    if n == 0 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
# in bg
"""
5*fact(4)
5*4*fact(3)
5*4*3*fact(2)
5*4*3*2*fact(1)
5*4*3*2*1
"""
# calaculate fibonacci sequence using recursion
"""
f0=0
f1=1
f2=f1+f0
f(n)=f(n-1)+f(n-2)
"""

def recur(n):
    if n<=0:
        return n
    else:
        return recur(n-1)+recur(n-2)
#ysing loop as recursion returns multiple values        
for i in range(10):
    print(recur(i),end=("~"))
    
    
    
    

        
        
    
    







