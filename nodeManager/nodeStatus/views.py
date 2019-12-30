from django.shortcuts import render
import paho.mqtt.client as mqtt
from .models import NodeMQTT
# Create your views here.

def index(request):
    objects = NodeMQTT.objects.all()
    return render(request, 'nodeStatus/index.html', {'objects' : objects})