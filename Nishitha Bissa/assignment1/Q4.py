m = int(input("enter the number: "))
n = m
def uniquePaths(m: int, n: int) -> int:
        
    memo = {(1,1): 1}
        
    def helper(m,n):
            
        if m < 1 or n < 1:
            return 0
            
        if (m,n) in memo:
            return memo[(m,n)]
        elif (n,m) in memo:
            return memo[(n,m)]
        else:
            memo[(m,n)] = helper(m-1,n) + helper(m,n-1)
                
        return memo[(m,n)]
        
    return helper(m,n)

print(uniquePaths(m,n))
