import sys

# плюсануть или минусануть индекса у аргументов, если вдруг не работает
path1=str(sys.argv[1])
path2=str(sys.argv[2])
print(path1,path2)
file1=[]
file2=[]

with open(path1,'r') as tf:
    for i in tf:
        file1.append(i)
    x_center,y_center=file1[0].split(" ")
    x_center=int(x_center)
    y_center=int(y_center.strip())
    r=int(file1[1])
with open(path2,'r') as tf:
    for i in tf:
        file2.append(i)

ln=len(file2)
m_dot_x=[0]*ln
m_dot_y=[0]*ln
for i in range(ln):
    m_dot_x[i],m_dot_y[i]=file2[i].split(" ")
    m_dot_x[i]=int(m_dot_x[i])
    m_dot_y[i]=int(str(m_dot_y[i]).strip())

for i in range(ln):
    dist=pow(pow(m_dot_x[i]-x_center,2)
             +pow(m_dot_y[i]-y_center,2),0.5)
    if(dist==r):
        print(0)
    if(dist>r):
        print(2)
    if(dist<r):
        print(1)