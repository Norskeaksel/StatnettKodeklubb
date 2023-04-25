import sys
import math

startPosisjon = ""
spor = [[0]*15 for i in range(15)]
kart = []
har_flyttet = False
torpedo_kraft = 3
def start_spill():
    width, height, my_id = [int(i) for i in input().split()]

    for i in range(height):
        rad = input()
        kart.append(rad) 
        print(rad, file=sys.stderr, flush=True)
    for y, rad in enumerate(kart):
        for x, kolonne in enumerate(rad):
            if kolonne == '.':
                print(x, y, end="")
                spor[y][x] = 1
                global startPosisjon
                startPosisjon = str(x) + str(y)
                return

def flytt_opp_hvis_mulig():
    global har_flyttet
    if y> 0 and kart[y-1][x]=='.' and spor[y-1][x] == 0 and har_flyttet == False:
        print("MOVE N TORPEDO", end="")
        har_flyttet = True
        spor[y-1][x] = 1

def flytt_ned_hvis_mulig():
    global har_flyttet
    if y<14 and kart[y+1][x] == '.' and spor[y+1][x] == 0 and har_flyttet == False:
        print("MOVE S TORPEDO", end="")
        har_flyttet = True
        spor[y+1][x] = 1

def flytt_venstre_hvis_mulig():
    global har_flyttet
    if x>0 and kart[y][x-1] == '.' and spor[y][x-1] == 0 and har_flyttet == False:
        print("MOVE W TORPEDO", end="")
        har_flyttet = True
        spor[y][x-1] = 1

def flytt_hoyre_hvis_mulig():
    global har_flyttet
    if x<14 and kart[y][x+1] == '.' and spor[y][x+1] == 0 and har_flyttet == False:
        print("MOVE E TORPEDO", end="")
        har_flyttet = True
        spor[y][x+1] = 1

def fjern_spor_hvis_man_ikke_har_flyttet(x,y):
    global har_flyttet
    global spor 
    if har_flyttet == False:
        print("| SURFACE |", end="")
        spor = [[0]*15 for i in range(15)]
        spor[y][x] = 1
    
def skyt_torpedo_hvis_mulig(tx, ty, torpedo_cooldown):
    if torpedo_cooldown == 0:
        print("|TORPEDO",tx,ty,"|", end="")


def xy_posisjon():
    x, y, my_life, opp_life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown = [int(i) for i in input().split()]
    sonar_result = input()
    opponent_orders = input()
    return (x,y, torpedo_cooldown)

def har_gjort_ett_trekk(x,y):
    global startPosisjon
    xy = str(x)+str(y)
    if xy != startPosisjon:
        print("MSG Du klarte oppgave 0! | Vellykket flytt")

def har_kommmet_seg_til_sektor9(x, y):
    if x >= 10 and y >= 10:
        print("MSG Du klarte oppgave 1! | Har ankommet sektor 9!")

def har_overlevd_i_60_trekk(trekk):
    if(trekk>=60):
        print("MSG Du klarte oppgave 2! | Har overlevd i 60 trekk!")

def har_vunnet_over_motstanderen_med_torpedoer():
    pass

start_spill()
for trekk_nr in range(1000):
    print()
    x,y,torpedo_cooldown = xy_posisjon()
    har_flyttet = False
    # Oppgaver. De kan kommenteres ut når de er løst med "#" 

    har_gjort_ett_trekk(x, y) # Oppgave 0
    har_kommmet_seg_til_sektor9(x,y) # Oppgave 1
    har_overlevd_i_60_trekk(trekk_nr) # Oppgave 2
    har_vunnet_over_motstanderen_med_torpedoer() # Oppgave 3

    # Din kode her 
