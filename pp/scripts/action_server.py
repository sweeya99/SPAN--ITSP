#! /usr/bin/env python

import rospy
import actionlib
from pp.msg import DoDishesAction,DoDishesResult

class DoDishesServer :

  def__init__(self):
    self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, self.execute, False)
    self.server.start()

  def execute(self, goal):
    
    success = True
    s=0 
    result = DoDishesResult()
