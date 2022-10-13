from typing import Dict
from gpx_converter import Converter
import json
dic = Converter(input_file='gpx/LA.gpx').gpx_to_dictionary(
    latitude_key='latitude', longitude_key='longitude')
# now you have a dictionary and can access the longitudes and latitudes values from the keys
latitudes = dic['latitude']
# print(latitudes)
longitudes = dic['longitude']

input_json = json.load(open('u/victor/2022-Guangdong-Xiangxi'))


class JsonBuilder:
    def __init__(self, input_json: Dict):
        self.json = input_json
        self.clear_column()

    def clear_column(self):
        self.json["mapViewData"]["data"][0]["polylines"] = []
        self.json["mapViewData"]["data"][0]["stationIDs"] = []
        self.json["mapViewData"]["data"][0]["stations"] = []
        self.json["mapViewData"]["data"][1]["polylines"]["points"] = []

    def add_station(self, latitudes: list, longitudes: list) -> Dict:
        for i in range(len(latitudes)):
            self.json["mapViewData"]["data"][0]["stationIDs"].append(i)
            self.json["mapViewData"]["data"][0]["polylines"].append(
                [latitudes[i], longitudes[i]])

    def add_data(self, latitudes: list, longitudes: list) -> Dict:
        for i in range(len(latitudes)):
            self.json["mapViewData"]["data"][1]["polylines"].append(
                [latitudes[i], longitudes[i]])

output = JsonBuilder(input_json)

out_file = open("u/victor/2022-SantaCruz-LA-Irvine", "w")

json.dump(output.json, out_file, indent=4)
