import psycopg2

verbindung = psycopg2.connect(
    dbname="lead_crm",
    user="muda2907",
    host="localhost",
    port="5432"
)

print("Verbindung erfolgreich!")

cursor = verbindung.cursor()
cursor.execute("SELECT * FROM leads;")
ergebnis = cursor.fetchall()

for zeile in ergebnis:
    print(f"{zeile[1]}: {zeile[2]} Euro ({zeile[3]})")

cursor.execute(
    "INSERT INTO leads (firmenname, budget, status) VALUES (%s, %s, %s);",
    ("Testkunde Gmbh", 800, "kalt")
)
verbindung.commit()