f,b,fd,bd,st = map(int,input().split(" "))
bd=-bd
if(f == b):
    if(f>=fd):
        print(fd*st)
    else:
        print("NO")
else:
    p,t = 0,0
    while(1):
        if(p+f >=fd):
            print('F',(t+fd-p)*st)
            break
        else:
            p=p+f
            t=t+f
        if(p-b<=bd):
            print('B',(t-bd+p)*st)
            break
        else:
            p=p-b
            t=t+b