def arvutaHinnad(hinnad, juurdehindlus):
    uued_hinnad = []
    for x in hinnad:
        uus_hind = x + x * (juurdehindlus / 100)
        uus_hind = uus_hind + uus_hind * 0.2
        uued_hinnad.append(uus_hind)
    return uued_hinnad

print(arvutaHinnad([100.0, 1200.0], 10.0))