from lead_utils import qualifiziere_lead, formatiere_euro

import psycopg2

verbindung = psycopg2.connect(
    dbname="lead_crm",
    user="muda2907",
    host="localhost",
    port="5432"
)
cursor = verbindung.cursor()

cursor.execute("SELECT*FROM leads;")
leads = cursor.fetchall()

ausgewerte_leads = []

for lead in leads:
    status = qualifiziere_lead(lead[2])
    cursor.execute(
    "UPDATE leads SET status = %s WHERE id = %s;",
    (status, lead[0]))
    verbindung.commit()
    ausgewerte_leads.append(lead)

cursor.execute("SELECT * FROM leads;")
ergebnis = cursor.fetchall()

for zeile in ergebnis:
    print(f"{zeile[1]}: {zeile[2]} Euro ({zeile[3]})")

print(ausgewerte_leads)
