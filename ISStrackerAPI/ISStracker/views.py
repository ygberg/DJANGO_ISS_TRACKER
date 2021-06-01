from django.http import HttpResponse, request
from django.shortcuts import render
from ISStracker_API.ISStracker.ISSData import *

data = ISS_data_collector.get_data_iss()
time = ISS_data_extractor.get_time(data)
lat = ISS_data_extractor.get_lat(data)
long = ISS_data_extractor.get_long(data)

# Create your views here.

def home_view(request,**kwargs):
    
    context = {'my_time':time,'my_lat':lat,'my_long':long}
    return render (request,"home.html",context)
