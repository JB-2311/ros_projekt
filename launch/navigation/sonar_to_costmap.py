#!/usr/bin/env python3
# sonar_to_costmap.py
# ################################################################################
# edited Jonas Meyering 23.01.2021
#
# brings Sonar detected Obstacles into move_base local costmap
# using point_cloud - message
#
# usage
#   $1 roslaunch ros_projekt turtlebot3_arena_robotiklabor.launch
#   $2 roslaunch ros_projekt turtlebot3_navigation.launch
#   $3 rosrun rtc sonar_to_costmap.py
# ------------------------------------------------------------------

import rospy
import std_msgs.msg
from geometry_msgs.msg import Point32
# from sensor_msgs.msg import Range
from sensor_msgs.msg import PointCloud
from turtlebot3_msgs.msg import SensorState


class Sonar_to_Point_Cloud():
    def __init__(self):
        rospy.loginfo("Publishing PointCloud")

        self.cloud_pub = rospy.Publisher('sonar/point_cloud',
                                         PointCloud,
                                         queue_size=10)

        # receiving sonar_left and sonar_right
        self.sonar_sub_left = rospy.Subscriber('sensor_state',
                                               SensorState,
                                               self.get_sonar,
                                               queue_size=10)
        self.dist_left = 0.0
        self.dist_right = 0.0
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.rate.sleep()

    def get_sonar(self, sensor_data):
        # rospy.loginfo(" Sonar Data received ")
        self.reset_values
        self.dist_left = sensor_data.cliff/100.0
        rospy.loginfo(" Sonar Data Left %f", self.dist_left)
        self.dist_right = sensor_data.sonar/100.0
        rospy.loginfo(" Sonar Data Right %f", self.dist_right)
        self.cloud_build()

    def reset_values(self):
        self.dist_left = 0.0
        self.dist_right = 0.0
        self.dist = 0.0

    def cloud_build(self):
        # add sonar readings (robot-local coordinate frame) to cloud
        pl = Point32()
        pr = Point32()
        # Instanziiere leere PointCloud
        cloud = PointCloud()
        # filling pointcloud header
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        header.frame_id = 'base_link'
        cloud.header = header
        boolpl = False
        boolpr = False

        # Linke Seite
        if(self.dist_left < 0.95 and self.dist_left > 0.05):
            pl.x = self.dist_left + 0.05
            pl.y = 0.075
            pl.z = 0.0
            cloud.points.append(pl)
            boolpl = True

        # Rechte Seite
        if(self.dist_right < 0.95 and self.dist_right > 0.05):
            pr.x = self.dist_right + 0.05
            pr.y = -0.075
            pr.z = 0.0
            cloud.points.append(pr)
            boolpr = True

        if boolpl is True and boolpr is True:
            pm = Point32()
            pm.x = (pl.x + pr.x) / 2
            pm.y = 0.0
            pm.z = 0.0
            cloud.points.append(pm)

        # Senden
        self.cloud_pub.publish(cloud)


if __name__ == '__main__':
    rospy.init_node('sonar_controller', anonymous=True)
    try:
        sonar = Sonar_to_Point_Cloud()
    except rospy.ROSInterruptException:
        pass
