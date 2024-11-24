def sum(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    result = ''
    num, num_ = 0, 0
    for i in range(max(len(num1), len(num2))-1, -1, -1):
        if int(num1[i]) + int(num2[i]) + num >= 10:
            num, num_ = divmod(num1[i] + num2[i]+ num, 10)
            result = str(num_) + result
        else:
            result = str(int(num1[i]) + int(num2[i]) + num) + result
    return result

print(sum(9,2))




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