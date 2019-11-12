def seosta_lapsed_ja_vanemad(lapsed_txt, nimed_txt):
    lapsed = dict()
    with open(lapsed_txt) as fail:
        for rida in fail:
            #print(rida)
            veergud = rida.strip().split()
            lapsed.setdefault(veergud[1], [])
            lapsed[veergud[1]].append(veergud[0])
    #print(lapsed)

    nimed = dict()
    with open(nimed_txt) as fail:
        for rida in fail:
            veergud = rida.strip().split()
            nimed[veergud[0]] = veergud[1] + " " + veergud[2]
    #print(nimed)
    """
    for x in lapsed:
        print(nimi(x), end=": ")
        sõne = ""
        for y in lapsed[x]:
            sõne += nimi(y) + ", "
        print(sõne[:-2])
    """
    tulemus = dict()
    for x in lapsed:
        lapsevanemad = set()
        for y in lapsed[x]:
            lapsevanemad.add(nimed[y])
        tulemus.setdefault(nimed[x], [])
        tulemus[nimed[x]] = lapsevanemad
    return tulemus

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))