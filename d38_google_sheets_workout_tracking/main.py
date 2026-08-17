
import requests
import json
import datetime as dt

APP_ID = 123
API_KEY = 123

req_header = {
    # "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

data = {
  "query": "ran 3 miles",
  "weight_kg": 70,
  "height_cm": 175,
  "age": 30,
  "gender": "male"
}

workout_response = requests.post(url=URL, json=data, headers=req_header)
result = workout_response.json()["exercises"][0]
print(result)



# with open("./workout.json", mode="w") as file:
#     json.dump(result, file, indent=4)

SHITTY_GET = "https://api.sheety.co/64fb40c12336c694e44daeed1667e640/myWorkouts/workouts"
SHITTY_POST = "https://api.sheety.co/64fb40c12336c694e44daeed1667e640/myWorkouts/workouts"

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

body = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": result["name"].title(),
        "duration": result["duration_min"],
        "calories": result["nf_calories"],
    }
}



# print(type(today_date))
# print(type(now_time))

# {
#     "duration_min": 30,
#     "nf_calories": 360,
#     "name": "running",
# }


#? Shitty Post
post_on_shitty = requests.post(url=SHITTY_POST, json=body)
shitty_response = post_on_shitty.json()
print(shitty_response)


#? Shitty Get
# shitty_response = requests.get(url=SHITTY_GET)
# shit_result = shitty_response.json()
# print(shit_result)