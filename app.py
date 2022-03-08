raeume = []
raumgroeßen = []
raumzahl = int(input("Wieviele Räume gibt es?\n"))
while raumzahl > 0:
    tempinput = int(input("1:Neuen Raum hinzufügen? \n2:Raumliste anzeigen\n"))
    if tempinput == 1:
        raumname = str(input("Bitte gib den Raumnamen an.\n"))
        raeume.append(raumname)
        viereck = str(input("Ist der Raum ein Viereck? [y/n]\n"))
        if viereck == "y":
            quadrat = str(input("Ist der Raum quadratisch? [y/n]\n"))
            if quadrat == "y":
                length = float(input("Wandlänge?\n"))
                length = length * 4
                raeume.append(length)
                raumgroeßen.append(length)
                print(length)
                raumzahl -= 1
            else:
                wallA = float(input("Gib die Länge von Wand A an\n"))
                wallB = float(input("Gib die Länge von Wand B an\n"))
                flaeche = wallA * wallB
                raeume.append(flaeche)
                raumgroeßen.append(flaeche)
                print (flaeche)
                raumzahl -= 1
        else:
            bigA = float(input("Größte Wandlänge? \n"))
            bigB = float(input("Größte Wandbreite?\n"))
            smallA = float(input("Kleinste Wandlänge?\n"))
            smallB = float(input("Kleinste Wandbreite?\n"))
            flaecheA = bigA * bigB
            flaecheB = smallA * smallB
            flaeche = flaecheA - flaecheB
            raeume.append(flaeche)
            raumgroeßen.append(flaeche)
            print (flaeche)
            raumzahl -= 1
    elif tempinput == 2:
        if len(raeume) > 0:
            print(raeume)
        else:
            print("Keine Räume vorhanden!") 
print (raeume)
print ("Summe aller Räume: ", float(sum(raumgroeßen)))