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
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJ2ZW5uZWxhbmFsbHVyaUBnbWFpbC5jb20iLCJleHAiOjE3Nzc3MDQzMDAsImlhdCI6MTc3NzcwMzQwMCwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6ImMzYjc4YjU5LTY3MGEtNDU3ZC05Mjg1LTBjMjEyMDhmM2E0OSIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InZlbm5lbGEiLCJzdWIiOiI2OGU2NWRkOS0wOGRiLTQxMjItYWM0Ni0xZmJhZGZiNzc1MGQifSwiZW1haWwiOiJ2ZW5uZWxhbmFsbHVyaUBnbWFpbC5jb20iLCJuYW1lIjoidmVubmVsYSIsInJvbGxObyI6InJhMjMxMTAyNjAxMDUyMiIsImFjY2Vzc0NvZGUiOiJRa2JweEgiLCJjbGllbnRJRCI6IjY4ZTY1ZGQ5LTA4ZGItNDEyMi1hYzQ2LTFmYmFkZmI3NzUwZCIsImNsaWVudFNlY3JldCI6ImdaSG1zTmVGYUJiZGZWRHUifQ._tNu5kj6ol3i6XN41DymfQWQqGvNIh2K7plEeaHp4Q0"

    result = get_notifications(token)

    print("\n TOP 10 PRIORITY NOTIFICATIONS:\n")

    for n in result:
        print(f"{n['Type']} | {n['Message']} | {n['Timestamp']}")
