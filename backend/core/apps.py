from django.apps import AppConfig
import threading
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    def ready(self):
        from core.mqtt_client import start_mqtt
        thread = threading.Thread(target=start_mqtt)
        thread.daemon = True
        thread.start()
