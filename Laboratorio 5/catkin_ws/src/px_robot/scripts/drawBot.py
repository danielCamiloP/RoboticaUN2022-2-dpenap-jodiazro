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
from iKinePincher import getQLine,iKine,getQArc

pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
rospy.init_node('joint_publisher', anonymous=False)

loaded = False
n = 5
grip = -1.7442
loose = -1.1832
z_up = 120.8719
z_down = 33.3882

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



def drawParallelLines():
    x_in = [212.701, 134.919, 198.559]
    y_in = [188.059, 251.698, 173.916]
    
    x_f = [141.990, 205.630, 127.848]
    y_f = [258.769, 180.988, 244.627]
    
    for i in range(3):
        q_in = iKine(x_in[i], y_in[i],z_up,0)
        q_draw = getQLine(n, x_in[i], y_in[i],x_f[i], y_f[i],z_down)
        q_out = iKine(x_f[i], y_f[i],z_up,0)
        
        q = np.concatenate((q_in,q_draw,q_out),axis=1)
    
        for j in range(q.shape[1]):
            move(q[0,j],q[1,j],q[2,j],q[3,j],grip)
    

def drawInitials():
    x_J = [289.865,264.865,259.865,259.865]
    y_J = [-37.016,-37.016,-32.016,-17.016]
    R = 5
    
    q_in = iKine(x_J[0],y_J[0],z_up)
    q_draw1 = getQLine(n,x_J[0],y_J[0],x_J[1],y_J[1],z_down)
    q_draw2 = getQArc(n,R,x_J[1],y_J[1],x_J[2],y_J[2],z_down,False)
    q_draw3 = getQLine(n,x_J[2],y_J[2],x_J[3],y_J[3],z_down)
    q_out = iKine(x_J[3],y_J[3],z_up)
    
    q = np.concatenate((q_in,q_draw1,q_draw2,q_draw3,q_out),axis=1)
    
    for i in range(q.shape[1]):
        move(q[0,i],q[1,i],q[2,i],q[3,i],grip)
    
    
    x_D = [259.865,289.865,289.865,284.865,264.865,259.865]
    y_D = [-47.016,-47.016,-62.016,-67.016,-67.016,-62.016]
    
    q_in = iKine(x_D[0],y_D[0],z_up)
    q_draw1 = getQLine(n,x_D[0],y_D[0],x_D[1],y_D[1],z_down)
    q_draw2 = getQLine(n,x_D[1],y_D[1],x_D[2],y_D[2],z_down)
    q_draw3 = getQArc(n,R,x_D[2],y_D[2],x_D[3],y_D[3],z_down,False)
    q_draw4 = getQLine(n,x_D[3],y_D[3],x_D[4],y_D[4],z_down)
    q_draw5 = getQArc(n,R,x_D[4],y_D[4],x_D[5],y_D[5],z_down,False)
    q_draw6 = getQLine(n,x_D[5],y_D[5],x_D[0],y_D[0],z_down)
    
    q = np.concatenate((q_in,q_draw1,q_draw2,q_draw3,q_draw4,q_draw5,q_draw6,q_in),axis=1)
    
    for i in range(q.shape[1]):
        move(q[0,i],q[1,i],q[2,i],q[3,i],grip)

