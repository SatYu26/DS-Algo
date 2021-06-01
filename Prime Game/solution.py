def main():

    testCase = int(input())
    def isprime(n):
        if n<=1:
            return False
        for i in range(2,n):
            if n%i ==0:
                return False
        return True
    
    while testCase >0:
        LR = list(map(int,input().strip().split()))
        first = LR[0]
        last = LR[1]
        f = 0
        l = 0
        for i in range(first,last+1):
            if f ==0:
                if isprime(i):
                    f=i
                else:
                    i = i+1
            if l==0:
                if isprime(last):
                    l=last
                else:
                    last -=1
            if f!=0 and l!=0:
                break
            
        if f!=0 and l!=0:
            print(l-f)
        else:
            print(-1)
        
        testCase -=1

main()