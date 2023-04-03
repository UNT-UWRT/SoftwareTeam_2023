#!/bin/bash
gnome-terminal -- roscore
sleep 3
gnome-terminal -- sudo modprobe xpad &&
rosparam set joy_node/dev "/dev/input/js2" &&
rosrun joy joy_node &
sleep 5
gnome-terminal -- sudo jstest /dev/input/js2
