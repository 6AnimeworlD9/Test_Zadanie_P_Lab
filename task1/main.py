# Считывание данных
print('Введите n: ', end='')
n=int(input())
print('Введите m: ', end='')
m=int(input())

# Создание массивов и переменных
lenght=1
mas=[0]*m
mas[0]=0
mas[m-1]=1
way=""
last=0

# Идем по циклу пока последним элементом(переменная last) не станет цифра '1'
# заодно записываем путь(первую цифру) в переменную way
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

