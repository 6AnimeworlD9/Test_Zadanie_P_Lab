import sys

def min_kol_hod(mas):
    med= mas[len(mas)//2]
    hod=0
    for i in mas:
        hod += abs(i-med)
    return hod

mas = []
with open(sys.argv[1],'r') as massiv:
    for i in massiv:
        mas.append(i)
        mas[-1]=int(str(mas[(-1)].strip()))
mas.sort()
print(min_kol_hod(mas))