tee_pikkus = float(input("Sisesta tee pikkus (km): "))

taksod = [] # (takso nimi, sisseastumise hind, km hind)

with open("taksohinnad.txt", encoding="utf-8") as fail:
    for x in fail:
        takso = x.replace("\n", "").split(",")
        taksod.append((takso[0], takso[1], takso[2]))


if taksod:
    taksohind = []
    for x in range(len(taksod)):
        taksohind.append(float(taksod[x][1]) + (float(taksod[x][2]) * tee_pikkus))

    print("Kõige odavam on " + taksod[taksohind.index(min(taksohind))][0] + ".")
else:
    print("taksohinnad.txt on tühi")