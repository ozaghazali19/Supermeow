import requests

from smart_airdrop_claimer import base
from core.headers import headers, retrieve_user_id


def claim(data, proxies=None):
    tele_id = retrieve_user_id(data)
    url = f"https://api.supermeow.vip/meow/claim?telegram={tele_id}&is_on_chain=false&auth_data={data}"

    try:
        response = requests.post(
            url=url, headers=headers(), proxies=proxies, timeout=20
        )
        status_code = response.status_code
        data = response.json()
        return status_code, data
    except:
        return None


def process_claim(data, proxies=None):
    base.log(f"{base.yellow}Trying to claim...")
    status_code, start_claim = claim(data=data, proxies=proxies)
    if status_code == 200:
        base.log(f"{base.white}Auto Claim: {base.green}Success")
    else:
        message = start_claim["message"]
        base.log(f"{base.white}Auto Claim: {base.red}{message}")
