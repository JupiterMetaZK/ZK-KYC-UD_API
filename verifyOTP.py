import requests
import json

def OTPGenerate(url, consent, reference_id, purpose, transaction_id, OTP):
    # Read credentials from JSON file
    with open('creds.json') as f:
        creds = json.load(f)
    
    payload = {
        "consent": consent,
        "generate_pdf": False,
        "generate_xml": True,
        "reference_id": reference_id,
        "purpose": purpose,
        "initiation_transaction_id": transaction_id,
        "otp": OTP
    }
    headers = {
        "accept": "application/json",
        "client_id": creds.get("CLIENT_ID"),
        "client_secret": creds.get("CLIENT_SECRET"),
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()