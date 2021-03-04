#!/usr/bin/env python3
""" teleop_gamepad_real_bot.py"""
# Author: Jonas Meyering
# This ROS Node converts Joystick inputs from the joy node
# into commands for the real TurtleBot3
# based on the works of
# https://andrewdai.co/xbox-controller-ros.html#rosjoy

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Start joy Node first
# $ rosrun joy joy_node dev:=/dev/input/js0
# ----------------------------------------------------
# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed


def callback(data):
    twist = Twist()
    if data.axes[2] == 1.0:
        twist.linear.x = 0.06 * (-data.axes[5] + 1)
        twist.angular.z = 0.5 * data.axes[0]
    elif data.axes[5] != 1.0:
        twist.linear.x = 0
        twist.angular.z = 0
    else:
        twist.linear.x = -0.03 * (-data.axes[2] + 1)
        twist.angular.z = -0.5 * data.axes[0]

    pub.publish(twist)


def start():
    # Intializes everything

    # publishing to "/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rospy.init_node('Joy2TurtleBot')

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)

    rospy.spin()


if __name__ == '__main__':
    rospy.loginfo(" Sending /Joy-Node commands to TurtleBot3 ")
    rospy.loginfo(" Start joy Node first \
                 - $ rosrun joy joy_node dev:=/dev/input/js0 ")
    start()
