import googlemaps
from datetime import datetime, timedelta

import json
import requests
import sys


def load_json(filename):
    file = open(filename, mode='r')
    json_loaded = file.read()
    return json.loads(json_loaded)


def get_maps_to_json(maps: str):
    url = "https://mapstogpx.com/load.php?d=default&lang=en&elev=off&tmode=off&pttype=fixed&o=json&cmt=off&desc=off&descasname=off&w=on&dtstr=20220201_211249&gdata=goo.gl%2Fmaps%2F" + maps
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def get_direction(src: str, des: str):
    gmaps = googlemaps.Client(key='AIzaSyBg8Mz7JdohCi_6S9A1ZBqqsrCuXDxWqrg')
    waypoints = [src, des]

    results = gmaps.directions(origin=src,
                               destination=des,
                               waypoints=waypoints,
                               optimize_waypoints=True,
                               departure_time=datetime.now() + timedelta(hours=1))

    print(results[0])


if __name__ == "__main__":
    json_ = load_json("u/victor/2019")
    # print(json_['mapViewData']['data'])
    # get_direction(sys.argv[1], sys.argv[2])
    get_maps_to_json("uA8L1FZXsXA2LikU6")
