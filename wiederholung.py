def berechne_rabatt(bestellwert, kundentyp):
    if kundentyp == "stammkunde" and bestellwert >= 1000:
        rabatt = 15
    elif kundentyp == "stammkunde" and bestellwert < 1000:
        rabatt = 5
    elif kundentyp == "neukunde":
        rabatt = 10
    else:
        rabatt = 0
    return rabatt