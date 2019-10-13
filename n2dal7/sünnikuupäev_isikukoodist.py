def sünnikuupäev(isikukood):
    sugu = isikukood[:1]
    sünnipäev = isikukood[5:7]
    sünnikuu = isikukood[3:5]
    sünniaasta = isikukood[1:3]
    if sünnikuu == "01":
        sünnikuu = "jaanuar"
    elif sünnikuu == "02":
        sünnikuu = "veebruar"
    elif sünnikuu == "03":
        sünnikuu = "märts"
    elif sünnikuu == "04":
        sünnikuu = "aprill"
    elif sünnikuu == "05":
        sünnikuu = "mai"
    elif sünnikuu == "06":
        sünnikuu = "juuni"
    elif sünnikuu == "07":
        sünnikuu = "juuli"
    elif sünnikuu == "08":
        sünnikuu = "august"
    elif sünnikuu == "09":
        sünnikuu = "september"
    elif sünnikuu == "10":
        sünnikuu = "oktoober"
    elif sünnikuu == "11":
        sünnikuu = "november"
    elif sünnikuu == "12":
        sünnikuu = "detsember"
    if sugu == "1" or sugu == "2": # 1800...1899a sündinud
        sünniaasta = "18" + sünniaasta
    elif sugu == "3" or sugu == "4": # 1900...1999a sündinud
        sünniaasta = "19" + sünniaasta
    elif sugu == "5" or sugu == "6": # 2000...2099a sündinud
        sünniaasta = "20" + sünniaasta
    return (sünnipäev + ". " + sünnikuu + " " + sünniaasta)

print(sünnikuupäev('34501234215'))