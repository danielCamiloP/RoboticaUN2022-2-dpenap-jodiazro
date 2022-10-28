## Codigo para robot dibujante
# Rutinas
# Tecla L - Tomar o dejar el marcador en la base
# Tecla Q - Dibujar espacio de trabajo (Diestro)
# Tecla W - Dibujar Iniciales
# Tecla E - Dibujar Figuras geometricas (triangulo equilatero, circulo, 3 rectas paralelas)
# Tecla R - Dibujar puntos equidistantes (5 Puntos)
# Tecla T - Dibujar un mongo

import rospy
from cmath import pi
import numpy as np
import math
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrayectory, JointTrajectoryPoint


pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
rospy.init_node('joint_publisher', anonymous=False)

loaded = False


while not rospy.is_shutdown():
    key=input()

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()

    goRest()
    if loaded:
        if key == 'l':
            leaveMarker()
            key=' '
        elif key == 'q': #pos 1 0 0 0 0 0
            aux= point.positions = [0,0,0,0,0]
            key=' '
        elif key == 'w': #pos 2 -20 20 -20 20 0
            aux= point.positions = [-20*pi/180,20*pi/180,-20*pi/180,20*pi/180,0]
            key=' '
        elif key == 'e': #pos 3 30 -30 30 -30 0
            aux= point.positions = [30*pi/180,-30*pi/180,30*pi/180,-30*pi/180,0]
            key=' '
        elif key == 'r': #pos 4 -90 15 -55 17 0
            aux= point.positions = [-90*pi/180,15*pi/180,-55*pi/180,17*pi/180,0]
            key=' '
        elif key == 't': #pos 5 -90 45 -55 45 10
            aux= point.positions = [-90*pi/180,45*pi/180,-55*pi/180,45*pi/180,10*pi/180]
            key=' '

    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [0.25, 0, 0, 0, 1.3]    
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def goRest():
    aux= point.positions = [0,0,-pi/2,0,0]
    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def takeMarker():
    aux= point.positions = [0,0,-pi/2,0,0]
    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def leaveMarker():
    aux= point.positions = [0,0,-pi/2,0,0]
    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def drawInitials():
    aux= point.positions = [0,0,-pi/2,0,0]
    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def drawShapes():
    aux= point.positions = [0,0,-pi/2,0,0]
    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)
    
def drawDots():
    aux= point.positions = [0,0,-pi/2,0,0]
    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)
    
def drawSus():
    aux= point.positions = [0,0,-pi/2,0,0]
    point.positions = aux
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)
    
def mapAngle(analogVal):
    #512 - 0
    #820 - +pi
    #204 - -pi
    m = pi/(512-204)
    b = pi-m*820
    radVal = analogVal*m + b
    
    return radVal
