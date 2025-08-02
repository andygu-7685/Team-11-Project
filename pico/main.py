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
        
    if topic == b"user_input" and constants.BADGE != 1:
        OLEDShow(msg)


def main():
    try:
        connect_internet("HAcK-Project-WiFi-1",password="UCLA.HAcK.2024.Summer") #ssid (wifi name), pass
        client = connect_mqtt("af9d745144ae47e2bd0393dab5fe6d46.s1.eu.hivemq.cloud", "andygu1066", "Ab883539@") # url, user, pass

        client.set_callback(cb)
        client.subscribe("text")
        client.subscribe("user_input")
        OLEDShow("HAcK 2025\n Day2\n")

        counter=0
        while True:
            client.check_msg()
            
            if constants.BADGE == 1:
                temperature = DHTRead(1)
                client.publish("temp", temperature)

                brightness = LDRRead()
                client.publish("light", brightness)

                humidity = DHTRead(3)
                client.publish("humidity", humidity)
            
            else:
                distance = ultra()
                #print(f"{distance:.3f} cm")
                client.publish("ultrasonic", f"{distance:.3f}")
            
            sleep(0.1)
            counter+=1
            if (counter == 100):
                client.publish("response", "Hello from the pico!")

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()




