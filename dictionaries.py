lead = {
    "name": "Musterfirma",
    "kontakt": "Max Mustermann",
    "budget": 10000,
    "status": "neu"
}

print(f"Firma {lead["name"]} hat den Status {lead["status"]}.")
lead["status"] = "qualifiziert"
print("Gesamtes Dictionary:", (lead))