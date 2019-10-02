import textwrap

lähtefail = input("Palun sisesta lähtefaili nimi: ")
sihtfail = input("Palun sisesta sihtfaili nimi: ")
sf_realaius = int(input("Palun sisesta sihtfaili realaius: "))

with open(lähtefail, encoding="utf-8") as lf:
    sisu = lf.read().replace("\n", "")

print("Esialgses tekstis oli " + str(len(sisu)) + " tähemärki.")

sisu = ' '.join(sisu.split())

print("Lõplikus tekstis on " + str(len(sisu)) + " tähemärki.")

print("Tekstis on " + str(len(sisu.split())) + " sõna.")

msisu = textwrap.wrap(sisu, sf_realaius)

with open(sihtfail, "a") as sf:
    for x in range(len(msisu)):
        sf.write(msisu[x])
        if x is not len(msisu)-1:
            sf.write("\n")

print("Sihtfaili salvestati " +  str(len(msisu)) + " rida laiusega " + str(sf_realaius) + " tähemärki.")
