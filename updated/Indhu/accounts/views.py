from django.shortcuts import render,redirect
import requests
import json
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import EmailMessage
from .forms import EmailForm
from django.conf import settings
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

def done1(request):
  res = requests.get('https://ipinfo.io/')
  data = res.json()
  city = data['city']
  location = data['loc'].split(',')
  latitude = str(location[0])
  longitude = str(location[1])
  print("Latitude : "+latitude)
  print("Longitude : "+longitude)
  print("City : "+city)
  url = 'https://api.chat-api.com/instance92768/sendMessage?token=04y9do9knq3wct9y'
  #data1 = {"phone": "+916303965439","body": "Help me!! it's a fire accident!!"}
  #data2 = {"phone": "+918500520851","body": "Help me!! it's a fire accident!!" + "Latitude : "+latitude+"Longitude : "+longitude+"City : "+city}
  data1 = {"phone": "+919959091719","body": "Help me!!Fire accident it's an emergency!!" + "Latitude : "+latitude+ "Longitude : "+longitude+"City : "+city}
  #res1 = requests.post(url, json=data1)
  #res2 = requests.post(url, json=data2)
  res1 = requests.post(url, json=data1)
  #print(res1.text)
  #print(res2.text)
  print(res1.text)
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
  #response = sendPostRequest(URL,'QH9CPHJM0807OSAX44SP0JGHLN2MOLU8', '7642BNRXFRG8UYUS', 'stage','8500520851', 'chinthamanenisowmya176@gmail.com',"Latitude : "+latitude+"Longitude : "+longitude+"City : "+city)
  #g = Nominatim(user_agent="my-application")
  #n = g.reverse((latitude, longitude), timeout=10) # Lat, Long to reverse geocode
  #print(n.address)
  #print(response.text)
  return render(request,'success1.html')

def done2(request):
  res = requests.get('https://ipinfo.io/')
  data = res.json()
  city = data['city']
  location = data['loc'].split(',')
  latitude = str(location[0])
  longitude = str(location[1])
  print("Latitude : "+latitude)
  print("Longitude : "+longitude)
  print("City : "+city)
  url = 'https://api.chat-api.com/instance92768/sendMessage?token=04y9do9knq3wct9y'
  #data4 = {"phone": "+916303965439","body": "Help me!! it's a fire accident!!"}
  #data5 = {"phone": "+918500520851","body": "Help me!! it's a fire accident!!"}
  data2 = {"phone": "+919959091719","body": "Help me!!Harrasment it's an emergency!!" + "Latitude : "+latitude+"Longitude : "+longitude+"City : "+city}
  #res4 = requests.post(url, json=data1)
  #res5 = requests.post(url, json=data2)
  res2 = requests.post(url, json=data2)
  #print(res4.text)
  #print(res5.text)
  print(res2.text)
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
  #response = sendPostRequest(URL,'QH9CPHJM0807OSAX44SP0JGHLN2MOLU8', '7642BNRXFRG8UYUS', 'stage','8500520851', 'chinthamanenisowmya176@gmail.com',"Latitude : "+latitude+"Longitude : "+longitude+"City : "+city)
  #g = Nominatim(user_agent="my-application")
  #n = g.reverse((latitude, longitude), timeout=10) # Lat, Long to reverse geocode
  #print(n.address)
  #print(response.text)
  return render(request,'success2.html')

def done3(request):
  res = requests.get('https://ipinfo.io/')
  data = res.json()
  city = data['city']
  location = data['loc'].split(',')
  latitude = str(location[0])
  longitude = str(location[1])
  print("Latitude : "+latitude)
  print("Longitude : "+longitude)
  print("City : "+city)
  url = 'https://api.chat-api.com/instance92768/sendMessage?token=04y9do9knq3wct9y'
  #data7 = {"phone": "+916303965439","body": "Help me!! it's a fire accident!!"}
  #data8 = {"phone": "+918500520851","body": "Help me!! it's a fire accident!!"}
  data3 = {"phone": "+919959091719","body": "Violation of traffic rules!!" + "Latitude : "+latitude+"Longitude : "+longitude+"City : "+city}
  #res7 = requests.post(url, json=data1)
  #res8 = requests.post(url, json=data2)
  res3 = requests.post(url, json=data3)
  #print(res7.text)
  #print(res8.text)
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
  #response = sendPostRequest(URL,'QH9CPHJM0807OSAX44SP0JGHLN2MOLU8', '7642BNRXFRG8UYUS', 'stage','8500520851', 'chinthamanenisowmya176@gmail.com',"Latitude : "+latitude+"Longitude : "+longitude+"City : "+city)
  #g = Nominatim(user_agent="my-application")
  #n = g.reverse((latitude, longitude), timeout=10) # Lat, Long to reverse geocode
  #print(n.address)
  #print(response.text)
  return render(request,'success3.html')

