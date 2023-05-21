import psycopg2

conn = psycopg2.connect(
    database="postgres",
    host="localhost",
    user="postgres",
    password="password",
    port="5433"
)

cur = conn.cursor()

cur.execute("SELECT * FROM gnaf_202302.address_principals WHERE postcode = '2305' LIMIT 1000")

rows = cur.fetchall()

addresses = []

for row in rows:
    address = {}
    address["name"] = f"{row[15]} {row[16]} {row[17]}"
    address["location"] = [row[24], row[25]]
    addresses.append(address)