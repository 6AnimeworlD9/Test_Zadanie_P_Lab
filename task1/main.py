print('Введите n: ', end='')
n=int(input())
print('Введите m: ', end='')
m=int(input())
lenght=1
mas=[0]*m
mas[0]=0
mas[m-1]=1
way=""
last=0
while last!=1:
    way+=str(mas[m-1])
    for i in range(m):
        if(i==0):
            mas[i]=mas[m-1]
        else:
            next=(mas[i-1]+1)
            if(next<=n):
                mas[i]=next
            else:
                mas[i]=1
        if(i==m-1):
            last=mas[i]
print(way)

