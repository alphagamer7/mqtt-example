import paho.mqtt.client as mqtt
import random
import time

# Define MQTT server details
BROKER = 'broker.emqx.io'  # Public EMQX broker
PORT = 8083  # WebSocket port for EMQX
TOPIC = 'sensor/temperature'

# Set a threshold for alarming values
THRESHOLD = 75

# Callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to EMQX broker over WebSocket")
    else:
        print(f"Failed to connect with result code {rc}")

# Publish sensor values
def publish_values():
    # Create a client instance
    client = mqtt.Client(transport="websockets")  # Specify "websockets" as transport
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)  # Connect to broker over WebSockets

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
