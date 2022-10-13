"""
Allows to use the service dynamixel_command 
"""
from cmath import pi

from Laboratorio 4.dynamixel_one_motor.scripts.jointPub import joint_publisher
import rospy
import time
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand


#Joint Setup
jointCommand('', 1, 'Torque_Limit', 400, 0)
jointCommand('', 2, 'Torque_Limit', 400, 0)
jointCommand('', 3, 'Torque_Limit', 400, 0)
jointCommand('', 4, 'Torque_Limit', 400, 0)
jointCommand('', 5, 'Torque_Limit', 400, 0)

cycleNumber = 2

while(cycleNumber>0):
    # Home Position
    jointCommand('', 1, 'Goal_position', 0, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 2, 'Goal_position', 0, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 3, 'Goal_position', 0, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 4, 'Goal_position', 0, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 5, 'Goal_position', 0, 0.5)
    joint_publisher()
    time.sleep(2)

    # Goal Position [45 30 10 -15 0]
    jointCommand('', 1, 'Goal_position', pi/4, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 2, 'Goal_position', pi/6, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 3, 'Goal_position', pi/12, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 4, 'Goal_position', -pi/12, 0.5)
    joint_publisher()
    time.sleep(0.5)
    jointCommand('', 5, 'Goal_position', 0, 0.5)
    joint_publisher()
    time.sleep(2)

    cycleNumber = cycleNumber - 1
