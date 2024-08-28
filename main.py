import requests
from datetime import datetime

today = datetime.now()

pixel_endpoint = "https://pixe.la/v1/users"
USER_NAME = "[username]"
TOKEN = "[your password]"
GRAPH_ID = "graph1"
DATE_FORMAT = today.strftime("%G%m%d")

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixel_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "my_coding_graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# print(today.strftime("%G%m%d"))
post_config = {
    "date": DATE_FORMAT,
    "quantity": input("How many minutes do you code ? "),
}

update_endpoint = f"{post_endpoint}/{DATE_FORMAT}"
# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)
update_data = {
    "quantity": "120",
}
response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)
delete_endpoint = f"{update_endpoint}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
