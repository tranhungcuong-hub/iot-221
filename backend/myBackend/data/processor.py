import requests
import json

# GET LIGHT DATA
def getLedData():
    response_API = requests.get('https://io.adafruit.com/api/v2/trungbui2405/feeds/dadn.cambien-anhsang/data/')
    data = response_API.text
    parse_json = json.loads(data)

    lightData = []

    for i in parse_json:
        lightData.append([i['value'], i['created_at'], i['created_epoch'], i['expiration']])
    return lightData