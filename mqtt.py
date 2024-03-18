#!/usr/bin/python
import argparse
import paho.mqtt.client as mqtt
import time
import sys

USER = "user"
PW = "password"
IP = "192.168.0.100"
PORT = 1883

def send_mqtt_message(topic, message):
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(USER, PW)
    client.connect(IP, PORT)
    result, _ = client.publish(topic, message)
    client.disconnect()
    return "OK" if result == mqtt.MQTT_ERR_SUCCESS else "Fehler"

def read_mqtt_message(topic):
    message_received = False

    def on_message(client, userdata, msg):
        nonlocal message_received
        if msg.topic == topic:
            print(msg.payload.decode())
            client.loop_stop()  # stop the loop
            client.disconnect()
            message_received = True

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(USER, PW)
    client.connect(IP, PORT)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_start()

    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < 5:  # 5 seconds timeout
        if message_received:
            sys.exit(0)
        time.sleep(1)  # wait for messages

    print("Timeout")
    client.loop_stop()  # stop the loop
    client.disconnect()

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--topic", help="MQTT topic")
    parser.add_argument("-m", "--message", help="Message to send")
    parser.add_argument("-r", "--read", help="Read messages from topic", action="store_true")
    args = parser.parse_args()


    if args.topic and args.message:
        result = send_mqtt_message(args.topic, args.message)
        print(result)
    elif args.topic and args.read:
        read_mqtt_message(args.topic)
    else:
        print("Missing topic or message argument.")
