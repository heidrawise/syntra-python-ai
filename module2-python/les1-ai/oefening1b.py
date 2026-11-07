# Manier 2: AI-autocomplete in je editor (Copilot): functie die het hoogste getal uit een lijst teruggeeft, zonder max()


def hoogste(getallen):
    if not getallen:
        return None  # Of geef een foutmelding als de lijst leeg is

    hoogste_waarde = getallen[0]

    for getal in getallen:
        if getal > hoogste_waarde:
            hoogste_waarde = getal

    return hoogste_waarde


print(hoogste([3, 17, 8, 2]))  # output: 17
