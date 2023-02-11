import requests
import datetime
import os

day = datetime.datetime.now()

today = day.strftime('%d/%m/%Y')
time = day.strftime('%H:%M:%S')

print(today)

API_ID = 'ID'
API_KEY = 'KEY'

url = 'END_POINT'

HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

body = {
 "query":input("Tell me which exercises you did\n"),
 "gender":input("Your Gender('female/male/other')\n"),
 "weight_kg":float(input("your weight\n")),
 "height_cm":float(input("your height\n")),
 "age":int(input("your age\n"))
}
respons = requests.post(url, json=body, headers=HEADERS)
file = respons.json()
exercises = file['exercises'][0]['name']

url_sheet = os.environ.get('SHEET_API')

data = {
    'workout': {
        'date': today,
        'time': format(time),
        'exercise': exercises,
        'duration': file['exercises'][0]['duration_min'],
        'calories': file['exercises'][0]['nf_calories'],
        'id':2
}
}
header = {
    'Authorization': 'Basic AUT_KEY'
}
RESPONS = requests.post(url_sheet,json=data, headers=header
)
print(RESPONS.text)
