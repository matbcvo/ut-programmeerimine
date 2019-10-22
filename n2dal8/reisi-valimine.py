def loetleReisid(failinimi, eelarve):
    reisid = []
    with open(failinimi, encoding="utf-8") as f:
        for rida in f:
            reis = rida.replace("\n", "").split(";")
            if float(reis[1]) <= float(eelarve):
                reisid.append(reis[0])
    return reisid

eelarve = float(input("Sisesta sobiv reisi eelarve: "))
print("Sobivaid reisid on:")
for x in range(len(loetleReisid('reisid.txt', eelarve))):
    print(loetleReisid('reisid.txt', eelarve)[x])
    