#!/usr/bin/env python

import rospy
import matplotlib.pyplot as plt
import numpy as np


def plot():
        rospy.init_node("simple_node")
        rate = rospy.Rate(2)
	t=np.linspace(-(np.pi),np.pi,100)
	x= np.cos(t)
	y=2*np.sin(2*t)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	plt.plot(x,y,'r')
	plt.show()
	

if __name__ == "__main__":
    plot()
    while not rospy.is_shutdown():
        pass

