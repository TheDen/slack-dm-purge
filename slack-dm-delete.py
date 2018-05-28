#!/usr/bin/env python3

import requests


def dmdelete(token, channel):
    params = {"channel": channel, "token": token}

    while True:
        try:
            response = requests.get("https://slack.com/api/im.history", params=params)
        except requests.exceptions.RequestException as e:
            print(e)

        dmhistory = response.json()
        for i in dmhistory["messages"]:
            requests.post(
                "https://slack.com/api/chat.delete?ts=" + i["ts"], params=params
            )
        if not dmhistory["has_more"]:
            break


def dmlist(token):
    params = {"token": token}
    try:
        response = requests.get("https://slack.com/api/im.list", params=params)
    except requests.exceptions.RequestException as e:
        print(e)

    dmdata = response.json()
    dmlist = []
    for i in dmdata["ims"]:
        dmlist.append(i["id"])
    return dmlist


def main():
    token = "Your Slack Token"
    channels = dmlist(token)
    for channel in channels:
        dmdelete(token, channel)


if __name__ == "__main__":
    main()
