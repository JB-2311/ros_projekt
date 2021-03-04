# ros_projekt
## Installation

clone repository to catkin_ws/src

 >$ cd $HOME/catkin_ws/src

 >$ git clone https://github.com/JB-2311/ros_projekt.git

enter models folder and copy model to .gazebo/models

>$ cd ros_projekt/models

>$ cp -r arena_robotiklabor $HOME/.gazebo/models/arena_robotiklabor

perform a catkin_make

>$ cd $HOME/catkin_ws

>$ catkin_make

## open gazebo
### Robotiklabor

>$ roslaunch ros_projekt turtlebot3_arena_robotiklabor.launch

### Labyrinth

>$ roslaunch ros_projekt turtlebot3_arena_labyrinth.launch

## open RViz to navigate
### Robotiklabor

>$ roslaunch ros_projekt turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/ros_projekt/maps/arena_robotiklabor_02.yaml

### Labyrinth

currently not working

>$ roslaunch ros_projekt turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/ros_projekt/maps/rtc_Arena01.yaml

### change parameters

>$ rosrun rqt_reconfigure rqt_reconfigure

Costmap parameters are found in move_base/global_costmap and move_base/local_costmap in inflation_layer

## map a new gazebo world

start slam mapping

>$ roslaunch ros_projekt turtlebot3_slam.launch

control turtlebot via teleop

>$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

save map as new_map

>$ rosrun map_server map_saver -f \$HOME/catkin_ws/src/ros_projekt/maps/new_map

## setup real TurtleBot3

edit .bashrc file on local machine with local ip address (192.168.1.46)

>$ nano .bashrc

>$ export ROS_MASTER_URI=http://192.168.1.46:11311
>$ export ROS_HOSTNAME=192.168.1.46

do according changes on the TurtleBot

start roscore on local machine

>$ roscore

launch ros on TurtleBot

>$ roslaunch turtlebot3_bringup turtlebot3_robot.launch