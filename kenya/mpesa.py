import base64
import requests
from datetime import datetime
from django.conf import settings


def format_phone(phone):
    """
    Convert phone numbers to 2547XXXXXXXX format.
    """

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

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,

        # For PayBill use CustomerPayBillOnline.
        # For a Till (Buy Goods), production integrations may instead use
        # CustomerBuyGoodsOnline if your setup supports it.
        "TransactionType": "CustomerPayBillOnline",

        "Amount": int(amount),

        "PartyA": phone,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone,

        "CallBackURL": settings.MPESA_CALLBACK_URL,

        "AccountReference": "Buy Me Coffee",
        "TransactionDesc": "Support Japhet Cheremo",
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30,
    )

    print("=" * 60)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)
    print("=" * 60)

    response.raise_for_status()

    result = response.json()

    if result.get("ResponseCode") != "0":
        raise Exception(result.get("errorMessage") or result.get("ResponseDescription") or "STK Push failed")

    return result