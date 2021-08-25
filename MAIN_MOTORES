

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

#-----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------FUNCIONES------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------


#SUSCRIPTOR RECIBE MENSAJES
def sub_cb(topic, msg):
  global motion
  print((topic, msg))
  msg2=b'PRODUCTO ENTREGADO'
  angulo = 45 #90 se detiene #180 cambia sentido de giro
  duty = ((12.346*angulo**2 + 7777.8*angulo + 700000))
  duty /= 1000000
  duty = int(duty*1023/20)
  #Para detener el servo
  duty_p = ((12.346*90**2 + 7777.8*90 + 700000))
  duty_p /= 1000000
  duty_p = int(duty_p*1023/20)
  if topic == b'boton_3' and msg == b'Se encendio el boton_1':
    motion = False
    print('ESP32B prendio el led rojo')
    servo_360_1.duty(duty)
    while True:
      if motion:
        
        print("OFF")
        servo_360_1.duty(duty_p)
        client.publish(b'boton_1', msg2)
        motion = False
        break


  if topic == b'boton_3' and msg == b'Se encendio el boton_2':
    motion = False
    print('ESP32B apago el led azul')
    servo_360_2.duty(duty)
    while True:
      if motion:
        
        print("OFF")
        servo_360_2.duty(duty_p)
        client.publish(b'boton_1', msg2)
        motion = False
        break

  if topic == b'boton_3' and msg == b'Se encendio el boton_3':
    motion = False
    print('ESP32B apago el led naranja')
    servo_360_3.duty(duty)
    while True:
      if motion:
        print("OFF")
        servo_360_3.duty(duty_p)
        client.publish(b'boton_1', msg2)
        motion = False
        break

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
  machine.reset()

#FUNCION QUE ESTABLECE CONEXION CON EL BROKER def connect_and_subscribe():   global client_id, mqtt_server, topic_sub   client = MQTTClient(client_id, mqtt_server)   client.set_callback(sub_cb)   client.connect()   client.subscribe(topic_sub)   print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))   return client #EN CASO DE DESCONEXION O QUE NO SE PUEDE CONECTAR  def restart_and_reconnect():   print('Failed to connect to MQTT broker. Reconnecting...')   time.sleep(10)   machine.reset()
#-----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------PROGRAMA-------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#INTENTA LA CONEXION CON EL BROKER
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()
  
#EJECUTA EL PROGRAMA
i=0
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
while True:
  try:
    client.check_msg()
    msg=b'apagar' 
      #PUBLICACIONES
    if i==1:
      client.publish(topic_pub, msg)
      i=0
      sleep(0.1)

  except OSError as e:
    restart_and_reconnect()
