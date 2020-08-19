#!/usr/bin/env python
#import sys

from pylab import *
import numpy as np
from matplotlib import pyplot as plt
import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image

import tensorflow as tf

model=tf.keras.models.load_model('my_model.h5')
##model=tf.lite.TFLiteConverter.from_keras_model('my_model.h5')

##from google.colab import drive
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from tensorflow.python.keras.callbacks import TensorBoard
from time import time
##from tensorboardcolab import TensorBoardColab, TensorBoardColabCallback

b=112
h=112

def detect(data):

    bridge = CvBridge()
    image = bridge.imgmsg_to_cv2(data, "bgr8")
    img=cv2.imread(image,1)

    ##img=cv2.imread('/content/drive/My Drive/ITSP/SOIL/image24.jpg',1)
##img=cv2.resize(b,h)
    img= cv2.resize(img,(b,h))
    img = img.astype(np.uint8)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    image=np.zeros([1,b,h,3])
    image[0]=img
    predictions=model.predict(image)
    print(predictions)
    if predictions >0.5 :
        print("SOIL")
    else :
        print("NO SOIL")    
##model.predict(img)
##prediction=model.predict([[img]])
    

    

    cv2.imshow("Image",image)
    k = cv2.waitKey(5) & 0xFF

if __name__ == '__main__':
	rospy.init_node('image_gazebo', anonymous=True)
	rospy.Subscriber("/front_cam/camera/image", Image, detect)
	rospy.spin()




