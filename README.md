# IoT Security Project - Docker Compose bundle

Contenu:
- Docker Compose with 3 services: MySQL, Django backend, Eclipse Mosquitto.
- Django project (`backend/`) with a `core` app and models matching the IoT security schema.
- SQL initialization script `db/init.sql` that will create the tables automatically when MySQL first starts.
- Mosquitto config and a small script to create the username/password file from environment variables.

Quick start:
1. Copy `.env.example` to `.env` and edit credentials.
2. Build and run:
   docker compose up --build

Notes:
- For production, add TLS for Mosquitto (listener 8883), and secure Django with HTTPS and robust SECRET_KEY.
