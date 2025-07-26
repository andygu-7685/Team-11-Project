from connections import connect_mqtt, connect_internet
from time import sleep
from DHTsensor import DHTRead
from LDRsensor import LDRRead
from ultra import ultra


def cb(topic, msg):
    if topic == b"text":
        print(msg.decode())


def main():
    try:
        connect_internet("",password="") #ssid (wifi name), pass
        client = connect_mqtt("", "", "") # url, user, pass

        client.set_callback(cb)
        client.subscribe("text")

        counter=0
        while True:
            client.check_msg()
            client.publish("temp", DHTRead(1))
            sleep(0.1)
            counter+=1
            if (counter == 100):
                client.publish("response", "Hello from the pico!")

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()



