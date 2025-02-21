from pathlib import Path
from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
# from saml2.saml import NAME_FORMAT_BASIC


BASE_DIR = Path(__file__).resolve().parent
BASE = "http://localhost:54321"

SAML2_IDP_CONFIG = {
    "entityid": "http://localhost:54321",
    "name": "Test IdP",
    "service": {
        "idp": {
            "endpoints": {
                "single_sign_on_service": [
                    (f"{BASE}/sso", BINDING_HTTP_POST),
                    (f"{BASE}/redirect", BINDING_HTTP_REDIRECT)],
                "single_logout_service": [
                    (f"{BASE}/slop", BINDING_HTTP_POST)]
            },
        },
    },
    "debug": 0,
    "key_file": f"{BASE_DIR}/private.key",
    "cert_file": f"{BASE_DIR}/public.cert",
    # "xmlsec_binary": xmlsec_path,
    "metadata": [],
    # "attribute_map_dir": full_path("attributemaps"),
    "organization": {
        "name": "Exempel AB",
        "display_name": [("Exempel AB", "se"), ("Example Co.", "en")],
        "url": "http://www.example.com/roland",
    },
    "contact_person": [
        {
            "given_name": "John",
            "sur_name": "Smith",
            "email_address": ["john.smith@example.com"],
            "contact_type": "technical",
        },
    ],
}
