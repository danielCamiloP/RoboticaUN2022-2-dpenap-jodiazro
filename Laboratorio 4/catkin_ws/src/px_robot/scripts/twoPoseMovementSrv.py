"""
Allows to use the service dynamixel_command 
"""
from cmath import pi

# import joint_Pub
from jointSrv import jointCommand
from pubMovement import joint_publisher
import rospy
import time
from math import ceil
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand

def angleMap(ang):
    angMap = ceil(3.422*ang + 512)
    
    return angMap

# print(angleMap(90))

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

# Goal Position [720 205 345 690 512]
jointCommand('', 1, 'Goal_position', 720, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 2, 'Goal_position', 205, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 3, 'Goal_position', 345, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 4, 'Goal_position', 690, 0.5)
# joint_publisher()
time.sleep(0.5)
jointCommand('', 5, 'Goal_position', 512, 0.5)
# joint_publisher()
time.sleep(2)   

    # cycleNumber = cycleNumber - 1

#joint limits Pincher 3
# 1: 204 - 820 pendiente (-90 = 204 / 90=820 0 en 512)
# 2: 85-970
# 3: 20-950
# 4: 190-835
# 5: 150 - pendiente

'''
Serv:
1: 720
2: 205
3: 345
4: 690
5: 512
'''