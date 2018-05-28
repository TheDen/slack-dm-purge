# slack-dm-purge

## Motivation
[Given the updated Slack Policy](https://thenextweb.com/apps/2018/03/22/slacks-new-policy-lets-bosses-read-employees-dms-without-consent/) which grants customers on Slack's Plus and Enterprise Grid plans access to a self-service tool for exporting data from all public and private channels, having an option to delete your entire DM history is something I feel is needed.

Unfortunately Slack doesn't allow bulk deletes, and apparently there isn't a way of knowing if your DMs are actually private:

>This functionality was previously available too, but it used to notify users when it was turned on, so they’d know that their DMs weren’t entirely private.

This handy script allows you automatically to delete all your DMs given you have a slack token.


## Prerequisites

* `python3`
* [requests](https://github.com/requests/requests)
* A valid slack token

`pip3 install -r requirements.txt`


## Deleting all private DMs

`./slack-dm-purge.py`

This script will delete **_all_** your DMs.

## Alternatives

If you don't have a Slack token, you can also use [this chrome extenion](https://chrome.google.com/webstore/detail/message-deleter-for-slack/eledhnkjmlmljbbamapmggcjkbpcgdlb) to delete your messages through the browser once logged into slack.



