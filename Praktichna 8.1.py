s = input("Введіть рядок: ")

summa = 0
dobutok = 1
є_цифра = False  

for ch in s:
    if ch.isdigit():  
        є_цифра = True
        num = int(ch)
        summa = summa + num
        dobutok = dobutok * num

if є_цифра:
    print("Сума цифр =", summa)
    print("Добуток цифр =", dobutok)
else:
    print("У рядку немає цифр!")