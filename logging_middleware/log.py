import requests

def Log(stack, level, package, message, token):
    url = "http://20.207.122.201/evaluation-service/logs"

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    body = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    try:
        requests.post(url, json=body, headers=headers)
    except:
        pass
