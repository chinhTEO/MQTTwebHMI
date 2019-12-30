import paho.mqtt.client as mqtt
from nodeStatus.models import NodeMQTT

class MqttClient():
    flag_connected = 0

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.flag_connected = 1

    def on_disconnect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.flag_connected = 0

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode("utf-8"))
        NodeMQTT.objects.filter(topicName = msg.topic).update(last_msg = msg.payload.decode("utf-8"))

    def connectToBroker(self):
        if( self.flag_connected == 0 ):
            self.client = mqtt.Client()
            self.client.username_pw_set(username="chinh1997",password="chinhgood")
            self.client.on_connect = self.on_connect
            self.client.on_disconnect = self.on_disconnect
            self.client.on_message = self.on_message
            self.client.connect("xem1997.ddns.net",1883,60)

            self.client.loop_start()
            return "done"
        else:   
            return "connected"

    def publishToBroker(self, topic, msg):
        if( self.flag_connected == 1 ):
            self.client.publish(topic, msg)
            return "ok"
        else:   
            return "error"
    
    def subcribe(self, topic):
        if( self.flag_connected == 1 ):
            self.client.subscribe(topic)

mqttClient = MqttClient() 