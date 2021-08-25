from machine import Pin,PWM,reset
from time import sleep,ticks_ms
x=0
motion=0
contador=0 
dt=1000
dinero=0
control=1
i=0

i2c=I2C(-1,scl=Pin(22),sda=Pin(21))
oled_width=128
oled_height=64
oled=ssd1306.SSD1306_I2C(oled_width,oled_height,i2c)
def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'boton_1' and msg == b'PRODUCTO ENTREGADO':
    cancion()
    oled.fill(1)
    oled.fill(0)
    oled.text("PRODUCTO LISTO!",12,20)
    oled.show()
    sleep(1)
    oled.fill(1)    
    print("PON ALGO POR PANTALLA")
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  reset()
def cancion():
    buzzer.freq(2637) #E7
    buzzer.duty(512)#volumen
    sleep_ms(150)
    buzzer.freq(2637) #E7
    buzzer.duty(512)#volumen
    sleep_ms(150)
    buzzer.freq(0) #0
    buzzer.duty(512)#volumen
    sleep_ms(150)
    buzzer.freq(2637) #E7
    buzzer.duty(512)#volumen
    sleep_ms(150)  
    buzzer.freq(0) #0
    buzzer.duty(512)#volumen
    sleep_ms(150)
    buzzer.freq(2093) #C7
    buzzer.duty(512)#volumen
    sleep_ms(150)  
    buzzer.freq(2637) #E7
    buzzer.duty(512)#volumen
    sleep_ms(150) 
    buzzer.freq(0) #0
    buzzer.duty(512)#volumen
    sleep_ms(150)
    buzzer.freq(3136) #G7
    buzzer.duty(512)#volumen
    sleep_ms(150) 
    buzzer.freq(0) #0
    buzzer.duty(512)#volumen
    sleep_ms(450)
    buzzer.freq(1568) #G6
    buzzer.duty(512)#volumen
    sleep_ms(150) 
    buzzer.duty(0)#volumen         
def handle_interrupt(pin):      
  global x
  x=3
  led.value(not led.value())    
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt) 

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()
#Programa principal
while True:
  try:
    client.check_msg()
    oled.fill(0)
    oled.text("INTRODUZCA 0.50$",1,20)
    oled.show()
    sleep(1)
    oled.fill(1)
    msg=b'NO'    
    if x==3:
      buzzer.freq(1047) #DO
      buzzer.duty(512)#volumen
      sleep(0.5)
      buzzer.duty(0)#volumen
      contador+=1
      dinero=dinero+0.5
      oled.fill(0)
      print("El monto total de su monedero es de:",0.5*contador,"$")
      oled.text("INGRESO "+str(0.5*contador)+"$",17,20)
      oled.show()
      sleep(1)
      oled.fill(1)
    x=0
    if PIND.value()==0 and dinero>0:
      contador=0.5*contador-0.5
      oled.fill(0)
      print("Monto a retirar:",contador,"$")
      print("Usted ha seleccionado el producto Don Brown")
      msg =b'Se encendio el boton_1'
      client.publish(topic_pub, msg)
      oled.text("Eligio Manjar ",0,20)
      oled.show()
      sleep(1)
      i=1
      contador=0
      dinero=dinero-0.5
    if PIND2.value()==0 and dinero>0:
      contador=0.5*contador-1
      oled.fill(0)
      print("Monto a retirar:",contador,"$")
      print("Usted ha seleccionado brownies")
      msg=b'Se encendio el boton_2'
      client.publish(topic_pub, msg)
      oled.text("Eligio Brownies",8,20)
      oled.show()
      sleep(1)
      i=1
      contador=0
      dinero=dinero-0.5
    if PIND3.value()==0 and dinero>0:
      contador=0.5*contador-1
      oled.fill(0)
      print("Monto a retirar:",contador,"$")
      print("Usted ha seleccionado biri")
      msg=b'Se encendio el boton_3'
      client.publish(topic_pub, msg)
      oled.text("Eligio Koki",8,20)
      oled.show()
      sleep(1)
      i=1
      contador=0
      dinero=dinero-0.5
      sleep(0.1)
  except OSError as e:
    restart_and_reconnect()
