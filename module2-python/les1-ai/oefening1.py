# De opdracht: Maak een functie `hoogste(getallen)` die het hoogste getal uit een lijst teruggeeft. Gebruik geen `max()` van Python. Schrijf de logica zelf.

# Manier 1: Copy-paste vanuit een chat-LLM (Gemini)
def hoogste(getallen):
    if not getallen:
        return None  # Of geef een foutmelding als de lijst leeg is

    hoogste_waarde = getallen[0]

    for getal in getallen:
        if getal > hoogste_waarde:
            hoogste_waarde = getal

    return hoogste_waarde


# Voorbeeldgebruik:
mijn_lijst = [4, 12, 7, 23, 8]
print(hoogste(mijn_lijst))  # Output: 23

print(hoogste([3, 17, 8, 2]))  # output: 17
