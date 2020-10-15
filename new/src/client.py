#!/usr/bin/env python


import rospy
##from hector_uav_msgs.msg import PoseActionGoal
##from geometry_msgs import PoseStamped

from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point,Twist
from geometry_msgs.msg import PoseStamped
from math import atan2

x = 0.0
y = 0.0
z = 0.0
theta = 0.0

def newOdom (msg) :
    global x
    global y
    global z
    global theta
    
    x = msg.pose.position.x   ##pose.position.x
    y = msg.pose.position.y    ##pose.position.y
    z = msg.pose.position.z
    rot_q =msg.pose.orientation
    (roll ,pitch ,theta)=euler_from_quaternion([rot_q.x ,rot_q.y,rot_q.z ,rot_q.w])

rospy.init_node("speed_controller")
sub = rospy.Subscriber("/ground_truth_to_tf/pose",PoseStamped ,newOdom)
pub = rospy.Publisher("/cmd_vel/",Twist,queue_size=1)   
  
speed =Twist()
r= rospy.Rate(1000) 
goal = Point()
goal.x =9
goal.y =2
goal.z =7

while not rospy.is_shutdown():

    inc_x=goal.x - x
    inc_y=goal.y - y
    inc_z=goal.z - z
    print(x,y,z)
    print(goal.x,goal.y,goal.z)
    print(inc_x,inc_y,inc_z)
    angle_to_goal = atan2(inc_y,inc_x)
    if inc_z > 0.1 :

        speed.linear.z = 0.5
    else :
 
       
        if abs(angle_to_goal - theta )>0.1 :
            
            speed.linear.x = 0.0
            speed.angular.z = 0.3
            print(speed.linear.z)

        else :
            
            speed.linear.x = 0.5
            speed.angular.z = 0.0
            print(speed.linear.z)

    pub.publish(speed)       
    r.sleep()      

'''
while not rospy.is_shutdown():

    
    inc_z=goal.z - z
    print(x,y,z)
    print(goal.x,goal.y,goal.z)
    print(inc_z)
    print(speed.linear.z )
    ##angle_to_goal = atan2(inc_y,inc_x)
    if inc_z > 0.1 :

        speed.linear.z = 0.5
        pub.publish(speed)       
        r.sleep() 
    else :
        speed.linear.z = 0.0
        pub.publish(speed)       
        r.sleep()
        


def path_plan(px ,py) :
    r = rospy.Rate(10)
    goal.x = px
    goal.y = py
    print(goal.x)   
    print(goal.y)
    print(goal.z)   
    while not rospy.is_shutdown():
        
        print("s1")
        print(x,y,z) 
        inc_x=goal.x - x
        inc_y=goal.y - y
        ##inc_z=goal.z - z
        print("s2")
        angle_to_goal = atan2(inc_y,inc_x)
        
        
            
        if abs(angle_to_goal - theta )>0.1 :
                
            speed.linear.x = 0.0
            speed.angular.z = 0.3
            print("angular")
        else :
                
            speed.linear.x = 0.5
            speed.angular.z = 0.0
            print("linearx")
        print("about to pub")        
        pub.publish(speed)   
        print("published")    
        r.sleep() 
        print("slept")
        return "ok" 
    return "ok2"

a=5
##a=int (input("enter a num :"))

k=a+1
k=k/2
 ##print (k)
r,c=0,0


for l in range (k) :
    ##l means iterations ,int of (a+1)/2 times.... a = side of the square 
    if  r < a and c < a :
                    ##to keep constarints for r,c...
   
        for i in range (a-1) : 

   
            print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))                            
            path_plan(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
            time.sleep(0.1)
            r=r+1
   
    if  r < a and c < a :

        print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
        path_plan(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
        time.sleep(0.1)
        c=c+1
  

    if  r < a and c < a :
        
        for i in range (a-1):
            
            print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
            path_plan(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
            time.sleep(0.1)
            r=r-1
    
    
    if  r < a and c < a :
         
        print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
        path_plan(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
        time.sleep(0.1)
        c=c+1
  

 '''