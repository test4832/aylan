import requests

url = "https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms1"

querystring = {"phonenum":"14388229782","msg":"Hello, google.ca"}

headers = {
    'x-rapidapi-key': "cbc9fb60f2msh283a4325d46c8afp1b46e6jsn4353c386ff23",
    'x-rapidapi-host': "sms-international.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
