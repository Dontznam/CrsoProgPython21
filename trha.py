
#s = input("Inserisci stringa: ")
#while len(s) < 2:
#    print("La riga è troppo corta!")
#    s = input("Inserisci stringa: ")

#nuevas = s[-2] + s[-1]
#for i in range(3):
#    nuevas = nuevas + s[-2] + s[-1]
#print(nuevas)
# lis = []
# lis2 = []
# fusl = []

# def prendi_elemento_lst(n):
#     tlis = []
#     i = 1
#     while i <= n:
#         pezzo = input("Inserisci stringa: ")
#         i = i + 1
#         tlis.append(pezzo)
#     return tlis

# n = 0
# n1 = int(input("dimensione lis1: "))
# n2 = int(input("dimensione lis2: "))

# lis = prendi_elemento_lst(n1)
# lis2 =  prendi_elemento_lst(n2)
# fusl = lis + lis2

        
# for i in lis:
#         if i in lis2:
#             while i in fusl:
#                 fusl.remove(i)


""" 4rn vrtuh54 nvht """
# print(fusl)
""" ll = 0
while ll <= 0:
    ll = int(input("Lunghezza lista da inseire(non può essere meno di zero): ")) or 0
lst = []
lst2 = []
n = 1
while n <= ll:
    lst.append(input("Aggiungi elemento: "))
    n = n + 1
# lst = ["Gracco", "Fedesso", "Arse", "Nigg Rock", "Nurgfere"]
m = 0
while m <= 0:
    m = int(input("Lunghezza parole da stampare: "))


for i in range(0, len(lst)):
    if len(lst[i]) > m:
        lst2.append(lst[i])
print(lst2)
 """
# lin = []
# n = int(input("Numero Caratteri: "))
# str = ""
# c = ""

# while len(lin) < n:
#     while len(c) != 1:
#         c = input("Aggiungi carattere: ")
#     lin.append(c)
#     c = ""


# for i in lin:
#     str = str + i

# print(str)

t = ("a", "4", "c")
lt = list(t)
# st = input("Elemento da aggiungere. ")
print("Lista: " + str(lt))
rt = input("Elemento da eliminare. ")
# lt.append(st)
# t2 = tuple(lt)

# print(t2)
for i in lt:
        if i == rt:
            while i in lt:
                lt.remove(i)
t2 = lt

# lt.reverse()
# t2 = tuple(lt)
# print(t2)

