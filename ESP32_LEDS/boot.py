import time
from time import sleep,sleep_ms
from umqttsimple import MQTTClient
import ubinascii
import machine,neopixel
import micropython
from machine import Pin,PWM
import network
import esp
import utime
esp.osdebug(None)
import gc
gc.collect()

#CONEXION Y CLAVE DE INTERNET----------------------------------------------------------------
ssid = 'red'
password = 'clave'
#CONEXION AL BROKER, SIEMPRE USAR 'broker.emqx.io'--------------------------------------------
mqtt_server = 'broker.emqx.io'
client_id = ubinascii.hexlify(machine.unique_id())
#CREACION DE SUSCRIPTORES---------------------------------------------------------------------
#topic_pub = b'boton_1'
#CREACION DE PUBLICADORES---------------------------------------------------------------------
topic_sub = b'boton_1'

#---------------------------------------------------------------------------------------------

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
#CONEXION CON LA  RED------------------------------------------------------------------------
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())   

# number of pixels
n = 8
# strip control gpio
p = 14
p2=12
p3=27
np = neopixel.NeoPixel(machine.Pin(p), n)
np2 = neopixel.NeoPixel(machine.Pin(p2), n)
np3 = neopixel.NeoPixel(machine.Pin(p3), n)
