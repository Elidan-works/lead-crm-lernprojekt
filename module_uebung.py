import datetime
heute = datetime.date.today()

print(f"Angebot erstellt am: {heute}")

from lead_utils import qualifiziere_lead, formatiere_euro

leads = [
    {"firmenname": "Musterfirma", "budget": 17000},
    {"firmenname": "Beispiel AG", "budget": 4000},
    {"firmenname": "Sample GmbH", "budget": 8000},
    {"firmenname": "Everything KG", "budget": 1800},
    {"firmenname": "Elidan", "budget": 67000}]

for lead in leads:
    status = qualifiziere_lead(lead["budget"])
    budget_formatiert = formatiere_euro(lead["budget"])
    print(f"{lead['firmenname']}: {status}, {budget_formatiert} (Stand: {heute})")
    