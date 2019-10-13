def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for x in range(len(järjend)):
        #print(str(järjend[x])[-1])
        if järjend[x][-1] == "P":
            poisse += 1
        elif järjend[x][-1] == "T":
            tüdrukuid += 1
    return (poisse, tüdrukuid)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))