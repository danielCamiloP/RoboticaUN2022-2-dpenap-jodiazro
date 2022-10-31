from cmath import pi
import rospy
import numpy as np
import math
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        key=input()

        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()

        if key == 'f': #Move to Marker
            aux=[-1.32599689924245,-1.00469765057985,-1.6422,1.2648,-1.7442]
            key=' '
        elif key == 'h': #move to Rest
            aux= point.positions = [-1.32599689924245,-0.724198306509335,-1.6932,1.0098,-1.7442]
            key=' '
        elif key == 'q': #Move to outer arc start
            aux= point.positions = [-1.9482,-1.3362,-1.7442,1.6218,-1.7442]
            key=' '
        elif key == 'w': #Move to outer arc end
            aux= point.positions = [1.8258,-1.3362,-1.7442,1.6218,-1.7442]
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
        elif key == 'p': #close gripper:
            aux=[-1.32599689924245,-1.00469765057985,-1.6422,1.2648,-1.7442]
            key=' '
        elif key == 'o': #open gripper:
            aux=[-1.32599689924245,-1.00469765057985,-1.6422,1.2648,-1.1832]
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

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass


