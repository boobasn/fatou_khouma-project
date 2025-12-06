#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// ----------------- CONFIG WIFI -----------------
#define WIFI_SSID       "Familly Sakho"
#define WIFI_PASSWORD   "151080.Sn"

// ----------------- CONFIG MQTT -----------------
#define MQTT_SERVER     "192.168.1.2"
#define MQTT_PORT       1883
#define MQTT_USERNAME   "device1"
#define MQTT_PASSWORD   "devpass"

#define TOPIC_PUBLISH   "esp32/sensors"

// ----------------- CAPTEURS -----------------
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

#define WATER_SENSOR_PIN 34  // entrée analogique

WiFiClient espClient;
PubSubClient client(espClient);


// =========================================================
//                CONNECT WIFI
// =========================================================
void connectWifi() {
  Serial.print("Connexion au WiFi...");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connecté !");
  Serial.print("Adresse IP : ");
  Serial.println(WiFi.localIP());   // AFFICHAGE IP ESP32
}


// =========================================================
//                CONNECT MQTT
// =========================================================
void reconnectMQTT() {
  while (!client.connected()) {
    Serial.print("Connexion MQTT… ");

    if (client.connect("ESP32Client", MQTT_USERNAME, MQTT_PASSWORD)) {
      Serial.println("Connecté !");
    } else {
      Serial.print("Erreur : ");
      Serial.println(client.state());
      delay(2000);
    }
  }
}


// =========================================================
//                SETUP
// =========================================================
void setup() {
  Serial.begin(115200);
  dht.begin();
  connectWifi();
  client.setServer(MQTT_SERVER, MQTT_PORT);

  Serial.println("Initialisation terminée. Début du programme...");
}


// =========================================================
//                LOOP
// =========================================================
void loop() {
  if (!client.connected()) {
    reconnectMQTT();
  }
  client.loop();

  // Lire DHT22
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Lire capteur d'humidité du sol
  int soilValue = analogRead(WATER_SENSOR_PIN);

  // Vérifier erreurs DHT
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Erreur lecture DHT22");
    return;
  }

  // ------------------------------------------
  //      JSON EXACT QUE DJANGO ATTEND
  // ------------------------------------------
  String jsonPayload = "{";
  jsonPayload += "\"device_id\": 1,";
  jsonPayload += "\"temperature\": " + String(temperature, 1) + ",";
  jsonPayload += "\"humidity\": " + String(humidity, 1) + ",";
  jsonPayload += "\"soil_moisture\": " + String(soilValue);
  jsonPayload += "}";

  Serial.println("Envoi JSON => " + jsonPayload);

  client.publish(TOPIC_PUBLISH, jsonPayload.c_str());

  delay(5000); // toutes les 5 secondes
}
