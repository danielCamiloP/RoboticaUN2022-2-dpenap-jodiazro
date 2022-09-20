# Comentarios realizados para entender mejor el codigo

from pynput.keyboard import Key, Listener #libreria para leer input del teclado
import rospy #libreria de ros para python
from geometry_msgs.msg import Twist #permite crear mensajes de tipo Twist

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

def on_press(key): #on_press detecta cualquier tecla presionada
    if key == Key.space: #si la tecla fue espacio
        pubVel(0,1,2.2) 

def on_release(key): #detecta si se soltó esc para poder finalizar la ejecución
    if key == Key.esc:
        return False

if __name__ == '__main__':
    pubVel(0,0,0.1)
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except rospy.ROSInterruptException:
        pass


