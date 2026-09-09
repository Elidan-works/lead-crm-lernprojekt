def qualifiziere_lead(budget):
    if budget > 10000:
        return "heiß"
    elif budget >= 3000:
        return "warm"
    else:
        return "kalt"

leads = [
    {"firmenname": "Musterfirma", "budget": 17000},
    {"firmenname": "Beispiel AG", "budget": 4000},
    {"firmenname": "Sample GmbH", "budget": 8000},
    {"firmenname": "Everything KG", "budget": 1800},
    {"firmenname": "Elidan", "budget": 67000}
]

for lead in leads:
    ergebnis = qualifiziere_lead(lead["budget"])
    print(f"{lead['firmenname']}: {ergebnis}")

def formatiere_euro(betrag):
    return f"{betrag:,.0f} €"
print(formatiere_euro(12000))

