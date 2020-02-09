
def totDist(digg1, stopps, dists):
    tote = 0
    for i in range(digg1, digg1+stopps):
        tote += dists[i]
    return tote

thalLine = ["Sharn","Wroat","Hatheril","Sword Keep","Marketplace","Passage","Fairhaven","Thaliost"]
korrLine = ["Sharn","Wroat","Starilaskur","Sterngate","Zolanberg","Korranberg"]
flamLine = ["Sharn","Wroat","Starilaskur","Vathirond","Aruldusk","Sigilstar","Flamekeep"]
eastLine = ["Krona Peak","Irontown","Vulyar"]
karrLine = ["Korth","Rekkenmark","Atur","Vedykar","Fort Zombie","Gatherhold"]
westLine = ["Flamekeep","Sigilstar","Aruldusk","Vathirond","Starilaskur","Hatheril","Sword Keep","Marketplace","Passage","Fairhaven","Thaliost"]

thalDist = [212,735,184,331,322,461,620]
korrDist = [212,1007,396,260,271]
flamDist = [212,1007,315,342,164,470,620]
eastDist = [267,509]
karrDist = [128,146,248,256,323]
westDist = [620,470,164,342,356,184,331,322,461,620]

anotha = "yes"
while anotha == "yes":

    print("Enter 'list' if you need a list of all operating Lightning Rail Stations")

    stop1 = input("Please enter the first stop: ")

    if stop1 == "list":
        print("Stations in Aundair: Fairhaven, Marketplace, Passage")
        print("Stations in Breland: Hatheril, Sharn, Starilaskur, Sternagte, Sword Keep, Vathirond, Wroat")
        print("Stations in Karrnath: Atur, Fort Zombie, Irontown, Korth, Rekkenmark, Vedykar, Vulyar")
        print("Stations in the Mror Holds: Krona Peak")
        print("Stations in the Talenta Plains: Gatherhold")
        print("Stations in Thrane: Aruldusk, Flamekeep, Sigilstar, Thaliost")
        print("Stations in Zilargo: Korranberg, Zolanberg")
        stop1 = input("Please enter the first stop: ")

    stop2 = input("Please enter the second stop: ")

    if stop1 in thalLine and stop2 in thalLine:
        line = "Thaliost Line"
        dig1 = thalLine.index(stop1)
        dig2 = thalLine.index(stop2)
    elif stop1 in korrLine and stop2 in korrLine:
        line = "Korranberg Line"
        dig1 = korrLine.index(stop1)
        dig2 = korrLine.index(stop2)
    elif stop1 in flamLine and stop2 in flamLine:
        line = "Flamekeep Line"
        dig1 = flamLine.index(stop1)
        dig2 = flamLine.index(stop2)
    elif stop1 in eastLine and stop2 in eastLine:
        line = "Eastern Line"
        dig1 = eastLine.index(stop1)
        dig2 = eastLine.index(stop2)
    elif stop1 in karrLine and stop2 in karrLine:
        line = "Karrnath Line"
        dig1 = karrLine.index(stop1)
        dig2 = karrLine.index(stop2)
    elif stop1 in westLine and stop2 in westLine:
        line = "Flamekeep-Thaliost Line"
        dig1 = westLine.index(stop1)
        dig2 = westLine.index(stop2)
    else:
        print("Sorry, there is no way to travel between "+stop1+" and "+stop2+" via the Lightning Rail.")
        break

    if dig2 < dig1:
        dig1, dig2 = dig2, dig1
    stops = dig2 - dig1

    if line == "Thaliost Line":
        distance = totDist(dig1, stops, thalDist)
    elif line == "Korranberg Line":
        distance = totDist(dig1, stops, korrDist)
    elif line == "Flamekeep Line":
        distance = totDist(dig1, stops, flamDist)
    elif line == "Eastern Line":
        distance = totDist(dig1, stops, eastDist)
    elif line == "Karrnath Line":
        distance = totDist(dig1, stops, karrDist)
    elif line == "Flamekeep-Thaliost Line":
        distance = totDist(dig1, stops, westDist)

    print("\nThese stops are on the "+line+".")

    print("The distance between "+stop1+" and "+stop2+" is "+str(distance)+" miles. The travel time is "+str(round(distance/30,2))+" hours.")
    print("Steerage Fare: "+str(round(distance*0.03, 2)))
    print("Standard Fare: "+str(round(distance*0.2,2)))
    print("First Class Fare: "+str(round(distance*0.5,2)))

    anotha = input("Enter another ticket [yes/no]: ")