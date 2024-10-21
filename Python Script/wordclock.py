from gpiozero import Button

button = Button(3)
button.wait_for_press() #Das Programm läuft erst weiter wenn der Knopf gedrückt wird

from pi5neo import Pi5Neo
import time

strip = Pi5Neo('/dev/spidev0.0', 114, 800)

def anzeigen(): #Diese Funktion wird nacher in Dauerschleife Laufen um die Zeit immer zu Aktualisieren  
    def ListeVonLEDSanzeigen(arr): #Zeigt Liste der Nummern der LEDs an
        brightness = 255
        for i in range(len(arr)):
            strip.set_led_color(arr[i],brightness,brightness,brightness)
    
    #Listen der Nummern die es zum anzeigen der Wörter braucht
    esist = [112,111,109,108,107]
    fünf=[102,103,104,105]
    zehn=[90,91,92,93]
    viertel=[100,99,98,97,96,95,94]
    zwanzig=[89,88,87,86,85,84,83]
    vor=[79,80,81]
    nach=[69,70,71,72]
    halb=[77,76,75,74]
    stunden = [
        [65,64,63,62],
        [67,66,65,64],
        [34,33,32,31],
        [35,36,37,38],
        [26,27,28,29],
        [47,48,49,50,51],
        [57,58,59,60,61,62],
        [23,22,21,20],
        [42,41,40,39],
        [45,44,43,42],
        [24,25,26],
        [56,55,54,53,52]
               ]
    punkte = [[],[113],[101,113],[12,101,113],[0,12,101,113]]
    uhr = [16,17,18]
    ammorgen=[13,14,11,10,9,8,7,6]
    amabend=[13,14,1,2,3,4,5]

    t = time.localtime() #die Zeit wurde auf t gespeichert, t[3] ist die Stunde, t[4] die minute
        
    #minuten
    min= t[4] 
    punktmin = int(min%5) #gibt die Anzahl Punkte die Leuchten müssen für die Minutenanzeige 
    minute = int((min- (min%5))/5) #zahl zwischen 0-11
    minuten = [
        [],
        fünf+nach,
        zehn+nach,
        viertel+nach,
        zwanzig+nach,
        fünf+vor+halb,
        halb,
        fünf+nach+halb,
        zwanzig+vor,
        viertel+vor,
        zehn+vor,
        fünf+vor,
        ]
    
    #stunden
    stunde = t[3]
    def stundbe(h): #berechnet die Stunde die angezeigt werden muss: 13.25 -> 2, 23.30 -> 12, 00.15 -> 12
        if min>=25:
            h += 1
        if (h>12):
            h-= 12
        if (h==0):
            h =12
        return h-1
    
    #morgen oder abend
    moab=[]
    if 12 > stunde >= 5: #von 5.00 bis 11.59 -> am morgen
        moab = ammorgen
    if stunde> 18: #von 18.00 bis 23.59 -> am morgen
        moab =amabend
    
    strip.fill_strip(0,0,0) #strip Leer machen damit alte anzeigen nicht mehr angezeigt werden
    ListeVonLEDSanzeigen(esist)
    ListeVonLEDSanzeigen(minuten[minute])
    ListeVonLEDSanzeigen(punkte[punktmin])
    ListeVonLEDSanzeigen(stunden[stundbe(stunde)])
    if(minute==0):
        ListeVonLEDSanzeigen(uhr)
        if stunde==1 or stunde == 13: #bei "Ein Uhr" wird das "s" von eins gelöscht
            strip.set_led_color(62,0,0,0)
    ListeVonLEDSanzeigen(moab)
    strip.update_strip()


past_min = None

while True: #Dauerschleife: jedes mal wenn die minute ändert wird die Funktion ausgeführt
    t = time.localtime()
    now_min = t[4]
    if not past_min:
        past_min = now_min
        anzeigen()

    if now_min != past_min:
        anzeigen()

    past_min = now_min

    time.sleep(1.5)

while True: #Dauerschleife damit immer die Aktuelle uhrzeit lä
    anzeigen()
    time.sleep(1)
