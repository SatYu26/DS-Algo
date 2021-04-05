class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        while True:
            res=0
            while(n>0):
                r=n%10
                res+=(r**2)
                n=n//10
            print(res)
            if res==1:
                return True
            if res<7:
                return False
            n=res