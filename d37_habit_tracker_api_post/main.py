
import requests
import datetime as dt

#? Creating user

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "buytt765rtvuy75dfyg8huiu97777775"
USERNAME = "soham3301"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=parameters)
# res_data = response.json()

# print(res_data)

#? Creating a graph

req_header = {
    "X-USER-TOKEN": TOKEN
}

GRAPH_ID = "gymgraph001"

graph_body = {
    "id": GRAPH_ID,
    "name": "my_gym_graph",
    "unit": "day",
    "type": "int",
    "color": "kuro"
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_body, headers=req_header)
# print(graph_response.text)

#? Posting a Pixel

#! pythons inbuilt strftime method can format date / time however you need
today = dt.datetime.now()
pixel_body = {
    "date": f"{today.strftime("%Y%m%d")}",
    "quantity": "3",
}

POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_body, headers=req_header)
print(pixel_response.text)
