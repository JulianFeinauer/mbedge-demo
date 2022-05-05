import json
import os

import paho.mqtt.client as mqtt
from sqlalchemy import create_engine

HOST = os.environ.get("MQTT", "mqtt.eclipseprojects.io")
PORT = os.environ.get("MQTT_PORT", 1883)
DATABASE = os.environ.get("DATABASE", "postgresql://postgres:password@localhost:5432/postgres")

if __name__ == '__main__':
    # Connect to Database
    # Start via

    db = create_engine(DATABASE)

    # Create
    db.execute("""CREATE TABLE IF NOT EXISTS conditions
(
    time        TIMESTAMPTZ      NOT NULL,
    motor_current    DOUBLE PRECISION NOT NULL,
    machine_position DOUBLE PRECISION NOT NULL,
    random    DOUBLE PRECISION NOT NULL
);""")
    # db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

    client = mqtt.Client()


    def subscribe_callback(client, userdata, mid, granted_qos, properties=None):
        print(f"Subscribed to {userdata}")


    def on_connect(client, userdata, flags, rc):
        print("MQTT Broker connected!")
        client.subscribe("portal-test/#")


    def on_message(client, userdata, msg: mqtt.MQTTMessage):
        msg_topic = msg.topic
        message = msg.payload.decode('ascii')
        json_message = json.loads(message)
        print(f"Got message on {msg_topic}: {message} / {json_message}")
        db.execute(f"INSERT INTO conditions (time, motor_current, machine_position, random) VALUES (NOW(), {json_message['motor-current']}, {json_message['position']}, {json_message['rand_val']})")

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = subscribe_callback
    client.connect_async(HOST, PORT, 60)

    client.loop_forever(
        timeout=1.0, max_packets=1, retry_first_connection=False
    )


