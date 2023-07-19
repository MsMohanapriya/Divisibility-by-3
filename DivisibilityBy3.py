def DivisibilityBy3(array):
    array_sum=sum(array)
    
    if(array_sum%3==0):
        return 1
    return 0

array=list(map(int,input("enter array elements: ").split()))
print(DivisibilityBy3(array))