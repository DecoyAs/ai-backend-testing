import requests

print("WELCOME TO MY CHAT APP")
print("\n")

id = 1

while True:
    msg = input("YOU : ")

    if "exit" in msg.lower():
        print("Closing Program.")
        print("Bye")
        exit()

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "id" : id,
            "msg" : f"{msg}"
        }
    )

    data = response.json()

    if data["message"] == "UNSUCCESSFULL" :
        print("Bad Request, Unsuccessfull")
    else:
        print(f"Response : {data['msg']}")
        id = id + 1

