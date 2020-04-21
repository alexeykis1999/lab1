f =open("asd.txt", "r")

summa = 0

while True:

    s=f.readline()
    if not s: break
    llist = list(s.split())
    if "192.0.73.2" in s:
        if "192.0.73.2" in llist[5]: summa+=int(llist[11])

summa = (summa/1024)

if summa > 200:
    summa = 100 + (summa-200)
else: summa/=2

print("итоговая сумма -", "%.2f"%summa, "рублей")

f.close()
