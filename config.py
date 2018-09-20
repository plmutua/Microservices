import sqlite3

conn = sqlite3.connect('billing.db')

c =conn.cursor()

#c.execute("""CREATE TABLE invoice(
#	invoiceId int,
#	customerId int,
#	firstname text,
#	lastname text,
#	city text,
#	country text,
#	amount int
 #         ) """)

c.execute("INSERT INTO invoice VALUES(001,7382,'Mary','Joseph', 'Nairobi','Kenya',2000)")
c.execute("INSERT INTO invoice VALUES(003,7282,'John','Doe', 'Skelleftea','Sweden', 7839)")
c.execute("INSERT INTO invoice VALUES(005,6372,'Anna','Montana','Lappeenranta','Finland',7489)")

conn.commit()

conn.close()
