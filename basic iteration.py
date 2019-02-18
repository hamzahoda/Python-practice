#find smallest number in list
def minimum(lst):
    x=lst[0]
    for i in range(1,len(lst)):
        if x>lst[i]:
            x=lst[i]
    return x
#print(minimum([3,4,5,2,-5,1,0,-1]))

#count even numbers in a list
def even(lst):
    count=0
    for i in range(0,len(lst)):
        if lst[i]%2==0:
            count+=1
    return count
#print(even([3,4,5,2,6,8]))



