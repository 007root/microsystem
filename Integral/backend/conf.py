
RATE = 10.0
MONGO = {
    "pang_db": {
        "name": "pang_db",
        "host": "127.0.0.1",
        "port": 27017,
    }
}

import mongoengine
for alias, attrs in MONGO.items():
    mongoengine.register_connection(alias, **attrs)
