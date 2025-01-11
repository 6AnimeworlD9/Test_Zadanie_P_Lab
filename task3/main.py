import json
import os.path
import sys

# Считывание данных из json-файлов
path1=str(sys.argv[1])
path2=str(sys.argv[2])
path3=str(sys.argv[3])
if (os.path.exists(path1)==False
        or os.path.exists(path2)==False):
    sys.exit()
if os.path.exists(path3)==False:
    open(path3,"w+").close()
with open(path1, 'r') as f:
    val_data = json.load(f)
with open(path2, 'r') as f:
    test_data = json.load(f)

# Дополнение данных из values в tests
def func(t_d,v_d):
    for obj in t_d:
        p=obj['id']
        for i in v_d:
            if i["id"] == p:
                obj['value']=i['value']
        if 'values' in obj:
            func(obj['values'],v_d)

# Запись в новый файл report.json
func(test_data['tests'],val_data['values'])
with open(path3, 'w') as f:
    json.dump(test_data, f, indent=4)