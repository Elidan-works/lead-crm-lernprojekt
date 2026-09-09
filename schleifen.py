offene_angebote = ["Musterfirma", "Beispiel AG", "Sample GmbH", "Everything KG", "Elindan"]

zaehler = 1
for firma in offene_angebote:
    print(f"Angebot {zaehler}: {firma}")
    zaehler += 1


leads = [
    {"firmenname": "Musterfirma", "budget": 17000},
    {"firmenname": "Beispiel AG", "budget": 4000},
    {"firmenname": "Sample GmbH", "budget": 8000},
    {"firmenname": "Everything KG", "budget": 1800},
    {"firmenname": "Elidan", "budget": 67000}
]
anzahl_heiß = 0
summe_warm = 0
for lead in leads:
    if lead["budget"] > 10000:
        meldung = "heiß"
        anzahl_heiß += 1
    elif lead["budget"] >= 3000:
        meldung = "warm"
        summe_warm += lead["budget"]
    else:
        meldung = "kalt"

    print(f"{lead["firmenname"]}: {meldung}")

print(f"Anzahl heiße Leads: {anzahl_heiß}")
print(f"Gesamtbudget warme Leads: {summe_warm} Euro")
