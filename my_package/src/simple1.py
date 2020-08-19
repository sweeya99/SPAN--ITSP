#!/usr/bin/env python
#import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
from pylab import *
import numpy as np
from matplotlib import pyplot as plt
import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image

print("2")
def detect(data):
    print("4")
    bridge = CvBridge()
    image = bridge.imgmsg_to_cv2(data, "bgr8")
    print("3")
   

    cv2.imshow("Image",image)
    print("aagaya")
    k = cv2.waitKey(5) & 0xFF

if __name__ == '__main__':
    
	rospy.init_node('image_gazebo', anonymous=True)
	rospy.Subscriber("/front_cam/camera/image", Image, detect)
    
	rospy.spin()





