from typing import Dict
from gpx_converter import Converter
import json

input_json = json.load(open('u/victor/2022-Guangdong-Xiangxi'))

def get_gpx_data(filename):
    dic = Converter(input_file=filename).gpx_to_dictionary(
        latitude_key='latitude', longitude_key='longitude')
    # now you have a dictionary and can access the longitudes and latitudes values from the keys
    latitudes = dic['latitude']
    # print(latitudes)
    longitudes = dic['longitude']
    return latitudes, longitudes

class JsonBuilder:
    def __init__(self, input_json: Dict):
        self.json = input_json
        self.clear_column()

    def clear_column(self):
        self.json["mapViewData"]["data"][0]["polylines"] = []
        self.json["mapViewData"]["data"][0]["stationIDs"] = []
        self.json["mapViewData"]["data"][0]["stations"] = []
        for idx, a in enumerate(self.json["mapViewData"]["data"]):
            if idx != 0:
                self.json["mapViewData"]["data"][idx] = {}

    # @staticmethod
    def add_station(self, index: int, id: str, name: str, lat: float, lng: float, addr: str, postcode: int):
        new_json = {"id": id, "name": {"en": name}, "location": {
            "lat": lat, "lng": lng, "address": addr, "postcode": postcode}}
        self.json["mapViewData"]["data"][index]["stations"].append(new_json)
        self.json["mapViewData"]["data"][index]["stationIDs"].append("id")

    # @staticmethod
    def add_car_data(self, index: int, latitudes: list, longitudes: list):
        new_poly = {"type": "CAR",
                    "style": {
                        "color": 4284198070,
                        "pattern": "SOLID"
                    },
                    "points": []}
        for i in range(len(latitudes)):
            new_point = {"lat": latitudes[i], "lng": latitudes[i]}
            new_poly["points"].append(
                new_point)
        self.json["mapViewData"]["data"][index]["polylines"].append(new_poly)

    def add_train_data(self, index: int, latitudes: list, longitudes: list):
        new_poly = {"type": "RAIL",
                    "style": {
                        "color": 4294198070,
                            "pattern": "SOLID"
                    },
                    "points": []}
        for i in range(len(latitudes)):
            new_point = {"lat": latitudes[i], "lng": latitudes[i]}
            new_poly["points"].append(
                new_point)
        self.json["mapViewData"]["data"][index]["polylines"].append(new_poly)


output = JsonBuilder(input_json)

output.add_station(0, "Santa Cruz", "Santa Cruz, CA, USA",
                   36.9741, -122.0308, "Santa Cruz, CA, USA", 95060)
output.add_station(0, "Big Sur", "Big Sur, CA, USA",
                   36.2358, -121.6893, "Big Sur, CA, USA", 93920)
output.add_station(0, "Santa Barbara", "Santa Barbara, CA, USA",
                   34.4208, -119.6982, "Santa Barbara, CA, USA", 93101)
output.add_station(0, "Oxnard", "Oxnard, CA, USA",
                   34.1975, -119.1771, "Oxnard, CA, USA", 93030)
output.add_station(0, "Los Angeles", "Los Angeles, CA, USA",
                   34.0522, -118.2437, "Los Angeles, CA, USA", 90012)
output.add_station(0, "Irvine", "Irvine, CA, USA",
                   33.6839, -117.7947, "Irvine, CA, USA", 92618)

output.add_car_data(0,*get_gpx_data("gpx/From_SC_to_LA.gpx"))
output.add_train_data(0,*get_gpx_data("gpx/LA_to_IV.gpx"))  
output.add_car_data(0,*get_gpx_data("gpx/Morning_Ride.gpx"))  
output.add_car_data(0,*get_gpx_data("gpx/josef.gpx"))  
out_file = open("u/victor/2022-SantaCruz-LA-Irvine", "w")

json.dump(output.json, out_file, indent=4)
