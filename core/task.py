import requests

from smart_airdrop_claimer import base
from core.headers import headers, retrieve_user_id


def checkin(data, proxies=None):
    tele_id = retrieve_user_id(data)
    url = f"https://api.supermeow.vip/meow/serial-checkin?telegram={tele_id}&is_on_chain=false&auth_data={data}"

    try:
        response = requests.post(
            url=url, headers=headers(), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["is_done"]
        return status
    except:
        return None


def get_quest(data, proxies=None):
    tele_id = retrieve_user_id(data)
    url = f"https://api.supermeow.vip/meow/quests?telegram={tele_id}&auth_data={data}"

    try:
        response = requests.get(url=url, headers=headers(), proxies=proxies, timeout=20)
        data = response.json()
        quest_list = data["results"]
        return quest_list
    except:
        return None


def do_task(data, task_id, proxies=None):
    url = f"https://api.supermeow.vip/meow/tasks/{task_id}/do?auth_data={data}"

    try:
        response = requests.post(
            url=url, headers=headers(), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["is_complete"]
        return status
    except:
        return None


def process_checkin(data, proxies=None):
    checkin_status = checkin(data=data, proxies=proxies)
    if checkin_status is not None:
        if checkin_status:
            base.log(f"{base.white}Auto Check-in: {base.green}Success")
        else:
            base.log(f"{base.white}Auto Check-in: {base.red}Checked in already")
    else:
        base.log(f"{base.white}Auto Check-in: {base.red}Fail")


def process_do_task(data, proxies=None):
    quest_list = get_quest(data=data, proxies=proxies)
    if quest_list:
        for quest in quest_list:
            tasks = quest["tasks"]
            for task in tasks:
                task_id = task["id"]
                task_name = task["name"]
                task_status = task["account_task"]["is_complete"]
                if task_id == 11:
                    base.log(f"{base.white}{task_name}: {base.red}Incomplete")
                elif task_status:
                    base.log(f"{base.white}{task_name}: {base.green}Completed")
                else:
                    do_task_status = do_task(
                        data=data, task_id=task_id, proxies=proxies
                    )
                    if do_task_status:
                        base.log(f"{base.white}{task_name}: {base.green}Completed")
                    else:
                        base.log(f"{base.white}{task_name}: {base.red}Incomplete")
    else:
        base.log(f"{base.white}Auto Do Task: {base.red}Get quest list error")
