from connections import connect_mqtt, connect_internet
from time import sleep
import constants
from DHTsensor import DHTRead
from LDRsensor import LDRRead
from ultra import ultra
from OLED import OLEDShow




def cb(topic, msg):
    if topic == b"text":
        print(msg.decode())
        
    if topic == b"user_input":
        OLEDShow(msg.decode())


def main():
    try:
        connect_internet("TP-LINK_175B",password="07661174") #ssid (wifi name), pass
        client = connect_mqtt("af9d745144ae47e2bd0393dab5fe6d46.s1.eu.hivemq.cloud", "andygu1066", "Ab883539@") # url, user, pass

        client.set_callback(cb)
        client.subscribe("text")
        client.subscribe("user_input")
        OLEDShow("HAcK 2025\n Day2\n")

        counter=0
        while True:
            client.check_msg()
            
            temperature = DHTRead(1)
            client.publish("temp", f"{temperature:.3f}")

            brightness = LDRRead()
            client.publish("light", f"{brightness:.3f}")

            humidity = DHTRead(3)
            client.publish("humidity", f"{humidity:.3f}")

            distance = ultra()
            client.publish("ultrasonic", f"{distance:.3f}")
            
            sleep(0.1)
            counter+=1
            if (counter == 100):
                client.publish("response", "Hello from the pico!")

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()




