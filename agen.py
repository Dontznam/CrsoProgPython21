import json

def mostra_elementi(age):
        idage = 0
        for el in age:
            print(int(idage), str(el) + " " + str(age[el]))
            idage = idage + 1

def aggiungi_elemento(age):
        try:
            numa = int(input("Numero da aggiungere: "))
        except:
           numa = 0
        while numa < 1:
            try:
                numa = int(input("Numero da aggiungere: "))
            except:
                numa = 0
        i = 1
        ide = {}
        ep = {}
        while i <= numa:
            n = input("Nome: ")
            c = input("Cognome: ")
            d = input("Email: ")
            pw = input("Passwd: ")


            ide[c] = n 

            age[d] = ide
            ide = {}
            i = i + 1
        return age

def modifica_elemento(age):
        moage = input("Inserire numero dell account da modificare: ")
        ml = 0
        for moager in age:
            if str(ml) == moage:
                moagev = input("Inserire nuova mail: ")
                break
            ml = ml + 1
        age[moagev] = age[moager]
        age.pop(moager, "Elemento non presente")
        return age



def cancella_elemento(age):
#         filaget = open("agenda.dat", "r")
#         agestr = filaget.read()
#         filaget.close()
        # try:
        #     age = json.loads(agestr)
        # except:
        #     age = {}
        #print(agestr)
        elage = input("Inserire numero dell account da eliminare: ")
        el = 0
        for elager in age:
            if str(el) == elage: 
                break
            el = el + 1
        age.pop(elager, "Elemento non presente")
        return age

def svuota_dizionario(nomef):
    filages = open(nomef, "w")
    filages.close()

try:
    filaget = open("agenda.dat", "r")
    agestr = filaget.read()
    filaget.close()
except:
    filaget = open("agenda.dat", "w")
    filaget.close()
    filaget = open("agenda.dat", "r")
    agestr = filaget.read()
    filaget.close()
try:
    age = json.loads(agestr)
except:
    age = {}
print("Seleziona l'operazione da effettuare:")
print("1. Mostra agenda ")
print("2. Aggiungi un account")
print("3. Modifica un account")
print("4. Rimuovi un account")
print("5. Svuota agenda")
print("0. Esci")
ask = ""
while ask != 0:
    try:
        ask = input(": ")
    except:
        ask = 0
    if ask == 0 or ask == "0":
        exit()
    elif ask == "1":
        mostra_elementi(age)
    elif ask == "2":
        age = aggiungi_elemento(age)
    elif ask == "3":
        age = modifica_elemento(age)
    elif ask == "4":
        age = cancella_elemento(age)
    elif ask == "5":
        try:
            ask2 = input("Sei sicuro(si/n)? ")
        except:
            ask2 = 0
        if ask2 == "si":
            svuota_dizionario("agenda.dat")
        else:
            print("Operazione annullata")
    
        ages = json.dumps(age)
        filages = open("agenda.dat", "w")
        filages.write(ages)
        filages.close()
    else:
        exit()
lista = []
#for li in range(0, len(age.keys())):
lista.append(age)
print(lista)