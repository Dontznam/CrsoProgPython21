
def riempi(rt):
    rct = rt
    while len(rct) < 4:
        rct = rct + ("x")
    return rct
    
def conson(co):
    consonante = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consoom = ""
    for i in co:
        if i in consonante:
            consoom = consoom + co[co.index(i)]
    return consoom


def omen(ct):
    l = 0
    cdt = ""
    cdt = conson(ct)
    cdt = riempi(cdt)
    cdt = cdt[0:3]
    #for i in ct:
    #    if l < 3:
    #        if i in consonante:
    #            cdt = cdt + ct[ct.index(i)]
    #            l = l + 1
    return cdt

def nomen(nt):
    l = 0
    cnt = ""
    cnt = conson(nt)
    cnt = riempi(cnt)
    cnt = cnt[0] + cnt[2] + cnt[3]
    #for i in nt:
    #        if i in consonante:
    #            if l == 0 or l == 2 or l == 3:
    #                cnt = cnt + nt[nt.index(i)]
    #            l = l + 1
                
    return cnt

def cf():
    c = input("cognome: ")
    n = input("nome: ")
    se = ""
    while se != m or se  != n:
        se = input("inserire(m/f): ")
        se.lower()
    
    a = input("anno: ")
    if len(a) < 4:
        print("inserire anno completo(es 1999)")
        a = input("anno: ")

    m = int(input("mese: "))
    if m > 12 and m < 0:
        print("Mese non valido, vanno da 1(gen) a 12(dic)")
        m = int(input("mese: "))
    g = int(input("giorno:"))
    if g > 31 and g < 1:
        g = int(input("giorno:"))
    

    la = " ABCDEHLMPRST"
    cd = ""
    cd = cd + omen(c)
    cd = cd + nomen(n)
#    for i in n:
 #            if i in consonante:
 #                if l == 0 or l == 1 or l == 3:
 #                    cd = cd + n[n.index(i)]
 #                l = l + 1
    cd = cd + a[2:4]
    cd = cd + la[m]
    if se == "f":
        cd = cd + str((g + 40))
    else:
        if g > 10:
            cd = cd + str(g)
        else:
            cd = cd + "0" + str(g)
    cd = cd.upper()        
    print(cd)

cf()
