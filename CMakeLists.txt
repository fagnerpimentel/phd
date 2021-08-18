cmake_minimum_required(VERSION 3.0.2)
project(phd)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  social_msgs
  message_generation
)

add_service_files(
  FILES
	NewEpisode.srv
)

generate_messages(
   DEPENDENCIES
   geometry_msgs
   std_msgs
   social_msgs
)

catkin_package(
)