def drawShapes():
    
    x_tri = [264.641,230.000,230.000]
    y_tri = [130.000,110.000,150.000]
    
    q_in = iKine(x_tri[0], y_tri[0],z_up,0)
    
    q_draw1 = getQLine(n, x_tri[0], y_tri[0],x_tri[1], y_tri[1],z_down)
    q_draw2 = getQLine(n, x_tri[1], y_tri[1],x_tri[2], y_tri[2],z_down)
    q_draw3 = getQLine(n, x_tri[2], y_tri[2],x_tri[0], y_tri[0],z_down)
    
    q = np.concatenate((q_in,q_draw1,q_draw2,q_draw3,q_in),axis=1)
    
    for i in range(q.shape[1]):
        move(q[0,i],q[1,i],q[2,i],q[3,i],grip)
        
    x_sq = [247.449,287.449,287.449,247.449]
    y_sq = [97.080,97.080,57.080,57.080]
    
    q_in = iKine(x_sq[0], y_sq[0],z_up,0)
    q_draw1 = getQLine(n, x_sq[0], y_sq[0],x_sq[1], y_sq[1],z_down)
    q_draw2 = getQLine(n, x_sq[1], y_sq[1],x_sq[2], y_sq[2],z_down)
    q_draw3 = getQLine(n, x_sq[2], y_sq[2],x_sq[3], y_sq[3],z_down)
    q_draw4 = getQLine(n, x_sq[3], y_sq[3],x_sq[0], y_sq[0],z_down)
    
    q = np.concatenate((q_in,q_draw1,q_draw2,q_draw3,q_in),axis=1)
    
    for i in range(q.shape[1]):
        move(q[1,i],q[2,i],q[3,i],q[4,i],grip)
    
    x_circ = [262.576, 290.861]
    y_circ = [8.738,37.023]
    R = 20
    
    q_in = iKine(x_circ[0], y_circ[0],z_up,0)
    q_draw1 = getQArc(n, R, x_circ[0], y_circ[0],x_circ[1], y_circ[1],z_down,False)
    q_draw2 = getQArc(n, R, x_circ[1], y_circ[1],x_circ[0], y_circ[0],z_down,False)

    q = np.concatenate((q_in,q_draw1,q_draw2,q_in),axis=1)
    
    for i in range(q.shape[1]):
        move(q[0,i],q[1,i],q[2,i],q[3,i],grip)
    
    
def drawDots():
    x = [240.198, 255.430, 215.552, 240.198, 215.552]
    y = [-129.894, -150.859, -137.902, -171.824, -163.816]
    
    for i in range(len(x)):
        q_in = iKine(x[i], y[i],z_up,0)
        q_draw = iKine(x[i], y[i],z_down,0)
        
        q = np.concatenate((q_in,q_draw,q_in),axis=1)
        
        for j in range(q.shape[1]):
            move(q[0,j],q[1,j],q[2,j],q[3,j],grip)
        
    
    
def drawSus():
    x_out = [238.108, 238.108, 238.108, 250.968, 256.318, 254.374, 262.113, 259.620,
             273.863, 277.786, 273.863, 259.620, 262.113, 254.374, 256.318, 250.968]
    y_out = [-108.869, -102.303,  -95.736, -99.688, -86.314, -86.314, -99.039, -96.011,
             -102.303, -108.595, -105.566, -118.291, -118.291, -104.918,-104.918,-108.869]
    R = [-1,-1,27.8267,-1, 34.6471,-1, 41.0786, 14.0250, 6.7098,
         6.7098, 14.0250, 41.0786,-1, 34.6471,-1, 27.8267]
    CCW = [-1,-1,True,-1,True,-1,True,False,False,False,False,True,-1,True,-1,True]
    l_ = len(R)
    
    q_in = iKine(x_out[0],y_out[0],z_up,0)
    q = q_in
    
    for i in range(l_):
        if R == -1:
            q_draw = getQLine(n, x_out[i], y_out[i],x_out[np.mod(l_,i+1)], y_out[np.mod(l_,i+1)],z_down)
        else:
            q_draw = getQArc(n,R[i],x_out[i], y_out[i],x_out[np.mod(l_,i+1)], y_out[np.mod(l_,i+1)],z_down,CCW[i])
        q = np.concatenate((q,q_draw),axis=1)
        
     
    q = np.concatenate((q,q_in),axis=1)
    
    for j in range(q.shape[1]):
        move(q[0,j],q[1,j],q[2,j],q[3,j],grip)
        
    x_in = [262.263, 269.747, 273.649, 269.747]
    y_in = [-102.303, -98.866, -102.303, -105.740]
    
    R = [9.0758, 3.5447, 3.5447, 9.0758]
    CCW = [False,False,False,False]
    
    q_in = iKine(x_in[0],y_in[0],z_up,0)
    q = q_in
    
    for i in range(l_):
        if R == -1:
            q_draw = getQLine(n, x_in[i], y_in[i],x_in[np.mod(l_,i+1)], y_in[np.mod(l_,i+1)],z_down)
        else:
            q_draw = getQArc(n,R[i],x_in[i], y_in[i],x_in[np.mod(l_,i+1)], y_in[np.mod(l_,i+1)],z_down,CCW[i])
        q = np.concatenate((q,q_draw),axis=1)
    
    q = np.concatenate((q,q_in),axis=1)
    
    for j in range(q.shape[1]):
        move(q[0,j],q[1,j],q[2,j],q[3,j],grip)
    
def move(q1,q2,q3,q4,q5):
    aux= point.positions = [q1,q2,q3,q4,q5]
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
