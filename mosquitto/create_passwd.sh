#!/bin/sh
set -e

echo "Creating Mosquitto password file..."

# Créer le dossier si nécessaire
mkdir -p /mosquitto/config

# Créer le fichier de mot de passe
mosquitto_passwd -b -c /mosquitto/config/passwd "$MOSQUITTO_USER" "$MOSQUITTO_PASS"

# Donner les bonnes permissions
chmod 600 /mosquitto/config/passwd

# Lancer Mosquitto
exec mosquitto -c /mosquitto/config/mosquitto.conf
