from os import environ

API_ID = int(environ.get("API_ID", "28713982"))
API_HASH = environ.get("API_HASH", "237e15f7c006b10b4fa7c46fee7a5377")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002100963256"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002100963256"))
ADMINS = int(environ.get("ADMINS", "7195990500 5512860435"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
