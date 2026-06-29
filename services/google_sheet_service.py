import json
import tempfile
import os

if os.path.exists(SERVICE_ACCOUNT):

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT,
        SCOPES
    )

else:

    service_json = os.environ["GOOGLE_SERVICE_ACCOUNT"]

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        delete=False
    ) as f:

        f.write(service_json)

        temp_file = f.name

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        temp_file,
        SCOPES
    )