import base64
import requests
from datetime import datetime
from django.conf import settings


def format_phone(phone):
    phone = str(phone).strip().replace(" ", "")

    if phone.startswith("+254"):
        phone = phone[1:]
    elif phone.startswith("07"):
        phone = "254" + phone[1:]
    elif phone.startswith("01"):
        phone = "254" + phone[1:]
    elif phone.startswith("7") or phone.startswith("1"):
        phone = "254" + phone

    return phone


def get_access_token():
    url = (
        "https://sandbox.safaricom.co.ke/oauth/v1/generate"
        "?grant_type=client_credentials"
    )

    response = requests.get(
        url,
        auth=(
            settings.MPESA_CONSUMER_KEY,
            settings.MPESA_CONSUMER_SECRET,
        ),
        timeout=30,
    )

    print("=" * 60)
    print("ACCESS TOKEN STATUS:", response.status_code)
    print("ACCESS TOKEN RESPONSE:", response.text)
    print("=" * 60)

    response.raise_for_status()

    return response.json()["access_token"]


def stk_push(phone, amount):

    phone = format_phone(phone)

    access_token = get_access_token()

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    password = base64.b64encode(
        (
            settings.MPESA_SHORTCODE
            + settings.MPESA_PASSKEY
            + timestamp
        ).encode()
    ).decode()

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": phone,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "Buy Me Coffee",
        "TransactionDesc": "Support Japhet Cheremo",
    }

    print("=" * 60)
    print("ACCESS TOKEN:", access_token)
    print("TIMESTAMP:", timestamp)
    print("PHONE:", phone)
    print("PAYLOAD:", payload)
    print("=" * 60)

    response = requests.post(
        "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
        json=payload,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        timeout=30,
    )

    print("=" * 60)
    print("STK STATUS:", response.status_code)
    print("STK RESPONSE:", response.text)
    print("=" * 60)

    response.raise_for_status()

    return response.json()