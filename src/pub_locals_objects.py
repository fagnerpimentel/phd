#!/usr/bin/env python

import rospy
import yaml

from std_msgs.msg import Header
from social_msgs.msg import Locals, Local
from social_msgs.msg import Objects, Object

def init_publisher(_topic, _msg_type, _queue_size=10):
    rospy.loginfo('Starting publisher: {}'.format(_topic))
    return rospy.Publisher(_topic, _msg_type, queue_size=_queue_size)

class pub_locals_objects():
    def __init__(self):
        rate = rospy.Rate(25)
        pub_locals = init_publisher('locals_data', Locals)
        pub_objects = init_publisher('objects_data', Objects)

        path = rospy.get_param('~locals_objects_path')
        yaml_file = open(path,'r')
        yaml_data = yaml.load(yaml_file)
        locals_data = yaml_data['locals']
        objects_data = yaml_data['objects']

        while not rospy.is_shutdown():
            rate.sleep()

            locals = Locals()
            locals.header = Header(0,rospy.Time.now(),"/map")
            for local_name in locals_data:
                l = Local()
                l.name = local_name
                l.pose.position.x = locals_data[local_name]['position']['x']
                l.pose.position.y = locals_data[local_name]['position']['y']
                l.pose.position.z = locals_data[local_name]['position']['z']
                l.pose.orientation.x = locals_data[local_name]['orientation']['x']
                l.pose.orientation.y = locals_data[local_name]['orientation']['y']
                l.pose.orientation.z = locals_data[local_name]['orientation']['z']
                l.pose.orientation.w = locals_data[local_name]['orientation']['w']
                locals.locals.append(l)
            pub_locals.publish(locals)

            objects = Objects()
            objects.header = Header(0,rospy.Time.now(),"/map")
            for object_name in objects_data:
                o = Object()
                o.name = object_name
                o.pose.position.x = objects_data[object_name]['position']['x']
                o.pose.position.y = objects_data[object_name]['position']['y']
                o.pose.position.z = objects_data[object_name]['position']['z']
                o.pose.orientation.x = objects_data[object_name]['orientation']['x']
                o.pose.orientation.y = objects_data[object_name]['orientation']['y']
                o.pose.orientation.z = objects_data[object_name]['orientation']['z']
                o.pose.orientation.w = objects_data[object_name]['orientation']['w']
                objects.objects.append(o)
            pub_objects.publish(objects)

if __name__ == '__main__':
    try:
        rospy.init_node('pub_locals_objects')
        pub_locals_objects()

    except KeyboardInterrupt:
        pass
