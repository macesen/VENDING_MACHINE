from umqttsimple import MQTTClient
import ubinascii
from machine import Pin,PWM,reset,unique_id,I2C
import micropython
import network
import utime
import esp
import ssd1306
from time import sleep,sleep_ms




esp.osdebug(None)
import gc
gc.collect()

ssid = 'RED'  #Nombre de la Red
password = 'CLAVE' #Contrase甯絘 de la red
mqtt_server = 'broker.emqx.io'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(unique_id())
topic_sub = b'boton_1'
topic_pub = b'boton_3'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig()) 

pir=Pin(14,Pin.IN) 
PIND = Pin(15, Pin.IN)
PIND2=Pin(0, Pin.IN)
led=Pin(2,Pin.OUT) 
PIND3=Pin(5, Pin.IN)
buzzer=PWM(Pin(23,Pin.OUT))
buzzer.init(freq=0,duty=0)
