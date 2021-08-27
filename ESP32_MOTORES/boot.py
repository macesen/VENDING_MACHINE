import time
from time import sleep,sleep_ms
from umqttsimple import MQTTClient
import ubinascii
import machine
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
topic_pub = b'boton_1'
#CREACION DE PUBLICADORES---------------------------------------------------------------------
topic_sub = b'boton_3'
#---------------------------------------------------------------------------------------------

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
#CONEXION CON LA  RED------------------------------------------------------------------------
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())   

#SERVOS
servo_360_1 = PWM(Pin(17))
servo_360_1.freq(50)


servo_360_2 = PWM(Pin(16))
servo_360_2.freq(50)


servo_360_3 = PWM(Pin(5))
servo_360_3.freq(50)  
# PIR
pir=Pin(14,Pin.IN)
