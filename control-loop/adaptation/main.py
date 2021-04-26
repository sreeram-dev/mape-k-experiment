import os

from adaptation.app import app
from adaptation import routes

## Strict https

if __name__ == '__main__':
    if not app.config['DEBUG']:
        PORT = int(os.environ.get('PORT', 8080))
        app.run(host='0.0.0.0', port=PORT)
    elif app.config['DEBUG']:
        app.run(host='127.0.0.1', port=8080)
