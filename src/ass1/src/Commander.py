#!/usr/bin/env python


import rospy
import time
import math
import random
from std_msgs.msg import String
from geometry_msgs.msg import Point

 
## UserAction Function
def UserAction():
		## Loop 
    while True: 
	    comm = String() 
			## This selcts Randomly between the play or sleep state
	    comm = random.choice(['play','sleep'])
	    ## Publish Command 
	    speech = rospy.Publisher("command",String,queue_size=10) 
	    speech.publish(comm) 
	    
	    ## Generation of target positions if command is play 
	    if comm == 'play': 
			PersonPosition = Point() 
			PersonPosition.x = random.randrange(1,11,1) 
			PersonPosition.y = random.randrange(1,11,1) 
			PersonPosition.z = 0 
			## Publish Person Position 
			pos = rospy.Publisher("PersonPosition", Point, queue_size = 10)
			pos.publish(PersonPosition) 
			PointingGesture = Point() 
			PointingGesture.x = random.randrange(1,11,1) 
			PointingGesture.y = random.randrange(1,11,1) 
			PointingGesture.z = 0 
			## Publish a Pointed Position 
			point=rospy.Publisher("PointingGesture",Point, queue_size = 10) 
			point.publish(PointingGesture)

		
	    time.sleep(5) 
## Main Function
if __name__ == '__main__':
		##Init the ros node 
    rospy.init_node('Commander')
    UserAction()
