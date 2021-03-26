#!/usr/bin/env python

import rospy

from std_msgs.msg import Header
from pedsim_msgs.msg import AgentStates
from social_msgs.msg import People, Person

def init_publisher(_topic, _msg_type, _queue_size=10):
    rospy.loginfo('Starting publisher: {}'.format(_topic))
    return rospy.Publisher(_topic, _msg_type, queue_size=_queue_size)
def init_subscriber(_topic, _msg_type, _callback):
    rospy.loginfo('Starting subscriber: {}'.format(_topic))
    return rospy.Subscriber(_topic, _msg_type, _callback)

class pedsim_to_social():
    def __init__(self):
        init_subscriber('/pedsim_simulator/simulated_agents', AgentStates, self.callback_people)
        self.pub_locals = init_publisher('people_data', People)
        rospy.spin()

    def callback_people(self, msg):
        people = People()
        people.header = Header(0,rospy.Time.now(),"/map")
        for person in msg.agent_states:
            p = Person()
            p.name = 'person_{}'.format(person.id)
            p.pose = person.pose
            p.pose.position.z += 1
            people.people.append(p)
        self.pub_locals.publish(people)


if __name__ == '__main__':
    try:
        rospy.init_node('pedsim_to_social')
        pedsim_to_social()


    except KeyboardInterrupt:
        pass
