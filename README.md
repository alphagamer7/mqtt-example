
# MQTT Sensor Monitoring Project

This project helps you monitor sensor values in real-time using MQTT over WebSockets. You'll see the sensor value on the screen, and if it gets too high, an alarm will appear.

## Key Concepts

- **MQTT**: A lightweight messaging protocol used for devices to communicate (like sensors and servers).
- **WebSockets**: A way for web pages to keep a connection open to a server so they can get updates (like sensor data).

### How It Works

- A sensor sends data (like temperature) to the server.
- The system checks the sensor value:
  - If it's **below or equal to 75**, everything is normal.
  - If it's **above 75**, an alarm is triggered.
  
### Project Features

- **Threshold**: The system raises an alarm when the sensor value exceeds `75`.
- **Normal State**: If the sensor value is at or below 75, the system shows that everything is fine.
- **Alarm State**: If the sensor value goes above 75, the system shows a warning.

### What You Will See:

- **When there's an alarm** (sensor value > 75):
  ![Alarm State](https://github.com/user-attachments/assets/a8ec48b8-c84d-4df1-9a56-f0831e4e45e2)

- **When the sensor value is normal** (sensor value ≤ 75):
  ![Normal State](https://github.com/user-attachments/assets/41d8680d-1450-4e95-b754-87e7b8d5ec6e)

### Steps to Get Started:

1. **Understand the Threshold**: The system will trigger an alarm when the sensor value is greater than `75`.
2. **Watch for Changes**: As the sensor sends data, the display will update to show the current status—either normal or alarm.
3. **Experiment**: Try adjusting the threshold and see how the system responds to different values.
