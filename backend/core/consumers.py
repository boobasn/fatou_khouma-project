import json
import asyncio
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from asgiref.sync import sync_to_async

logger = logging.getLogger(__name__)

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        logger.info(f"WebSocket connecté: {self.channel_name}")

        # Flag pour arrêter la boucle si le client se déconnecte
        self.keep_sending = True

        # Boucle d'envoi des infos toutes les 2 sec
        asyncio.create_task(self.send_sensor_data_loop())

    async def disconnect(self, code):
        self.keep_sending = False
        logger.info(f"WebSocket déconnecté: {self.channel_name} (code {code})")

    async def send_sensor_data_loop(self):
        
        try:
            while self.keep_sending:
                data = await self.get_last_readings()
                await self.send(json.dumps(data))
                logger.debug(f"Envoyé au client {self.channel_name}: {data}")
                await asyncio.sleep(2)
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi des données WebSocket: {e}")

    @sync_to_async
    def get_last_readings(self):
        from .models import SensorReading
        
        readings = SensorReading.objects.order_by("-timestamp")[:10]
        return [
            {
                "device": r.device.id,
                "temp": r.temp,
                "humidity": r.humidity,
                "soil_moisture": r.soil_moisture,
                "timestamp": r.timestamp.isoformat(),
            }
            for r in readings
        ]
