import requests

import uuid

from generateOTP import OTPGenerate as generate_otp
from verifyOTP import OTPGenerate as verify_otp


url_OTP = "https://in.staging.decentro.tech/v2/kyc/aadhaar/otp"
url_OTP_verify = "https://in.staging.decentro.tech/v2/kyc/aadhaar/otp/validate"


def main():
    aadhaar_number = input("Enter Aadhaar number: ")
    consent = True  # Assuming consent is always true for this example
    reference_id = str(uuid.uuid4())  # Generate a unique reference ID
    purpose = "FOR USER KYC Verification"  # Define the purpose

    # Generate OTP
    otp_response = generate_otp(url_OTP, consent, reference_id, purpose, aadhaar_number)
    print("OTP Generation Response:", otp_response)

    # Assuming the response contains a transaction ID (decentroTxnId)
    decentroTxnId = otp_response.get("decentroTxnId")
    if not decentroTxnId:
        print("Error: Transaction ID not found in OTP generation response.")
        return

    # Verify OTP
    otp = input("Enter the OTP received: ")
    verify_response = verify_otp(url_OTP_verify, consent, reference_id, purpose, decentroTxnId, otp)
    print("OTP Verification Response:", verify_response)

if __name__ == "__main__":
    main()