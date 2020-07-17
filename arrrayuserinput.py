#to take array element from user input
#to search entered val in array , if present returns its index
from array import *
arr=array('i',[])
n=int(input("enter the array size : "))
for i in range(n):
    x=int(input("enter the value :"))
    arr.append(x)
val=int(input("value to be searched :"))
#print(arr.index(val)) : to directly use function to search (return index of val)
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1