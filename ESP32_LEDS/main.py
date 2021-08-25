red,green,blue=125,125,125
red2,green2,blue2=125,125,125
red3,green3,blue3=125,125,125
def clear ():
  for i in range (n):
    np[i]=(0,0,0)
    np.write()

def clear2 ():
  for i in range (n):
    np2[i]=(0,0,0)
    np2.write()

def clear3 ():
  for i in range (n):
    np3[i]=(0,0,0)
    np3.write()

# set strip color
def set_color(r, g, b):
  for i in range(n):
    np[i] = (r, g, b)
    np.write()

def set_color2(r, g, b):
  for i in range(n):
    np2[i] = (r, g, b)
    np2.write()
def set_color3(r, g, b):
  for i in range(n):
    np3[i] = (r, g, b)
    np3.write()
# cycle
def cycle(r, g, b,r2, g2, b2,r3, g3, b3,wait):
  for i in range(4 * n):
    for j in range(n):
      np[j] = (0, 0, 0)
      np2[j] = (0, 0, 0)
      np3[j] = (0, 0, 0)
    np[i % n] = (r, g, b)
    np2[i % n] = (r2, g2, b2)
    np3[i % n] = (r3, g3, b3)
    np.write()
    np2.write()
    np3.write()
    time.sleep_ms(wait)



#-----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------FUNCIONES------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------
#clear()
#set_color(r, g, b)
# time.sleep(1)

#SUSCRIPTOR RECIBE MENSAJES
def sub_cb(topic, msg):
  global red,green,blue,red2,green2,blue2,red3,green3,blue3
  print((topic, msg))
# Extras
  if topic == b'boton_1' and msg == b'PRODUCTO ENTREGADO':
    print("Producto listo")
    clear()
    clear2()
    clear3()
    cycle(46,89,205,255,255,0,255,0,0, 50)
    clear()
    clear2()
    clear3()
    set_color(red,green,blue)
    set_color2(red2,green2,blue2)
    set_color3(red3,green3,blue3)
  
#TIRA 1 
  if topic == b'boton_1' and msg == b'Blue':
    print ("Azul activado")
    clear()
    set_color(0, 101, 255)
    red,green,blue=0, 101, 255
    sleep(1)
    
  if topic == b'boton_1' and msg == b'Red':
    print ("Rojo activado")
    clear()
    set_color(222, 45, 35)
    red,green,blue=222, 45, 35
    sleep(1)
    
  if topic == b'boton_1' and msg == b'Purple':
    print ("Purpura activado")
    clear()
    set_color(96, 35, 222)
    red,green,blue=96, 35, 222
    sleep(1) 
  if topic == b'boton_1' and msg == b'Yellow':
    print ("Yellow activado")
    clear()
    set_color(255, 255, 0)
    red,green,blue=255, 255, 0
    sleep(1)     
  if topic == b'boton_1' and msg == b'Green':
    print ("Green activado")
    clear()
    set_color(92, 246, 77)
    red,green,blue=92, 246, 77
    sleep(1)    
  if topic == b'boton_1' and msg == b'Orange':
    print ("Orange activado")
    clear()
    set_color(255, 152, 0)
    red,green,blue=255, 152, 0
    sleep(1)  
#TIRA 2
  if topic == b'boton_1' and msg == b'Blue2':
    print ("Azul2 activado")
    clear2()
    set_color2(0, 101, 255)
    red2,green2,blue2=0, 101, 255
    sleep(1)
  if topic == b'boton_1' and msg == b'Red2':
    print ("Rojo2 activado")
    clear2()
    set_color2(222, 45, 35)
    red2,green2,blue2=222, 45, 35
    sleep(1)    
  if topic == b'boton_1' and msg == b'Purple2':
    print ("Purpura2 activado")
    clear2()

    set_color2(96, 35, 222)
    red2,green2,blue2=96, 35, 222
    sleep(1)     
  if topic == b'boton_1' and msg == b'Yellow2':
    print ("Yellow2 activado")
    clear2()
    set_color2(255, 255, 0)
    red2,green2,blue2=255, 255, 0
    sleep(1)      
  if topic == b'boton_1' and msg == b'Green2':
    print ("Green2 activado")
    clear2()
    set_color2(92, 246, 77)

    red2,green2,blue2=92, 246, 77
    sleep(1)       
  if topic == b'boton_1' and msg == b'Orange2':
    print ("Orange2 activado")
    clear2()
    set_color2(255, 152, 0)
    red2,green2,blue2=255, 152, 0
    sleep(1)     
#TIRA 3
  if topic == b'boton_1' and msg == b'Blue3':
    print ("Azul2 activado")
    clear3()
    set_color3(0, 101, 255)
    red3,green3,blue3=0, 101, 255
    sleep(1)
  if topic == b'boton_1' and msg == b'Red3':
    print ("Rojo2 activado")
    clear3()
    set_color3(222, 45, 35)
    red3,green3,blue3=222, 45, 35
    sleep(1)    
  if topic == b'boton_1' and msg == b'Purple3':
    print ("Purpura2 activado")
    clear3()
    set_color3(96, 35, 222)
    red3,green3,blue3=96, 35, 222
    sleep(1)     
  if topic == b'boton_1' and msg == b'Yellow3':
    print ("Yellow2 activado")
    clear3()
    set_color3(255, 255, 0)
    red3,green3,blue3=255, 255, 0
    sleep(1)      
  if topic == b'boton_1' and msg == b'Green3':
    print ("Green2 activado")
    clear3()
    set_color3(92, 246, 77)
    red3,green3,blue3=92, 246, 77
    sleep(1)       
  if topic == b'boton_1' and msg == b'Orange3':
    print ("Orange2 activado")
    clear3()
    set_color3(255, 152, 0)
    red3,green3,blue3=255, 152, 0
    sleep(1)     
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

while True:
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()
