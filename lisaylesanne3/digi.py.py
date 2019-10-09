try:
    arv = int(input("Sisesta arv (täisarv): "))
    if arv >= 0 and arv <= 9999:
        pass
    else:
        raise Exception
except:
    print("Arv peab olema 0 kuni 9999 vahemikus!")
    quit()

try:
    suurus = int(input("Sisesta suurus (täisarv): "))
    if suurus >= 1 and suurus <= 8:
        pass
    else:
        raise Exception
except:
    print("Suurus peab olema 1 kuni 8 vahemikus!")
    quit()

number = [
    # X 1 X
    # 2 X 3
    # X 4 X
    # 5 X 6
    # X 7 X
    
    #1  2  3  4  5  6  7
    [1, 1, 1, 0, 1, 1, 1], # 0
    [0, 0, 1, 0, 0, 1, 0], # 1
    [1, 0, 1, 1, 1, 0, 1], # 2
    [1, 0, 1, 1, 0, 1, 1], # 3
    [0, 1, 1, 1, 0, 1, 0], # 4
    [1, 1, 0, 1, 0, 1, 1], # 5
    [1, 1, 0, 1, 1, 1, 1], # 6
    [1, 0, 1, 0, 0, 1, 0], # 7
    [1, 1, 1, 1, 1, 1, 1], # 8
    [1, 1, 1, 1, 0, 1, 1]  # 9
    ]

def j_number(nr, s):
    sõne = ""
    
    # esimene rida -> 1
    if number[nr][0] == 1:
        sõne += (" " + ("-" * s) + " " + "#")
    else:
        sõne += (" " + (" " * s) + " " + "#")
    
    for k in range(s):
        # teine rida -> 2 ja 3
        if number[nr][1] == 1 and number[nr][2] == 1:
            sõne += ("|" + (" " * s) + "|" + "#")
        elif number[nr][1] == 0 and number[nr][2] == 1:
            sõne += (" " + (" " * s) + "|" + "#")
        elif number[nr][1] == 1 and number[nr][2] == 0:
            sõne += ("|" + (" " * s) + " " + "#")
        else:
            sõne += (" " + (" " * s) + " " + "#")
    
    # kolmas rida -> 4
    if number[nr][3] == 1:
        sõne += (" " + ("-" * s) + " " + "#")
    else:
        sõne += (" " + (" " * s) + " " + "#")
    
    for k in range(s):
        # neljas rida -> 5 ja 6
        if number[nr][4] == 1 and number[nr][5] == 1:
            sõne += ("|" + (" " * s) + "|" + "#")
        elif number[nr][4] == 0 and number[nr][5] == 1:
            sõne += (" " + (" " * s) + "|" + "#")
        elif number[nr][4] == 1 and number[nr][5] == 0:
            sõne += ("|" + (" " * s) + " " + "#")
        else:
            sõne += (" " + (" " * s) + " " + "#")
    
    # viies rida -> 7
    if number[nr][6] == 1:
        sõne += (" " + ("-" * s) + " " + "#")
    else:
        sõne += (" " + (" " * s) + " " + "#")
    
    return sõne

if arv > 999:
    esimene = j_number(int(str(arv)[0]), suurus).split("#")
    teine = j_number(int(str(arv)[1]), suurus).split("#")
    kolmas = j_number(int(str(arv)[2]), suurus).split("#")
    neljas = j_number(int(str(arv)[3]), suurus).split("#")
    for x in range(suurus + suurus + 3):
        print(esimene[x] + (" " * suurus) + teine[x] + (" " * suurus) + kolmas[x] + (" " * suurus) + neljas[x])
elif arv > 99:
    esimene = j_number(int(str(arv)[0]), suurus).split("#")
    teine = j_number(int(str(arv)[1]), suurus).split("#")
    kolmas = j_number(int(str(arv)[2]), suurus).split("#")
    for x in range(suurus + suurus + 3):
        print(esimene[x] + (" " * suurus) + teine[x] + (" " * suurus) + kolmas[x])
elif arv > 9:
    esimene = j_number(int(str(arv)[0]), suurus).split("#")
    teine = j_number(int(str(arv)[1]), suurus).split("#")
    for x in range(suurus + suurus + 3):
        print(esimene[x] + (" " * suurus) + teine[x])
else:
    esimene = j_number(int(str(arv)[0]), suurus).split("#")
    for x in range(suurus + suurus + 3):
        print(esimene[x])