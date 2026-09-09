class Lead:
    def __init__(self, firmenname, budget):
        self.firmenname = firmenname
        self.budget = budget

    def qualifiziere(self):
        if self.budget > 10000:
            return "heiß"
        elif self.budget >= 3000:
            return "warm"
        else:
            return "kalt"

leads = [
    Lead("Musterfirma", 17000),
    Lead("Beispiel AG", 4000),
    Lead("Testkunde GmbH", 800),
]

for lead in leads:
    print(f"{lead.firmenname}: {lead.qualifiziere() }")
