#!/bin/sh

if [ ! -f /mosquitto/config/passwd ]; then
  mosquitto_passwd -c -b /mosquitto/config/passwd "$MOSQUITTO_USER" "$MOSQUITTO_PASS"
else
  mosquitto_passwd -b /mosquitto/config/passwd "$MOSQUITTO_USER" "$MOSQUITTO_PASS"
fi

exec mosquitto -c /mosquitto/config/mosquitto.conf
