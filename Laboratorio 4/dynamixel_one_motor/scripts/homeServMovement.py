"""
Allows to use the service dynamixel_command 
"""
from cmath import pi

# import joint_Pub
from jointSrv import jointCommand
from jointPub import joint_publisher
import rospy
import time
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand


# Joint Setup
jointCommand('', 1, 'Torque_Limit', 400, 0)
jointCommand('', 2, 'Torque_Limit', 400, 0)
jointCommand('', 3, 'Torque_Limit', 400, 0)
jointCommand('', 4, 'Torque_Limit', 400, 0)
jointCommand('', 5, 'Torque_Limit', 400, 0)
# Funciona

# #apagado de torques
# jointCommand('', 1, 'Torque_Limit', 0, 0)
# jointCommand('', 2, 'Torque_Limit', 0, 0)
# jointCommand('', 3, 'Torque_Limit', 0, 0)
# jointCommand('', 4, 'Torque_Limit', 0, 0)
# jointCommand('', 5, 'Torque_Limit', 0, 0)

# cycleNumber = 2

# while(cycleNumber>0):
    # Home Position (0 0 -90 0 0) (512 512 204 512 512)
jointCommand('', 1, 'Goal_position', 512, 0.5)
print("mov art 1")
# joint_publisher()
time.sleep(0.5)
jointCommand('', 2, 'Goal_position', 512, 0.5)
print("mov art 2")
# joint_publisher()
time.sleep(0.5)
jointCommand('', 3, 'Goal_position', 204, 0.5)
print("mov art 3")
# joint_publisher()
time.sleep(0.5)
jointCommand('', 4, 'Goal_position', 512, 0.5)
print("mov art 4")
# joint_publisher()
time.sleep(0.5)
jointCommand('', 5, 'Goal_position', 512, 0.5)
print("mov art 5")
# joint_publisher()
time.sleep(2)

# Goal Position [45 30 10 -15 0]
jointCommand('', 1, 'Goal_position', pi/4, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 2, 'Goal_position', pi/6, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 3, 'Goal_position', pi/12, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 4, 'Goal_position', -pi/12, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 5, 'Goal_position', 0, 0.5)
# joint_publisher()
time.sleep(2)

    # cycleNumber = cycleNumber - 1

#joint limits Pincher 3
# 1: 204 - 820 pendiente (-90 = 204 / 90=820 0 en 512)
# 2: 85-970
# 3: 20-950
# 4: 190-835
# 5: 150 - pendiente

def angleMap(ang):
    

    return ang
