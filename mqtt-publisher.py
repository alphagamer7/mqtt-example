import paho.mqtt.client as mqtt
import random
import time

# Define MQTT server details
BROKER = 'localhost'  # Change if necessary (e.g., use host IP or container IP)
PORT = 1883  # Standard MQTT port exposed by EMQX in Docker
TOPIC = 'sensor/temperature'

# Set a threshold for alarming values
THRESHOLD = 75

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to EMQX broker")
    else:
        print(f"Failed to connect with result code {rc}")

def publish_values():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)

    client.loop_start()

    try:
        while True:
            # Generate random sensor value between 50 and 100
            value = random.uniform(50, 100)
            client.publish(TOPIC, value)
            print(f"Published {value} to topic {TOPIC}")
            time.sleep(2)  # Publish every 2 seconds
    except KeyboardInterrupt:
        client.loop_stop()
        print("Stopping MQTT Publisher")

if __name__ == "__main__":
    publish_values()
