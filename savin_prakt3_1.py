print("Введите произвольное целое число")
opis=""
opis2=""

a=int(input())
if a>0:
    opis="положительное"
else:
    if a<0:
        opis="отрицательное"
    else:
        opis="нулевое"

a1=a%2
if a==0:
    opis2=""
else:
    if a1==0:
        opis2="четное"
    else:
        opis2="нечетное"
print(a," это",opis,opis2,"число")

