import urllib.parse
import json


def headers():
    headers = {
        "Accept": "application/json; indent=2",
        "Origin": "https://lfg.supermeow.vip",
        "Referer": "https://lfg.supermeow.vip/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    return headers


def retrieve_user_id(encoded_string):
    # Decode the URL-encoded string
    decoded_string = urllib.parse.unquote(encoded_string)

    # Load the JSON structure from the decoded string
    data = json.loads(decoded_string)

    # The 'user' field is itself a JSON-encoded string, so we need to decode it again
    user_data = json.loads(data["user"])

    # Extract the user id
    user_id = user_data["id"]

    return user_id


def retrieve_user_info(encoded_string):
    # Decode the URL-encoded string
    decoded_string = urllib.parse.unquote(encoded_string.replace("+", " "))

    # Load the JSON structure from the decoded string
    data = json.loads(decoded_string)

    # The 'user' field is itself a JSON-encoded string, so we need to decode it again
    user_data = json.loads(data["user"])

    # Return the user data as a dictionary
    return {"user": user_data}
