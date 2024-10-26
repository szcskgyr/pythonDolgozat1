def masodik():
    vegOsszeg = 10001
    kategoria = "ezüst kártyás"

    if kategoria == "arany kártyás":
        kedvezmeny = 10
    elif kategoria == "ezüst kártyás":
        kedvezmeny = 5
    elif kategoria == "bronz kártyás":
        kedvezmeny = 2
    elif kategoria == "VIP":
        kedvezmeny = 20
    else:
        kedvezmeny = 1

    if vegOsszeg > 10000:
        kedvezmeny = kedvezmeny + 5
        print("Akció: "+str(kedvezmeny)+"% kedvezményt kap ma! Nagy összegű vásárlás!")
    else:
        print("Akció: " + str(kedvezmeny) + "% kedvezményt kap ma!")