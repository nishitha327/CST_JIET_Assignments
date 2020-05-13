ar= list(input('enter the array:').split())
n=len(ar)
def single_entry(ar,n):

    r=int(ar[0])
    
    for i in range(1,n):
             r=r^int(ar[i])
    return r

r=single_entry(ar,n)
print(r)
        
