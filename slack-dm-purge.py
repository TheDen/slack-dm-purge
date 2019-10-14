#!/usr/bin/env python3

import os
import sys
import requests
import time


def dm_delete(token, channel):
    params = {"channel": channel, "token": token}
    latest = "0"

    while True:
        try:
            print(latest)
            response = requests.get(
                f"https://slack.com/api/im.history?latest=" + latest + "&count=1000",
                params=params,
            )
        except requests.exceptions.RequestException as e:
            print(e)

        dm_history = response.json()
        if not dm_history["messages"]:
            break
        latest = dm_history["messages"][-1]["ts"]
        for i in dm_history["messages"]:
            requests.post(
                "https://slack.com/api/chat.delete?ts=" + i["ts"], params=params
            )
            time.sleep(1)
        if not dm_history["has_more"]:
            break


def dm_list(token):
    params = {"token": token}
    try:
        response = requests.get("https://slack.com/api/im.list", params=params)
    except requests.exceptions.RequestException as e:
        print(e)

    dm_data = response.json()
    dm_list = []
    for i in dm_data["ims"]:
        dm_list.append(i["id"])
    return dm_list


def check_env_var_token(slack_token_env_var):
    if slack_token_env_var in os.environ:
        return os.environ.get(slack_token_env_var)
    else:
        return None


if __name__ == "__main__":
    slack_token_env_var = "SLACK_TOKEN"
    slack_token = check_env_var_token(slack_token_env_var)
    if slack_token is None:
        print("{} env var not set".format(slack_token_env_var))
        sys.exit(1)
    channels = dm_list(token)
    for channel in channels:
        dm_delete(token, channel)
