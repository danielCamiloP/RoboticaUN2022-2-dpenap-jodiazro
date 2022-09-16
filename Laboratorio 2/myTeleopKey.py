# Requerimientos: Movimiento adelante atras con W y S. Movimiento horario antihorario D y A. Reiniciar la tortuga con R. Giro de 180 con Espacio

from pynput.keyboard import Key, Listener #libreria para leer input del teclado
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
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t) #Creacion de un delay 
    while rospy.Time.now() < endTime:
        pub.publish(vel) #envio del mensaje

def relTp(lin_x, rot_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #creacion de un publisher para poder modificar el movimiento de la tortuga
    rospy.init_node('velPub', anonymous=False) #inicializacion de velPub para uso con Python 
    vel = Twist() #declaracion del mensaje a enviar a cmd_vel
    vel.linear.x = vel_x #Declaracion de la velocidad de la tortuga
    vel.angular.z = ang_z #declaracion del angulo de la tortuga
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t) #Creacion de un delay 
    while rospy.Time.now() < endTime:
        pub.publish(vel) #envio del mensaje

#tecla  w
def on_press(key): #on_press detecta cualquier tecla presionada
    if key == 'w': #si la tecla fue a
        pubVel(1,0,0.5) #mover la tortuga una  unidad en 0.5 segundos, sin rotacion
        print("w!")

#tecla s
def on_press(key): 
    if key == 'w': #si la tecla fue s
        pubVel(-1,0,0.5) #mover la tortuga menos una unidad en 0.5 segundos, sin rotacion
        print("s!")
#tecla a
def on_press(key): 
    if key == 'a': #si la tecla fue a
        pubVel(0,pi/10,0.5) #rotar la tortuga pi/10
        print("a!")
#tecla d
def on_press(key): 
    if key == 'd' : #si la tecla fue d
        pubVel(0.1,0,0.5) #rotar la tortuga -pi/10
        print("d!")
#tecla espacio
def on_press(key): 
    if key == Key.space: #si la tecla fue espacio
        pubVel(0.1,0,0.5) #rotar la tortuga 180 usando el servicio TeleportRelative

def on_release(key): #detecta si se soltó esc para poder finalizar la ejecución
    if key == Key.esc:
        return False

if __name__ == '__main__': #manejo de interrupciones dentro de ROS
    pubVel(0,0,0.1)
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except rospy.ROSInterruptException:
        pass
