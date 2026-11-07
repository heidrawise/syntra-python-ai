# Manier 3: Een agentic tool (GitHub Copilot CLI)


def hoogste(getallen):
    if not getallen:
        return None

    hoogste_waarde = getallen[0]

    for getal in getallen:
        if getal > hoogste_waarde:
            hoogste_waarde = getal

    return hoogste_waarde


print(hoogste([3, 17, 8, 2]))  # output: 17