def done4(request):
  res = requests.get('https://ipinfo.io/')
  data = res.json()
  city = data['city']
  location = data['loc'].split(',')
  latitude = str(location[0])
  longitude = str(location[1])
  print("Latitude : "+latitude)
  print("Longitude : "+longitude)
  print("City : "+city)
  url = 'https://api.chat-api.com/instance92768/sendMessage?token=04y9do9knq3wct9y'
  #data10 = {"phone": "+916303965439","body": "Help me!! it's a fire accident!!"}
  #data11 = {"phone": "+918500520851","body": "Help me!! it's a fire accident!!"}
  data4 = {"phone": "+919959091719","body": "Help me!! it's a cyber crime!!" + "Latitude : "+latitude+"Longitude : "+longitude+"City : "+city}
  #res10 = requests.post(url, json=data1)
  #res11 = requests.post(url, json=data2)
  res4 = requests.post(url, json=data4)
  #print(res1.text)
  #print(res2.text)
  print(res4.text)
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
  #response = sendPostRequest(URL,'QH9CPHJM0807OSAX44SP0JGHLN2MOLU8', '7642BNRXFRG8UYUS', 'stage','8500520851', 'chinthamanenisowmya176@gmail.com',"Latitude : "+latitude+"Longitude : "+longitude+"City : "+city)
  #g = Nominatim(user_agent="my-application")
  ##n = g.reverse((latitude, longitude), timeout=10) # Lat, Long to reverse geocode
  #print(n.address)
  #print(response.text)
  return render(request,'success4.html')

def done5(request):
  res = requests.get('https://ipinfo.io/')
  data = res.json()
  city = data['city']
  location = data['loc'].split(',')
  latitude = str(location[0])
  longitude = str(location[1])
  print("Latitude : "+latitude)
  print("Longitude : "+longitude)
  print("City : "+city)
  url = 'https://api.chat-api.com/instance92768/sendMessage?token=04y9do9knq3wct9y'
  #data1 = {"phone": "+916303965439","body": "Help me!! it's a fire accident!!"}
  #data2 = {"phone": "+918500520851","body": "Help me!! it's a fire accident!!"}
  data5 = {"phone": "+919959091719","body": "Help me!! Accident it's an emergency!!" + "Latitude : "+latitude+"Longitude : "+longitude+"City : "+city}
  #res1 = requests.post(url, json=data1)
  #res2 = requests.post(url, json=data2)
  res5 = requests.post(url, json=data5)
  #print(res1.text)
  #print(res2.text)
  print(res5.text)
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
  #response = sendPostRequest(URL,'QH9CPHJM0807OSAX44SP0JGHLN2MOLU8', '7642BNRXFRG8UYUS', 'stage','8500520851', 'chinthamanenisowmya176@gmail.com',"Latitude : "+latitude+"Longitude : "+longitude+"City : "+city)
  #g = Nominatim(user_agent="my-application")
  #n = g.reverse((latitude, longitude), timeout=10) # Lat, Long to reverse geocode
  #print(n.address)
  #print(response.text)
  return render(request,'success5.html')

def done6(request):
  res = requests.get('https://ipinfo.io/')
  data = res.json()
  city = data['city']
  location = data['loc'].split(',')
  latitude = str(location[0])
  longitude = str(location[1])
  print("Latitude : "+latitude)
  print("Longitude : "+longitude)
  print("City : "+city)
  url = 'https://api.chat-api.com/instance92768/sendMessage?token=04y9do9knq3wct9y'
  #data1 = {"phone": "+916303965439","body": "Help me!! it's a fire accident!!"}
  #data2 = {"phone": "+918500520851","body": "Help me!! it's a fire accident!!"}
  data6 = {"phone": "+919959091719","body": "Help me!! it's a  crime!!"}
  #res1 = requests.post(url, json=data1)
  #res2 = requests.post(url, json=data2)
  res6 = requests.post(url, json=data6)
  #print(res1.text)
  #print(res2.text)
  print(res6.text)
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
  #response = sendPostRequest(URL,'QH9CPHJM0807OSAX44SP0JGHLN2MOLU8', '7642BNRXFRG8UYUS', 'stage','8500520851', 'chinthamanenisowmya176@gmail.com',"Latitude : "+latitude+"Longitude : "+longitude+"City : "+city)
  #g = Nominatim(user_agent="my-application")
  #n = g.reverse((latitude, longitude), timeout=10) # Lat, Long to reverse geocode
  #print(n.address)
  #print(response.text)
  return render(request,'success6.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def report(request):
    return render(request,'report.html')    
def page(request):
    return render(request,'page.html')
def efire(request):
    return render(request,'efire.html')   

class EmailAttachementView(generic.CreateView):
    form_class = EmailForm
    success_url = reverse_lazy('login')
    template_name = 'emailattachment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

    # Single File Attachment
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)

    #     if form.is_valid():
            
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         email = form.cleaned_data['email']
    #         attach = request.FILES['attach']

    #         try:
    #             mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    #             mail.attach(attach.name, attach.read(), attach.content_type)
    #             mail.send()
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
    #         except:
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

    #     return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})
    
