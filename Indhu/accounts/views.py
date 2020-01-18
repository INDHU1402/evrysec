from django.shortcuts import render,redirect
import requests
import json
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from geopy.geocoders import Nominatim, ArcGIS, GoogleV3 # Geocoder APIs
import geocoder

import requests
import json
import geocoder
URL = 'https://www.sms4india.com/api/v1/sendCampaign'
# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

def done(request):
  url = 'https://api.chat-api.com/instance92768/sendMessage?token=04y9do9knq3wct9y'
  data1 = {"phone": "+916303965439","body": "Help me!! it's an emergency"}
  data2 = {"phone": "+918500520851","body": "Help me!! it's an emergency"}
  data3 = {"phone": "+919959091719","body": "Help me!! it's an emergency"}
  res1 = requests.post(url, json=data1)
  res2 = requests.post(url, json=data2)
  res3 = requests.post(url, json=data3)
  print(res1.text)
  print(res2.text)
  print(res3.text)
 #Create your views here.
  res = requests.get('https://ipinfo.io/')
  data = res.json()
  city = data['city']
  location = data['loc'].split(',')
  latitude = str(location[0])
  longitude = str(location[1])
  print("Latitude : "+latitude)
  print("Longitude : "+longitude)
  print("City : "+city)
  response = sendPostRequest(URL,'QH9CPHJM0807OSAX44SP0JGHLN2MOLU8', '7642BNRXFRG8UYUS', 'stage','8500520851', 'chinthamanenisowmya176@gmail.com',"Latitude : "+latitude+"Longitude : "+longitude+"City : "+city)
  g = Nominatim(user_agent="my-application")
  n = g.reverse((latitude, longitude), timeout=10) # Lat, Long to reverse geocode
  print(n.address)
  print(response.text)
  return render(request,'success.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def report(request):
    return render(request,'report.html')    
def page(request):
    return render(request,'page.html')
    
