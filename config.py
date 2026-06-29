import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SPREADSHEET_ID = "1Z6pd55Shd5kNBGkSGqBRENoDkOKYCeVbVz9nwubAnFs"

MASTER_SHEET = "MASTER SHEET 26-27"

# Local PC → use local file
# Render → use Secret File mounted at /etc/secrets/service_account.json
if os.path.exists("/etc/secrets/service_account.json"):
    SERVICE_ACCOUNT = "/etc/secrets/service_account.json"
else:
    SERVICE_ACCOUNT = os.path.join(BASE_DIR, "service_account.json")