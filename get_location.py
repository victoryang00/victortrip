import googlemaps
import sys
gmaps = googlemaps.Client(key='')

#short form of address, such as country + postal code
geocode_result = gmaps.geocode(sys.argv[1])

print(geocode_result[0]["formatted_address"]) 
print(geocode_result[0]["geometry"]["location"]["lat"]) 
print(geocode_result[0]["geometry"]["location"]["lng"])
