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
a=int (input("enter a no of sides:"))

k=a+1
k=k/2
print (k)
r,c=0,0


for l in range (k) :##l means iterations ,int of (a+1)/2 times.... a = side of the square 
 if  r < a and c < a : ##to keep constarints for r,c...
   
  for i in range (a-1) : 
   
   xd.append(((2*c)+1)/(2.0))
   yd.append(((2*r)+1)/(2.0))
   r=r+1
   

 if  r < a and c < a :

   xd.append(((2*c)+1)/(2.0))
   yd.append(((2*r)+1)/(2.0))
   c=c+1
  

 if  r < a and c < a : 

  for i in range (a-1):
    
   xd.append(((2*c)+1)/(2.0))
   yd.append(((2*r)+1)/(2.0))
   r=r-1
    
    
 if  r < a and c < a :
   xd.append(((2*c)+1)/(2.0))
   yd.append(((2*r)+1)/(2.0))
   c=c+1
  
 
  
 


## This function will give access to robots current position in `pose` variable
def callback(data):
    global pose_x
    global pose_y
    global theta_z
    x  = data.pose.pose.orientation.x;
    y  = data.pose.pose.orientation.y;
    z = data.pose.pose.orientation.z;
    w = data.pose.pose.orientation.w;
    pose_x = data.pose.pose.position.x
    pose_y = data.pose.pose.position.y
    theta_z = quat2euler(x,y,z,w)[2]
    
    #pose = [data.pose.pose.position.x, data.pose.pose.position.y, quat2euler(x,y,z,w)[2]]

def square(x):
    return x**2
def distance(a1,b1,a2,b2):
    return sqrt(square(a1-a2) + square(b1-b2))

goal = Point()


#def control_loop():
s = 0   

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
    goal.x = xd[s]
    goal.y = yd[s]
    #s = s+1

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
	s = s+1   
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


