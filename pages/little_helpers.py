import datetime


def tomorrow():
    today = datetime.datetime.now().day
    if today != 30 or today != 31:
        return str(today + 1)
    else:
        return '1'
