def sum(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    result = ''
    num, num_ = 0, 0
    if len(num1) > len(num2): #Выравнивание кол-ва знаков
        for i in range(len(num1)-len(num2)):
            num2 = '0' + num2
    elif len(num1) < len(num2):               
        for i in range(len(num2)-len(num1)):
            num1 = '0' + num1
    print(f'{num1} + {num2}')
    for i in range(max(len(num1), len(num2))-1, -1, -1):
        if int(num1[i]) + int(num2[i]) + num >= 10:
            num, num_ = divmod(int(num1[i]) + int(num2[i])+ num, 10)
            result = str(num_) + str(num) + result #Тут хуйня переделывай
        else:
            result = str(int(num1[i]) + int(num2[i]) + num) + result #И тут тоже

print(sum(999,2))




#def multiply(num1, num2):
#
#    if (num1*num2) >= 10:
#        num, num_ = divmod((num1*num2), 10)
#        result = f'{num}{num_}'
#    else:
#        result = num1*num2
#    return result
#
#print(multiply(12, 3))


#for i in range(0, 201):
#    for m in range(0,201):
#        if i*m == int(multiply(i,m)):
#            print(f"{i}*{m} = {multiply(i, m)}")  Проверка
#        else:
#            print('error')