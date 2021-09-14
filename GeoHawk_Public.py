#!/usr/bin/env python3

import json
import requests

class GeoHawk:
    def __init__(self, apiKey, ip_list, keys = ["ip", "country_name", "latitude", "longitude", "isp", "time_zone"]):
        self.url = 'https://api.ipgeolocation.io/ipgeo?'
        self.apiKey = apiKey
        self.keys = keys
        self.json_data = self.scrap(ip_list)
    
    def extract(self, ip_dict):
        data = { key:value for (key,value) in ip_dict.items() if key in self.keys}
        timeStamp = data['time_zone']['current_time'][:-5] + " UTC" + data['time_zone']['current_time'][-5:]

        del data['time_zone']

        data['timeStamp'] = timeStamp

        return data

    def scrap(self, ip_list):
        self.ipData = {}
        for ip in ip_list:
            url = self.url + 'apiKey=' + self.apiKey + '&=' + ip
            data = requests.get(url)
            if ip in self.ipData.keys():
                self.ipData[ip].append(self.extract(json.loads(data.text)))
            else:
                self.ipData[ip] = [self.extract(json.loads(data.text))]

    def returnLatestData(self):
        for key, val in self.ipData.items():
            print("IP: " + key)
            print("Value: " + json.dumps(val[-1]))

    def returnDatabase(self):
        print(self.ipData)

if __name__ == "__main__":
    api_key = ""
    ip_list = []

    try:
        api_key = sys.argv[1]
        ip_list = []
    except:
        api_key = 'KEY-HERE'
        ip_list = ['8.8.8.8', '1.1.1.1', '2.2.2.2', '8.8.8.8']

    geoips = GeoHawk(api_key, ip_list)
    geoips.returnLatestData()
