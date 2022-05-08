from py_mqtt import cameramqtt
if __name__ == "__main__":
    try:
        camera = cameramqtt()
        camera.mqtt_connect()
    except KeyboardInterrupt:
        pass
    finally:
        pass