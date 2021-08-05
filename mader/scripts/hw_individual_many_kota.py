#!/usr/bin/env python
# coding=utf-8

# /* ----------------------------------------------------------------------------
#  * Copyright 2020, Jesus Tordesillas Torres, Aerospace Controls Laboratory
#  * Massachusetts Institute of Technology
#  * All Rights Reserved
#  * Authors: Jesus Tordesillas, et al.
#  * See LICENSE file for the license information
#  * -------------------------------------------------------------------------- */

#   There's places you need to change depending on each agent
#   Each places are pointed out by #num#, so follow them from 1 to 

# Kota edited for hw experiments August 5, 2021 

import math
import os
import sys
import time
from random import *
# import numpy as np
# from pyquaternion import Quaternion
from tf.transformations import quaternion_from_euler, euler_from_quaternion

def sendCommand(action,quad):
    if(action=="start"):
        #Kota comment: this line launches mader_specific.launch
        os.system("roslaunch mader hw_mader_specific.launch gazebo:=false quad:=" + quad);
    if(action=="mader"):
        #Kota comment: this line launches mader.launch with the argument of quad number
        os.system("roslaunch mader hw_mader.launch quad:="+quad) 
        
if __name__ == '__main__':

    # set quad number

    # agent
#    quad="SQ01s";

    quad = sys.argv[1];   
    sendCommand(sys.argv[2],quad);

    time.sleep(1);