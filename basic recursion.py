#without recursion
def factorial(n):
    if n==1:
        return 1
    return factorial(n-1)*n
#print(factorial(3))

def towerOfHanoi1(disks):
    return (2**disks -1)

#with recursion
def towerOfHanoi2(disks):
    if disks==1:
        return 1
    return 2*towerOfHanoi2(disks-1)+1

#print(towerOfHanoi2(3))

#fibonacci numbers 0,1,1,2,3,5,8...
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

#print(fibonacci(6))
