from django.db import models
from django.contrib.auth.hashers import make_password
from django.db import models
from cryptography.fernet import Fernet

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=20, default='viewer')
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw):
        self.password_hash = make_password(raw)

    def __str__(self):
        return self.username

class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    secret_key = models.BinaryField(null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.device_id
    def set_password(self, raw_password, key):
        f = Fernet(key)
        self.password = f.encrypt(raw_password.encode())

    def get_password(self, key):
        f = Fernet(key)
        return f.decrypt(self.password).decode()

class SensorReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temp = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    soil_moisture = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Action(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50)
    initiated_by = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=255, blank=True)

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    refresh_token = models.CharField(max_length=255)
    revoked = models.BooleanField(default=False)
    issued_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
