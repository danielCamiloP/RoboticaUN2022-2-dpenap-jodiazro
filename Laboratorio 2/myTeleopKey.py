# Requerimientos: Movimiento adelante atras con W y S. Movimiento horario antihorario D y A. Reiniciar la tortuga con R. Giro de 180 con Espacio

from pynput.keyboard import Key, Listener, KeyCode #libreria para leer input del teclado
import rospy #libreria de ros para python
from geometry_msgs.msg import Twist #permite crear mensajes de tipo Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi

def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #creacion de un publisher para poder modificar el movimiento de la tortuga
    rospy.init_node('velPub', anonymous=False) #inicializacion de velPub para uso con Python 
    vel = Twist() #declaracion del mensaje a enviar a cmd_vel
    vel.linear.x = vel_x #Declaracion de la velocidad de la tortuga
    vel.angular.z = ang_z #declaracion del angulo de la tortuga
    rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t) #Creacion de un delay 
    while rospy.Time.now() < endTime:
        pub.publish(vel) #envio del mensaje

# def relTp(lin_x, rot_z, t):
#     relCl = rospy.client('/turtle1/teleport_relative', client, queue_size=10) #creacion de un publisher para poder modificar el movimiento de la tortuga
#     rospy.init_node('velPub', anonymous=False) #inicializacion de velPub para uso con Python 
#     vel = Twist() #declaracion del mensaje a enviar a cmd_vel
#     vel.linear.x = vel_x #Declaracion de la velocidad de la tortuga
#     vel.angular.z = ang_z #declaracion del angulo de la tortuga
#     #rospy.loginfo(vel)
#     endTime = rospy.Time.now() + rospy.Duration(t) #Creacion de un delay 
#     while rospy.Time.now() < endTime:
#         pub.publish(vel) #envio del mensaje

# def relTp(lin_x, rot_z, t):
#     pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #creacion de un publisher para poder modificar el movimiento de la tortuga
#     rospy.init_node('velPub', anonymous=False) #inicializacion de velPub para uso con Python 
#     vel = Twist() #declaracion del mensaje a enviar a cmd_vel
#     vel.linear.x = vel_x #Declaracion de la velocidad de la tortuga
#     vel.angular.z = ang_z #declaracion del angulo de la tortuga
#     #rospy.loginfo(vel)
#     endTime = rospy.Time.now() + rospy.Duration(t) #Creacion de un delay 
#     while rospy.Time.now() < endTime:wa
#         pub.publish(vel) #envio del mensaje

ts = 0.1

def on_press(key): #on_press detecta cualquier tecla presionada
    if key == KeyCode.from_char('w'): #si la tecla fue w
        print("avanzando")
        pubVel(1,0,ts) #mover la tortuga una  unidad en 0.5 segundos, sin rotacion
        
    if key == KeyCode.from_char('s'): #si la tecla fue s
        print("retrocediendo")
        pubVel(-1,0,ts) #mover la tortuga menos una unidad en 0.5 segundos, sin rotacion
        
    if key == KeyCode.from_char('a'): #si la tecla fue a
        print("girando cw")
        pubVel(0,0.2,ts) #rotar la tortuga cw
        
    if key == KeyCode.from_char('d'): #si la tecla fue d
        print("girando ccw")
        pubVel(0,-0.2,ts) #rotar la tortuga ccw
        
    if key == Key.space: #si la tecla fue espacio
        print("girando 180")
    #     (0,pi/2,0.5) #rotar la tortuga 180 usando el servicio TeleportRelative
    if key == KeyCode.from_char('r'): #si la tecla fue r
        print("reiniciando")

    #     (5.54444, 5.5444, 0, 0.1) #rotar la tortuga a 0, moverla al centro de la pantalla usando TeleportRelative
    #     #clear al trazo de la tortuga
    #     pubVel(0,0,0.1)#colocar cmd_vel en ceros

def on_release(key): #detecta si se soltó alguna tecla
    if key == Key.esc: #tecla esc presionada
        return False #salir del programa

if __name__ == '__main__': #manejo de interrupciones dentro de ROS
    pubVel(0,0,ts) #mantiene tiempo en simulación
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except rospy.ROSInterruptException:
        pass

'''    
def teleport(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
        print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))
def teleportRel(x,ang):
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp1 = teleportR(x, ang)
        
    except rospy.ServiceException:
        pass
'''    
