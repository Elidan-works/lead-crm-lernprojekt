import json

leads = [
    {"firmenname": "Musterfirma", "budget": 17000},
    {"firmenname": "Beispiel AG", "budget": 4000},
]

with open("leads.json", "w") as datei:
    json.dump(leads, datei, indent=2)

with open("leads.json", "r") as datei:
    geladene_leads = json.load(datei)

print(geladene_leads)
print(geladene_leads[0]["budget"])