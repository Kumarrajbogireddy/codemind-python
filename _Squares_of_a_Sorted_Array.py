n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    lst1.append(i*i)
lst1.sort()
for i in lst1:
    print(i,end=' ')