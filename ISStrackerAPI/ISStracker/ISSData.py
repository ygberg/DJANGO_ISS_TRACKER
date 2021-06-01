import requests
import datetime



class ISS_data_collector():

    def get_data_iss():
        url = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(url)
        json = response.json()
        return json

class ISS_data_extractor():

    def get_time(data):
        time = data['timestamp']
        date_time = datetime.datetime.fromtimestamp(time)
        return date_time
    def get_lat(data):
        latitude = data['iss_position']['latitude']
        return latitude
    def get_long(data):
        longitude = data['iss_position']['longitude']
        return longitude

data = ISS_data_collector.get_data_iss()
time = ISS_data_extractor.get_time(data)
lat = ISS_data_extractor.get_lat(data)
long = ISS_data_extractor.get_long(data)


print (f"current Time:{time}\ncurrent Longitude: {long}\ncurrent Latitude{lat}")

