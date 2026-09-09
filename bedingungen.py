lead = {
    "firmenname": "Musterfirma 123",
    "budget": 8200
}

if lead["budget"] > 10000:
    meldung = "Heißer Lead,sofort an Vertrieb"
elif lead["budget"] >= 3000:
    meldung = "Warmer Lead,Follow-up einplanen"
else:
    meldung = "Kalter Lead,Newsletter"

print(f"{lead["firmenname"]} {meldung}")