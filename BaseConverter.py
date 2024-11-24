import ConverterFunctions as cf
# ОСНОВАНИЕ СИСТЕМЫ НЕ БОЛЬШЕ 9!!!!!!!!!
def BaseConverter(a, base1, base2):
    a = str(a)
    m = cf.fromdec(base1, base2)
    print(m)
    solution = [['0'] * len(a) for _ in range(0,2)] #[[0]* (кол-во столбцов for _ in range (кол-во строк)]
    for i in range(0, len(a)):
        solution[0][i] = cf.fromdec(int(a[i]), base2)
    solution[1][0] = solution[0][0]
    print(solution[0])
    print(solution[1])
    #for i in range(1, len(a)):
    #    solution[1][i] = умножение solution[1][i-1] на m и + solution[0][i]       (WIP)
    print(solution[0])
    print(solution[1])
    
    
    
print(BaseConverter(4325, 7, 5))
