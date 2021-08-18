#!/usr/bin/env python

import random
import rospy
import numpy
import time

from phd.srv import NewEpisode
from std_srvs.srv import Empty
from social_msgs.srv import DestinationArray
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState

def euler_to_quaternion(roll, pitch, yaw):
  qx = numpy.sin(roll/2) * numpy.cos(pitch/2) * numpy.cos(yaw/2) - numpy.cos(roll/2) * numpy.sin(pitch/2) * numpy.sin(yaw/2)
  qy = numpy.cos(roll/2) * numpy.sin(pitch/2) * numpy.cos(yaw/2) + numpy.sin(roll/2) * numpy.cos(pitch/2) * numpy.sin(yaw/2)
  qz = numpy.cos(roll/2) * numpy.cos(pitch/2) * numpy.sin(yaw/2) - numpy.sin(roll/2) * numpy.sin(pitch/2) * numpy.cos(yaw/2)
  qw = numpy.cos(roll/2) * numpy.cos(pitch/2) * numpy.cos(yaw/2) + numpy.sin(roll/2) * numpy.sin(pitch/2) * numpy.sin(yaw/2)
  return [qx, qy, qz, qw]

def init_service_client(_topic, _msg_type):
    rospy.loginfo('Starting service client: {}'.format(_topic))
    rospy.wait_for_service(_topic)
    return rospy.ServiceProxy(_topic, _msg_type)

class Experiment():

    def __init__(self):

        self.rate = rospy.Rate(25)

        # params
        self.max_episode = rospy.get_param('~max_experiments', 10)
        self.robot_waypoints = rospy.get_param('~robot_waypoints', '')
        self.robot_model_name = rospy.get_param('~robot_model_name', '')

        # services clients
        self.srv_start = init_service_client("/extract_data/start", NewEpisode)
        self.srv_reset_world = init_service_client("/gazebo/reset_world", Empty)
        self.srv_get_destination = init_service_client("/social_reasoning/get_destination", DestinationArray)
        self.srv_model_reposition = init_service_client("/gazebo/set_model_state", SetModelState)

        data = []
        for i_episode in range(self.max_episode):
            print(' ')
            self.rate.sleep()
            rospy.loginfo("Preparing episode {}/{}".format(i_episode+1,self.max_episode))
            self.reset(self.robot_waypoints)
            rospy.loginfo("Running episode {}/{}".format(i_episode+1,self.max_episode))
            self.srv_start(self.robot_waypoints)
            rospy.loginfo("Finish episode {}/{}".format(i_episode+1,self.max_episode))
            print(' ')

    def reset(self, waypoints):
        start = waypoints.split()[0]

        # Reset world
        self.srv_reset_world()
        self.rate.sleep()


        # reset robot
        deg = random.randint(-180, 180)
        rad = deg/numpy.pi
        [qx, qy, qz, qw] = euler_to_quaternion(0, 0, rad)
        destination = self.srv_get_destination(start).destination_list[0]
        model = ModelState()
        model.model_name = self.robot_model_name
        model.pose = destination.pose
        model.pose.orientation.x = qx
        model.pose.orientation.y = qy
        model.pose.orientation.z = qz
        model.pose.orientation.w = qw
        self.srv_model_reposition(model)


if __name__ == '__main__':
    try:
        rospy.init_node('experiment')
        Experiment()

    except KeyboardInterrupt:
        pass
