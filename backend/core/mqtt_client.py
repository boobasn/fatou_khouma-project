import paho.mqtt.client as mqtt
import json
from django.conf import settings
from core.models import Device
from core.models import SensorReading

# Callback quand on se connecte au broker
def on_connect(client, userdata, flags, rc):
    print("✅ Connecté au broker avec le code :", rc)
    # S'abonner au topic
    client.subscribe("esp32/sensors")

# Callback quand un message est reçu
def on_message(client, userdata, msg):
    print(f"📩 Reçu sur {msg.topic} : {msg.payload.decode()}")
    try:
        data = json.loads(msg.payload.decode())
        print("🔍 Données reçues :", data)
        device_identifier = data.get("device_id")
        print(f"🔑 Device Primary Key :", {device_identifier})
        device_obj = Device.objects.get(device_id=device_identifier)
        print("🔑 Device Object :", {device_obj})
        SensorReading.objects.create(
            device = device_obj ,
            temp=data.get("temperature"),
            humidity=data.get("humidity"),
            timestamp=data.get("timestamp"),
            soil_moisture =data.get("soil_moisture")
        )
        print("✅ Données insérées en DB")
    except Exception as e:
        print("⚠️ Erreur insertion DB :", e)

def start_mqtt():
    client = mqtt.Client()
    client.username_pw_set(settings.MOSQUITTO_USER, settings.MOSQUITTO_PASS)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(settings.MQTT_HOST, settings.MQTT_PORT, 60)
    client.loop_forever()
