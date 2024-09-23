import requests

from smart_airdrop_claimer import base
from core.headers import headers, retrieve_user_id, retrieve_user_info


def get_info(data, proxies=None):
    tele_id = retrieve_user_id(data)
    url = f"https://api.supermeow.vip/meow/info?telegram={tele_id}&auth_data={data}"
    payload = retrieve_user_info(data)

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        balance = round(data["balance"], 3)
        base.log(f"{base.green}Balance: {base.white}{balance:,}")
        return data
    except:
        return None
