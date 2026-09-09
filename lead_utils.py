def qualifiziere_lead(budget):
    if budget > 10000:
        return "heiß"
    elif budget >= 3000:
        return "warm"
    else:
        return "kalt"

def formatiere_euro(betrag):
    return f"{betrag:,.0f} €"