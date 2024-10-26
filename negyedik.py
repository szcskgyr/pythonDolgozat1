import math

def valosSzamBeolvas():
    szam = float(input("Kérlek, adj meg valós számot: "))
    return szam

def negyedik():
    szam = valosSzamBeolvas()
    szam = math.floor(szam)
    print("Kerekített értéke: "+str(szam))