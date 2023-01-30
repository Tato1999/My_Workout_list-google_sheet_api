import requests
import datetime
import os

day = datetime.datetime.now()

today = day.strftime('%d/%m/%Y')
time = day.strftime('%H:%M:%S')

print(today)

API_ID = '59d19d8a'
API_KEY = '28f546c2239d7acc40ddd72b9a8ff5f8'

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

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
    'Authorization': 'Basic VGF0bzpHMTIzNDU2N0A='
}
RESPONS = requests.post(url_sheet,json=data, headers=header
)
print(RESPONS.text)