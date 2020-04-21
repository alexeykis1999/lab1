import matplotlib.pyplot as plt

X = []
Y = []
f = open("asd.txt","r")

while True:

    s=f.readline()
    if not s: break
    llist = list(s.split())
    if "192.0.73.2" in llist[5]:
        X.append(llist[1])
        Y.append(int(llist[11]))


fig, ax = plt.subplots()

ax.bar(X,Y)

plt.title ("Количество переданных данных абонентом")
plt.xlabel ("Время")
plt.ylabel ("объем данных, байт")

plt.show()
