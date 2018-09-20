from flask import make_response

JSON_MIME_TYPE = 'application/json'


def search_invoice(invoice, invoice_Id):
    for invoice in invoices:
        if invoice['invoiceId'] == invoice_Id:
            return invoice


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)
