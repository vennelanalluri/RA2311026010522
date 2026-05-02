import requests
from datetime import datetime

priority = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

def get_notifications(token):
    url = "http://20.207.122.201/evaluation-service/notifications"

    headers = {
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers)
    data = response.json()["notifications"]

    for n in data:
        n["time"] = datetime.strptime(n["Timestamp"], "%Y-%m-%d %H:%M:%S")

    data.sort(
        key=lambda x: (priority.get(x["Type"], 0), x["time"]),
        reverse=True
    )

    return data[:10]


if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."

    result = get_notifications(token)

    for n in result:
        print(n)
