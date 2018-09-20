import json
import sqlite3
from flask import Flask, request, jsonify
from utils import json_response, JSON_MIME_TYPE


app = Flask(__name__)


@app.route('/invoice')
def invoice_list():
    con = sqlite3.connect('billing.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM invoice')
    invoices = [{
        'invoiceId': row[0],
        'customerId': row[1],
        'firstname': row[2],
	'lastname': row[3],
        'city': row[4],
	'country': row[5],
	'amount': row[6]
    } for row in cur.fetchall()]

    return json_response(jsonify(invoices))

@app.route('/invoice',methods = ['POST'])
def invoice_create():
   if request.method == 'POST':
      data = request.json
      try:
         invoiceId = data['invoiceId']
         customerId = data['customerId']
         firstname = data['firstname']
         lastname = data['lastname']
	 city = data['city']
	 country = data['country']
	 amount = data['amount']
         
         with sqlite3.connect('billing.db') as con: cur = con.cursor()
            
         cur.execute("INSERT INTO invoice (invoiceId,customerId,firstname,lastname,city,country,amount)VALUES (?,?,?,?,?,?,?)",(invoiceId,customerId,firstname,lastname,city,country,amount))
            
         con.commit()

      except:
         con.rollback()

      
      finally:
         
       return json_response(jsonify(request.json))
       con.close()


if __name__ == '__main__':
    app.run(debug=True)
