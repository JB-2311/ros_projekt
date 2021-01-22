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

>$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/ros_projekt/maps/arena_robotiklabor.yaml

### Labyrinth

currently not working

>$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/ros_projekt/maps/rtc_Arena01.yaml

### change parameters

>$ rosrun rqt_reconfigure rqt_reconfigure

Costmap parameters are found in move_base/global_costmap and move_base/local_costmap in inflation_layer

## map a new gazebo world

start rviz mapping

>$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

control turtlebot via teleop

>$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

save map as new_map

>$ rosrun map_server map_saver -f \$HOME/catkin_ws/src/ros_projekt/maps/new_map




