from pykkar import *
import math
import random

samm = 0

# pykkar maailm
#  ______________
# |              |^ y
# |              | b külg 
# |______________|
#      a külg     > x

while (True):
    if samm is 0: # Küsin maailma külje A pikkust
        try:
            maailma_külg_a = int(input("Sisesta maailma ühe külje pikkus: "))
            if maailma_külg_a >= 3:
                if maailma_külg_a & 1:
                    samm = 1
                else:
                    print("Maailma külje pikkus peab olema paaritu arv!")
            else:
                print("Maailma külje pikkus peab olema vähemalt 3!")
        except:
            print("Vigane sisend! Proovime uuesti...")
    elif samm is 1: # Küsin maailma külje B pikkust
        try:
            maailma_külg_b = int(input("Sisesta maailma teise külje pikkus: "))
            if maailma_külg_b >= 3:
                if maailma_külg_b & 1:
                    samm = 2
                else:
                    print("Maailma külje pikkus peab olema paaritu arv!")
            else:
                print("Maailma külje pikkus peab olema vähemalt 3!")
        except:
            print("Vigane sisend! Proovime uuesti...")
    elif samm is 2: # Küsin pykkari x koordinaati
        try:
            pykkar_pos_x = int(input("Sisesta pykkari x positsioon: "))
            if pykkar_pos_x < maailma_külg_b and pykkar_pos_x > 1:
                samm = 3
            else:
                print("Pykkari x-koordinaat ei tohi olla väiksem kui 2 ja suurem kui " + str(maailma_külg_b-1) + ".")
        except:
            print("Vigane sisend! Proovime uuesti...")
    elif samm is 3: # Küsin pykkari y koordinaati
        try:
            pykkar_pos_y = int(input("Sisesta pykkari y positsioon: "))
            if pykkar_pos_y < maailma_külg_a and pykkar_pos_y > 1:
                samm = 4
            else:
                print("Pykkari y-koordinaat ei tohi olla väiksem kui 2 ja suurem kui " + str(maailma_külg_a-1) + ".")
        except:
            print("Vigane sisend! Proovime uuesti...")
    elif samm is 4: # Küsin pykkari suunda
        pykkar_suund = input("Sisesta pykkari suund: ").upper()
        ilmakaared = ["N", "E", "S", "W"]
        if pykkar_suund in ilmakaared:
            samm = 5
        else:
            print("Vigane sisend! Proovime uuesti...")
    elif samm is 5:
        print("Maailma külje A pikkus on " + str(maailma_külg_a))
        print("Maailma külje B pikkus on " + str(maailma_külg_b))
        print("Pykkar X on " + str(pykkar_pos_x))
        print("Pykkar Y on " + str(pykkar_pos_y))
        print("Pykkar suund on " + str(pykkar_suund))
        break

maailm = ""

for i in range(maailma_külg_a):
    for j in range(maailma_külg_b):
        if j == pykkar_pos_x-1 and i == pykkar_pos_y-1:
            if pykkar_suund == "W":
                maailm += ">"
            elif pykkar_suund == "E":
                maailm += "<"
            elif pykkar_suund == "N":
                maailm += "^"
            elif pykkar_suund == "S":
                maailm += "v"
        elif i == 0 or j == 0 or i == maailma_külg_a-1 or j == maailma_külg_b-1:
            maailm += "#"
        else:
            maailm += " "
        if j == maailma_külg_b-1:
            maailm += "\n"

print(maailm)

create_world(maailm)

keskkoht_x = math.ceil((maailma_külg_b) / 2)
keskkoht_y = math.ceil((maailma_külg_a) / 2)

print("Keskkoha X on " + str(keskkoht_x))
print("Keskkoha Y on " + str(keskkoht_y))

def sea_suund(suund):
    while (True):
        if get_direction() == suund:
            break
        right()

def liigu():
    global pykkar_pos_y
    global pykkar_pos_x
    if get_direction() == "W":
        pykkar_pos_x -= 1
    elif get_direction() == "E":
        pykkar_pos_x += 1
    elif get_direction() == "N":
        pykkar_pos_y -= 1
    elif get_direction() == "S":
        pykkar_pos_y += 1
    step()


while (True):
    print("pykkar X: " + str(pykkar_pos_x) + " keskkoht X: " + str(keskkoht_x))
    print("pykkar Y: " + str(pykkar_pos_y) + " keskkoht Y: " + str(keskkoht_y))
    if pykkar_pos_x == keskkoht_x and pykkar_pos_y == keskkoht_y:
        paint()
        break
    if pykkar_pos_x != keskkoht_x:
        if pykkar_pos_x > keskkoht_x:
            sea_suund("W")
        elif pykkar_pos_x < keskkoht_x:
            sea_suund("E")
        liigu()
    if pykkar_pos_y != keskkoht_y:
        if pykkar_pos_y > keskkoht_y:
            sea_suund("N")
        elif pykkar_pos_y < keskkoht_y:
            sea_suund("S")
        liigu()