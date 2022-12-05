#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное 
# количество символов влево или вправо. 
# При расшифровке происходит обратная операция. 

alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение: ").upper()
itog = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto - smeshenie
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto - smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
print (itog)
#PS Для дешифровки нужно поменять плюс на минус в строках 14 и 22 
# и поставить тот же шаг шифрования