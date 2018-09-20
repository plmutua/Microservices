import os

from api_invoice import app


if __name__ == '__main__':
    app.debug = True
    app.config['DATABASE_NAME'] = 'billing.db'
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
