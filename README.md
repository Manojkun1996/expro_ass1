# Assignment 1 - EXPRO
# Behavioral Architecture
Assuming a Robot, simulating a pet, that interacts with a human and moves in a discrete 2D environment. The robot may have three behaviors : normal (in which it moves randomly), sleep (in which it gets the home position, sleeps for a time and returns in normal behavior) and play (in which it goes in person location, waits for a poiting gesture, goes in the pointed location, comes back to the person and waits for the next pointing gestures. After some time it returns to the normal behavior). The human can interact by pointing gestures and speech.
## ROS Architecture
The system is composed by 3 nodes:"Commander" node, "state_machine" node and "Display" node, and a Launch file. The rqt_graph is showed.
![image]
