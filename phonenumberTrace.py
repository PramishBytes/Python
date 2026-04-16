import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from typing import Optional, Dict, Any

# ==============================
# CONFIG
# ==============================
NUMVERIFY_API_KEY = "YOUR_NUMVERIFY_API_KEY"
OPENCELLID_API_KEY = "YOUR_OPENCELLID_API_KEY"


# ==============================
# PHONE NUMBER UTILITIES
# ==============================
def parse_phone_number(number: str) -> Optional[phonenumbers.PhoneNumber]:
    try:
        return phonenumbers.parse(number)
    except phonenumbers.NumberParseException:
        return None


def get_number_details(number: str) -> Dict[str, Any]:
    parsed = parse_phone_number(number)
    if not parsed:
        return {"error": "Invalid phone number format"}

    is_valid = phonenumbers.is_valid_number(parsed)
    is_possible = phonenumbers.is_possible_number(parsed)

    result = {
        "input": number,
        "valid": is_valid,
        "possible": is_possible,
        "country_code": parsed.country_code,
        "national_number": parsed.national_number,
    }

    if is_valid:
        result.update({
            "location": geocoder.description_for_number(parsed, "en"),
            "carrier": carrier.name_for_number(parsed, "en"),
            "timezones": list(timezone.time_zones_for_number(parsed)),
        })

    return result


# ==============================
# IP LOOKUP
# ==============================
def get_location_from_ip(ip_address: str) -> Dict[str, Any]:
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") != "success":
            return {"error": data.get("message")}

        return {
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "isp": data.get("isp"),
            "timezone": data.get("timezone"),
        }

    except requests.RequestException as e:
        return {"error": str(e)}


# ==============================
# REVERSE LOOKUP
# ==============================
def reverse_phone_lookup(number: str) -> Dict[str, Any]:
    parsed = parse_phone_number(number)
    if not parsed:
        return {"error": "Invalid phone number"}

    url = "http://api.numverify.com/validate"
    params = {
        "phone": parsed.national_number,
        "country_code": parsed.country_code,
        "access_key": NUMVERIFY_API_KEY,
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        return {
            "valid": data.get("valid"),
            "type": data.get("line_type"),
            "carrier": data.get("carrier"),
            "location": data.get("location"),
        }

    except requests.RequestException as e:
        return {"error": str(e)}


# ==============================
# CELL TOWER LOOKUP
# ==============================
def get_cell_tower_location(mcc: int, mnc: int, lac: int, cell_id: int) -> Dict[str, Any]:
    url = "https://opencellid.org/cell/get"
    params = {
        "mcc": mcc,
        "mnc": mnc,
        "lac": lac,
        "cellid": cell_id,
        "key": OPENCELLID_API_KEY,
        "format": "json",
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        return {
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "accuracy": data.get("accuracy"),
        }

    except requests.RequestException as e:
        return {"error": str(e)}


# ==============================
# MAIN
# ==============================
def main():
    phone_number = "+918307317535"  # Add your number to try or someone else to find

    print("\n=== PHONE DETAILS ===")
    print(get_number_details(phone_number))

    print("\n=== REVERSE LOOKUP ===")
    print(reverse_phone_lookup(phone_number))

    # Optional
    # print("\n=== IP LOOKUP ===")
    # print(get_location_from_ip("8.8.8.8"))

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()