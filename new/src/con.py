#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point, Twist
import numpy as np
from math import atan2,tan,sin,cos,sqrt


from nav_msgs.msg import Odometry
from quat2euler import quat2euler


## Define global variables
pose_x = 0
pose_y =0
theta_z = 0

xd = []
yd = []
for i in range(0,50000):
    f = 10*cos(i)
    xd.append(f)
    g = 10*sin(2*i)
    yd.append(g)


## This function will give access to robots current position in `pose` variable
def callback(data):
    global pose_x
    global pose_y
    global theta_z
    x  = data.pose.pose.orientation.x
    y  = data.pose.pose.orientation.y
    z = data.pose.pose.orientation.z
    w = data.pose.pose.orientation.w
    pose_x = data.pose.pose.position.x
    pose_y = data.pose.pose.position.y
    theta_z = quat2euler(x,y,z,w)[2]
    
    #pose = [data.pose.pose.position.x, data.pose.pose.position.y, quat2euler(x,y,z,w)[2]]
    



def Waypoints(t):
    x  = 10*cos(t)
    y  = 10*sin(2*t)
    return [x,y] 

def square(x):
    return x**2
def distance(a1,b1,a2,b2):
    return sqrt(square(a1-a2) + square(b1-b2))

goal = Point()
t = np.arange(0,2*3.1415,0.1)

#def control_loop():
a = 0   

rospy.init_node('turtlebot_trajectory_tracker')
pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=20)
rospy.Subscriber('/odom', Odometry, callback)

rate = rospy.Rate(20)
while not rospy.is_shutdown():
   
    x = pose_x
    y = pose_y
    theta = theta_z 

    #t = rospy.get_time()
    
    #goal.x = Waypoints(t)[0]
    #goal.y = Waypoints(t)[1]
    goal.x = Waypoints(t[a])[0]
    goal.y = Waypoints(t[a])[1]
    #a = a+1

    error_x = goal.x - x
    error_y = goal.y - y
    angle_to_goal = atan2(error_y, error_x)
    error_theta = angle_to_goal - theta
    r = distance(x,y,goal.x,goal.y)
    velocity_msg = Twist()
    
    if(abs(angle_to_goal - theta) > 0.15):
	    
	    	
        #velocity_msg.linear.x = 0.2*(r)
        velocity_msg.angular.z = 0.25*(error_theta)
    else:
	
	velocity_msg.linear.x = 0.8*(r)
    
    if(r<0.2):
	a = a+1   
    pub.publish(velocity_msg)
    print(str(x)+" "+str(y))
#    print(" ")
        #print("Controller message pushed at {}".format(rospy.get_time()))
    rate.sleep()

#if __name__ == '__main__':
    #try:
        #control_loop()
    #except rospy.ROSInterruptException:
        #pass

