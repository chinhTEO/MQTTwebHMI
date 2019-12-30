from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .mqttClientConnection import mqttClient
from nodeStatus.models import NodeMQTT
import json

# Create your views here.



@csrf_exempt
def connect(request):
    if request.method == 'POST':
        cmd = request.POST['cmd']
        if cmd == "connect":

            response_data = {}
            response_data['host'] = "xem1997.ddns.net"
            response_data['port'] = "1883"
            response_data['msg'] =  mqttClient.connectToBroker()

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@csrf_exempt
def publish(request):
    if request.method == 'POST':
        cmd = request.POST['cmd']
        if cmd == "publish":
            response_data={}
            response_data['msg'] = "ok"

            status = mqttClient.publishToBroker(request.POST['topic'],request.POST['msg'])

            if(status == "error"):
                return HttpResponse(
                json.dumps({"msg" : "error ( please connect to broker first )"}),
                content_type="application/json")
            else:
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json")  

@csrf_exempt
def subcribe(request):
    if request.method == 'POST':
        cmd = request.POST['cmd']
        if cmd == "subcribe":
            response_data = {}
            response_data['msg'] = 'ok'
            mqttClient.subcribe(request.POST['topic'])
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

@csrf_exempt
def update(request):
    if request.method == 'POST':
        cmd = request.POST['cmd']
        if cmd == "update":
            response_data = {}
            response_data['msg'] = NodeMQTT.objects.get(topicName = request.POST['topic']).last_msg
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

