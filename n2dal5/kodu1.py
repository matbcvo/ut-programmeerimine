import re

samm = 0
kasutajannimi = ""
parool = ""
parool2 = ""

while True:
    if samm is 0: # Küsi kasutajanimi
        kasutajanimi = input("Palun sisesta kasutajanimi: ")
        samm = 1
    elif samm is 1: # Küsi kasutajalt parool esimest korda
        parool = input("Palun sisesta parool: ")
        samm = 2
    elif samm is 2: # Küsi kasutajalt parool teist korda
        parool2 = input("Palun sisesta uuesti parool: ")
        samm = 3
    elif samm is 3: # Kas esimene parool kattub teise parooliga?
        if parool == parool2:
            # print("Esimene parool kattub teise parooliga.")
            samm = 4
        else:
            print("Esimene parool ei kattu teise parooliga!")
            samm = 1
    elif samm is 4: # Kas sõne on vähemalt 8 tähemärki pikk?
        if len(parool) >= 8:
            # print("Parool on vähemalt 8 tähemärki pikk.")
            samm = 5
        else:
            print("Parool ei ole vähemalt 8 tähemärki pikk!")
            samm = 1
    elif samm is 5: # Kas sõnes on kasutatud nii tähti kui numbreid?
        #if parool.isalnum() is True and parool.isnumeric() is False and parool.isalpha() is False:
        if re.search('[A-Za-z]', parool) and re.search('[0-9]', parool):
            # print("Paroolis on kasutatud nii tähti kui numbreid.")
            samm = 6
        else:
            print("Paroolis ei ole kasutatud nii tähti kui numbreid!")
            samm = 1
    elif samm is 6: # Pööra parool tagurpidi (vaese mehe krüptograafia)
        parool = parool[::-1]
        # print(parool)
        samm = 7
    elif samm is 7: # Kirjuta kasutajanimi ja parool faili users.txt kujul: kasutajanimi:loorap
        with open("users.txt", "a") as fail:
            fail.write(kasutajanimi + ":" + parool)
            # print("Kasutajanimi ja parool on kirjutatud users.txt faili.")
        break