import paho.mqtt.client as mqtt

from gpiozero import LED

led = LED(17)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("glblcd/mee")
    
    
    
    
    
def on_message(client, userdata, msg):
    msg.topic + " \n " + msg.payload.decode("utf-8") + " \n "
    message = msg.payload.decode("utf-8").lower()
    
    
    if message == "on":
        led.on()
        print("LED is on")
        
    elif message == "off":
        led.off()
        print("LED is off")
    
    
    
    
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message



client.connect("197.255.72.230", 1883, 60)
client.loop_forever()