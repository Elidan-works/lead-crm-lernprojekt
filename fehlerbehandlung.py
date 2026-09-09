leads = [
    {"firmenname": "Musterfirma", "budget": 17000},
    {"firmenname": "Beispiel AG"},
    {"firmenname": "Testkunde GmbH", "budget": 4000},
    {"firmenname": "Unklar KG", "budget": "unbekannt"}
]

for lead in leads:
    try:
        if lead["budget"] > 10000:
            print("heiß")
        else:
            print("nicht heiß")
    except KeyError:
        print("kein Budget hinterlegt")
    except TypeError:
        print("Budget-Wert ungültig")
        