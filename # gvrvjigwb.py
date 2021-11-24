# gvrvjigwb
c = "si"

def isnotvalid(v):
    if v <= 0:    
        print("Le grandezze del poligono devono essere positive!")
        return 1
    else: 
        return 0

def area_rettangolo(w, h):
    risultato = 0
    risultato = w*h
    return risultato

def area_triangolo(w, h):
    risultato = 0
    risultato = w*h/2
    return risultato

def calcolo_cerchio():
    print("Inserisci dati conosciuti: ")
    r = int(input("Raggio: ") or 0)
    A = int(input("Area: ") or 0)
    C = int(input("Perimetro: ") or 0)
    print("che calcolo vuoi effettuare: ")
    print("1. Area")
    print("2. Raggio")
    print("3. Perimetro")
    t = int(input(": "))
    risultato = 0
    if t == 1:
        if r > 0:
            risultato = (r*r)*3.14
        elif C > 0:
            r = C/2*3.14
            risultato = (r*r)*3.14
    elif t == 2:
        if r > 0:
            risultato = (A**(1/2))/3.14
        elif C > 0:
            risultato = C/2*3.14
    elif t == 3:
        if r > 0:
            risultato = r*2*3.14
        elif A > 0:
            r = (A**(1/2))/3.14
            risultato = r*2*3.14
    return risultato

def calcola_aree():
    print("Seleziona la forma di cui calolare:")
    print("1. Rettangolo")
    print("2. Triangolo")
    print("3. Cerchio")
    f = int(input(": "))
    if f <= 2:
        a = int(input("Larghezza: "))
        l = int(input("Altezza: "))
        while isnotvalid(a) or isnotvalid(l):
            a = int(input("Larghezza: "))
            l = int(input("Altezza: "))
        if f == 1:
                area = area_rettangolo(a, l)
        elif f == 2:
                area = area_triangolo(a, l)
    elif f == 3:
            area = calcolo_cerchio()
    else:
        print("Operazione annullata")
    #if area != 0:
    print("Risultato: " + str(area))


calcola_aree()
while c == "si":
    c = input("Calcola un altra area? ")
    if c == "si" or c == "Si":
        calcola_aree()
    if c == "no" or c == "No":
        break
    
    
        




