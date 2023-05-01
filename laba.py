def create_dict(s = 'text.txt'):
    A = dict() 
    x = 0
    file = open(s,'r',encoding="utf-8")
    for line in file:
        if line[-1]=='\n' : line = line[:-1]  
        if line[-1]=='\r' : line = line[:-1] 
        line_f = line.split('/')  
        B = dict()
        B['FIO'] = line_f[0]
        B['Number'] = line_f[1]
        B['Count'] = line_f[2]
        B['Money'] = line_f[3]
        A[x] = B
        x += 1
    file.close()
    return A     

def f1(s ='text.txt'):
    file = open(s,'r',encoding="utf-8")
    for line in file: 
        print(line[:-1])
    file.close()
    
def print_dict(D):
    for i in D:
        line=D[i]['FIO']+' '+D[i]['Number']+' '+D[i]['Count']+ ' '+ D[i]['Money']
        print(line)

def f3(D, name):
    for i in D:
        name_on_diction = D[i]['FIO']
        if name_on_diction.strip() == name.strip():
            return D[i]

def f4(D,strukturnoe,m,n):
    L = dict()
    x = 0
    for i in D:
        strukturnoe_on_diction = D[i]['Number']
        time = D[i]['Count']
        if strukturnoe_on_diction.strip() == strukturnoe.strip() and int(time) in range(m,n+1):
            L[x] = D[i]
            x += 1    
    return L

def f5(D,strukturnoe):
    L = dict()
    x = 0
    sum = 0
    for i in D:
        strukturnoe_on_diction = D[i]['Number']
        time = D[i]['Count']
        money = D[i]['Money']
        if strukturnoe_on_diction.strip() == strukturnoe.strip():
            L[x] = D[i]
            sum += int(money)
            x += 1
    return L, sum

m = 1
s = 'text.txt'
while m != 0 :
    print('Выберите действия -')
    print('1 - Вывод на экран файла')
    print('2 - Чтение данных из файла в словарь. Вывод словаря.')
    print('3 - Поиск по ФИО')
    print('4 - Поиск по номеру подразделения и количеству рабочих дней (диапазон) ')
    print('5 - Поиск по номеру подразделения, вывод общей суммы выплат ') 
    print('0 - Выход из программы')
    
    m = int(input())
    
    if   m == 1 :  
        f1(s)
    elif m == 2 :
        Diction = create_dict(s)
        print_dict(Diction)
        print('-------')
    elif m == 3 : 
        Diction = create_dict(s)
        k = f3(Diction, input())
        print('Результаты поиска: ', k)
        print('-------')
    elif m == 4:
        Diction = create_dict(s)
        Diction_Avtor = f4(Diction,input("Введите номер структурного подразделения: "),int(input("Нижний порог диапазона: ")),int(input("Верхний порог диапазона: ")))
        print_dict(Diction_Avtor)
        print(f'Сотрудники, подходящие под критерии: {Diction_Avtor}')
        print('-------')
    elif m == 5:
        Diction = create_dict(s)
        Diction_Max, sum = f5(Diction,input("Номер структурного подразделения: "))
        print(f'Сотрудники, подходящие под критерий:{Diction_Max}')
        print(f'Сумма выплат: {sum}')
        print('-------')        
    elif m == 6:
        print()