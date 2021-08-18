#!/usr/bin/env python

import rospy
import enum
import random
import numpy
import actionlib

from phd.srv import NewEpisode, NewEpisodeResponse
from social_msgs.srv import DestinationArray
from std_srvs.srv import Empty, EmptyResponse
from nav_msgs.srv import GetPlan

from social_msgs.msg import Locals, Local
from social_msgs.msg import People, Person
from std_msgs.msg import String
from std_msgs.msg import Float32
from social_worlds.msg import Region
from nav_msgs.msg import Path
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from social_move_base.msg import SocialMoveBaseAction
from social_move_base.msg import SocialMoveBaseGoal

from geometry_msgs.msg import Point

class State(enum.Enum):
    NONE = 0
    RUNNING = 1
    SUCCESS = 2
    SPACE_EXCEEDED = 3
    TIME_EXCEEDED = 4
    ABORTION = 5
    COLLISION = 6
    INVASION = 7

class Info():
    def __init__(self):
        # pre episode info
        self.checkpoints = []
        self.path_plan = []
        self.space_min = 0
        self.time_min = 0
        # pos episode info
        self.state = State.NONE
        self.path_executed = []
        self.delta_space = []
        self.delta_time = []
        self.total_space = 0
        self.total_time = 0
        # misc info
        self.factor_array = []
        self.people_array = []
        self.localization_error_array = []

def euler_to_quaternion(roll, pitch, yaw):
  qx = numpy.sin(roll/2) * numpy.cos(pitch/2) * numpy.cos(yaw/2) - numpy.cos(roll/2) * numpy.sin(pitch/2) * numpy.sin(yaw/2)
  qy = numpy.cos(roll/2) * numpy.sin(pitch/2) * numpy.cos(yaw/2) + numpy.sin(roll/2) * numpy.cos(pitch/2) * numpy.sin(yaw/2)
  qz = numpy.cos(roll/2) * numpy.cos(pitch/2) * numpy.sin(yaw/2) - numpy.sin(roll/2) * numpy.sin(pitch/2) * numpy.cos(yaw/2)
  qw = numpy.cos(roll/2) * numpy.cos(pitch/2) * numpy.cos(yaw/2) + numpy.sin(roll/2) * numpy.sin(pitch/2) * numpy.sin(yaw/2)
  return [qx, qy, qz, qw]

def quaternion_to_euler(x, y, z, w):
  t0 = +2.0 * (w * x + y * z)
  t1 = +1.0 - 2.0 * (x * x + y * y)
  roll = numpy.arctan2(t0, t1)
  t2 = +2.0 * (w * y - z * x)
  t2 = +1.0 if t2 > +1.0 else t2
  t2 = -1.0 if t2 < -1.0 else t2
  pitch = numpy.arcsin(t2)
  t3 = +2.0 * (w * z + x * y)
  t4 = +1.0 - 2.0 * (y * y + z * z)
  yaw = numpy.arctan2(t3, t4)
  return [yaw, pitch, roll]

def init_files(path_storage):

    file_people = open(path_storage+"people.json","w+")
    file_people.write('{')
    file_path_min_x = open(path_storage+"path_plan_x.json","w+")
    file_path_min_x.write('{')
    file_path_min_y = open(path_storage+"path_plan_y.json","w+")
    file_path_min_y.write('{')
    file_path_elapsed_x = open(path_storage+"path_executed_x.json","w+")
    file_path_elapsed_x.write('{')
    file_path_elapsed_y = open(path_storage+"path_executed_y.json","w+")
    file_path_elapsed_y.write('{')
    file_result = open(path_storage+"result.csv","w+")
    file_result.write("i,start_x,start_y,start_ang,goal_x,goal_y,goal_ang," +
                    "space_min,time_min,space_elapsed,time_elapsed,state\n")

    file_people.close()
    file_path_min_x.close()
    file_path_min_y.close()
    file_path_elapsed_x.close()
    file_path_elapsed_y.close()
    file_result.close()

def finish_files(path_storage):

    file_people = open(path_storage+"people.json","a+")
    file_people.write('\n}')
    file_path_min_x = open(path_storage+"path_plan_x.json","a+")
    file_path_min_x.write('\n}')
    file_path_min_y = open(path_storage+"path_plan_y.json","a+")
    file_path_min_y.write('\n}')
    file_path_elapsed_x = open(path_storage+"path_executed_x.json","a+")
    file_path_elapsed_x.write('\n}')
    file_path_elapsed_y = open(path_storage+"path_executed_y.json","a+")
    file_path_elapsed_y.write('\n}')

    file_people.close()
    file_path_min_x.close()
    file_path_min_y.close()
    file_path_elapsed_x.close()
    file_path_elapsed_y.close()

def update_files(path_storage, info, episode):
    i = episode

    #
    file_people = open(path_storage+"people.json","a+")
    list_2 = []
    for e2 in info.people_array:
        list_3 = []
        for e3 in e2:
            list_3.append('['+str(e3.pose.position.x)+','+str(e3.pose.position.y)+']')
        list_2.append('[' + ','.join([str(x) for x in list_3]) + ']')
    line = '\n"'+str(i)+'":[' + ','.join([str(x) for x in list_2]) + ']'
    if(len(file_people.readlines()) > 1):
        file_people.write(',')
    file_people.write(line)
    file_people.close()

    #
    file_path_min_x = open(path_storage+"path_plan_x.json","a+")
    file_path_min_y = open(path_storage+"path_plan_y.json","a+")
    list_x = []
    list_y = []
    for e2 in info.path_plan:
        list_x.append(e2.pose.position.x)
        list_y.append(e2.pose.position.y)
    line_ex = '\n"'+str(i)+'":[' + ','.join([str(x) for x in list_x]) + ']'
    line_ey = '\n"'+str(i)+'":[' + ','.join([str(y) for y in list_y]) + ']'
    if(len(file_path_min_x.readlines()) > 1):
        file_path_min_x.write(',')
    if(len(file_path_min_y.readlines()) > 1):
        file_path_min_y.write(',')
    file_path_min_x.write(line_ex)
    file_path_min_y.write(line_ey)
    file_path_min_x.close()
    file_path_min_y.close()

    #
    file_path_elapsed_x = open(path_storage+"path_executed_x.json","a+")
    file_path_elapsed_y = open(path_storage+"path_executed_y.json","a+")
    list_x = []
    list_y = []
    for e2 in info.path_executed:
        list_x.append(e2.x)
        list_y.append(e2.y)
    line_ex = '\n"'+str(i)+'":[' + ','.join([str(x) for x in list_x]) + ']'
    line_ey = '\n"'+str(i)+'":[' + ','.join([str(y) for y in list_y]) + ']'
    if(len(file_path_elapsed_x.readlines()) > 1):
        file_path_elapsed_x.write(',')
    if(len(file_path_elapsed_y.readlines()) > 1):
        file_path_elapsed_y.write(',')
    file_path_elapsed_x.write(line_ex)
    file_path_elapsed_y.write(line_ey)
    file_path_elapsed_x.close()
    file_path_elapsed_y.close()

    #
    file_result = open(path_storage+"result.csv","a+")
    (start_yaw, _, _) = quaternion_to_euler(
        info.checkpoints[0].pose.orientation.x, info.checkpoints[0].pose.orientation.y,
        info.checkpoints[0].pose.orientation.z, info.checkpoints[0].pose.orientation.w)
    (goal_yaw, _, _) = quaternion_to_euler(
        info.checkpoints[-1].pose.orientation.x, info.checkpoints[-1].pose.orientation.y,
        info.checkpoints[-1].pose.orientation.z, info.checkpoints[-1].pose.orientation.w)
    file_result.write( str(i) + ",")
    file_result.write( str(info.checkpoints[0].pose.position.x) + ",")
    file_result.write( str(info.checkpoints[0].pose.position.y) + ",")
    file_result.write( str(start_yaw) + ",")
    file_result.write( str(info.checkpoints[-1].pose.position.x) + ",")
    file_result.write( str(info.checkpoints[-1].pose.position.y) + ",")
    file_result.write( str(goal_yaw) + ",")
    file_result.write( str(info.space_min) + ",")
    file_result.write( str(info.time_min) + ",")
    file_result.write( str(info.total_space) + ",")
    file_result.write( str(info.total_time) + ",")
    file_result.write( str(info.state.name) + "\n")
    file_result.close()











# def init_publisher(_topic, _msg_type, _queue_size=10):
#     rospy.loginfo('Starting publisher: {}'.format(_topic))
#     return rospy.Publisher(_topic, _msg_type, queue_size=_queue_size)
def init_subscriber(_topic, _msg_type, _callback):
    rospy.loginfo('Starting subscriber: {}'.format(_topic))
    return rospy.Subscriber(_topic, _msg_type, _callback)
def init_service_server(_topic, _msg_type, _callback):
    rospy.loginfo('Starting service server: {}'.format(_topic))
    return rospy.Service(_topic, _msg_type, _callback)
def init_service_client(_topic, _msg_type):
    rospy.loginfo('Starting service client: {}'.format(_topic))
    rospy.wait_for_service(_topic)
    return rospy.ServiceProxy(_topic, _msg_type)
# def init_action_server(_topic, _msg_type, _callback):
#     rospy.loginfo('Starting action server: {}'.format(_topic))
#     action = actionlib.SimpleActionServer(_topic, _msg_type, _callback)
#     action.start()
#     return action
def init_action_client(_topic, _msg_type):
    rospy.loginfo('Starting action client: {}'.format(_topic))
    action = actionlib.SimpleActionClient(_topic, _msg_type)
    action.wait_for_server()
    return action


class ExtractData():

    def __init__(self):

        self.rate = rospy.Rate(10)
        self.checkpoint_actual_index = 0
        self.episode = 0

        # params
        self.path_storage = rospy.get_param('~path_storage', '')
        self.global_planner = rospy.get_param('~global_planner', '')
        self.robot_max_vel = rospy.get_param('~robot_max_vel', 0.3)
        self.space_factor_tolerance = rospy.get_param('~space_factor_tolerance', 5)
        self.time_factor_tolerance = rospy.get_param('~time_factor_tolerance', 5)

        # subscribers
        self.sub_robot1 = init_subscriber('/odom', Odometry, self.__robot_odom_callback__)
        self.sub_robot2 = init_subscriber('/amcl_pose', PoseWithCovarianceStamped, self.__robot_amcl_callback__)
        self.sub_colision = init_subscriber('/collision', String, self.__collision_callback__)
        self.sub_forbidden = init_subscriber('/check_forbidden_region', Region, self.__forbidden_callback__)
        self.sub_people = init_subscriber('/people', People, self.__people_callback__)
        self.sub_locals = init_subscriber('/locals', Locals, self.__locals_callback__)
        self.sub_factor = init_subscriber('/real_time_factor', Float32, self.__factor_callback__)
        rospy.loginfo("Subscribers ready.")

        # action clients
        self.social_move_base = init_action_client("/social_navigation", SocialMoveBaseAction)
        rospy.loginfo("Action clients ready.")

        # service clients
        self.srv_get_destination = init_service_client("/social_reasoning/get_destination", DestinationArray)
        self.scl_clear_costmaps = init_service_client("/move_base/clear_costmaps", Empty)
        self.scl_make_plan = init_service_client("/move_base/{}/make_plan".format(self.global_planner.split("/", 1)[1]),GetPlan)
        # self.scl_cancel_navigation = init_service_client("/social_navigation/cancel", Empty)
        rospy.loginfo("Service clients ready.")

        # service servers
        self.sse_start = init_service_server('~start',NewEpisode, self.__callback_sse_start__)
        rospy.loginfo('Services server ready.')

        init_files(self.path_storage)
        rospy.spin()
        finish_files(self.path_storage)

    def __robot_odom_callback__(self, msg):
        self.robot_pose = msg.pose.pose
        pass
    def __robot_amcl_callback__(self, msg):
        # self.robot_pose = msg.pose.pose
        pass

    def __collision_callback__(self, msg):
        self.info.state = State.COLLISION
        # self.scl_cancel_navigation()
        self.done = True
    def __forbidden_callback__(self, msg):
        self.info.state = State.INVASION
        # self.scl_cancel_navigation()
        self.done = True
    def __people_callback__(self, msg):
        self.people = msg.people
    def __locals_callback__(self, msg):
        self.locals = msg.locals
    def __factor_callback__(self, msg):
        self.factor = msg.data

    def __social_movebase_command__(self, goal):
        target_name = goal
        smb_goal = SocialMoveBaseGoal()
        smb_goal.target_name = goal
        self.social_move_base.send_goal(smb_goal,
            done_cb=self.__movebase_callback_done__,
            active_cb=self.__movebase_callback_active__,
            feedback_cb=self.__movebase_callback_feedback__)
        # self.move_base.wait_for_result()
        self.rate.sleep()

    def __movebase_callback_active__(self):
        rospy.loginfo("Action server is processing the goal")

    def __movebase_callback_feedback__(self, feedback):
        # rospy.loginfo("Feedback:%s" % str(feedback))
        pass

    def __movebase_callback_done__(self, state, result):
        rospy.loginfo("Action server is done. State: %s, result: %s" % (str(state), str(result)))
        # if (state == actionlib::SimpleClientGoalState::SUCCEEDED){
        if (state == 3):
            rospy.loginfo('Reached checkpoint ' + str(self.checkpoint_actual_index))
            self.checkpoint_actual_index += 1
            if(self.checkpoint_actual_index == len(self.info.checkpoints)):
                self.info.state = State.SUCCESS
                self.done = True
            else:
                self.__social_movebase_command__(self.info.checkpoints[self.checkpoint_actual_index].name)
        else:
            self.info.state = State.ABORTION
            self.done = True


    def __callback_sse_start__(self, req):
        er = NewEpisodeResponse()

        # get new checkpoints
        self.checkpoint_actual_index = 1
        rp = req.checkpoints.split()
        checkpoints = []
        for cp_name in rp:
            if(cp_name == "person"):
                cp_name = random.choice(self.people).name
            destination = []
            destination = self.srv_get_destination(cp_name).destination_list[0]
            l = Local()
            l.name = destination.name
            l.pose = destination.pose
            checkpoints.append(l)

        # clear costmaps
        self.scl_clear_costmaps()
        self.rate.sleep()

        # get new path plan
        path_plan = []
        for n, cp in enumerate(checkpoints):
            rospy.loginfo("Checkpoint {}: (x={},y={},ang={})"
                .format(n, round(cp.pose.position.x,2), round(cp.pose.position.y,2), round(cp.pose.orientation.z,2)))
        rospy.loginfo("Finding a path plan...")
        for n in range(1,len(checkpoints)):
            plan = self.__find_new_path__(
                checkpoints[n-1].pose,
                checkpoints[n].pose).poses
            rospy.loginfo("Path plan from checkpoint {} to {}: {}".format(n-1, n, len(plan)))
            path_plan += plan
        rospy.loginfo("Total path plan size: {}".format(len(path_plan)))

        # min dist and time to reach destination
        space_min, time_min = self.__get_min_dist_time__(path_plan)
        rospy.loginfo("Space min: {} meters".format(round(space_min,2)))
        rospy.loginfo("Time min: {} seconds".format(round(time_min,2)))

        # max dist and time to reach destination
        space_max = space_min*self.space_factor_tolerance
        time_max = time_min*self.time_factor_tolerance
        rospy.loginfo('Space max: {} meters'.format(round(space_max,2)))
        rospy.loginfo('Time max: {} seconds'.format(round(time_max,2)))

        # Send navigation command to robot
        self.__social_movebase_command__(checkpoints[self.checkpoint_actual_index].name)

        ####################

        # episode info
        self.info = Info()
        self.info.checkpoints = checkpoints
        self.info.path_plan = path_plan
        self.info.space_min = space_min
        self.info.time_min = time_min
        #
        self.info.state = State.RUNNING
        self.info.path_executed.append(checkpoints[0].pose.position)
        self.info.delta_space.append(0)
        self.info.delta_time.append(rospy.Time.now())
        self.info.total_space = 0
        self.info.total_time = 0
        #
        self.info.factor_array = []
        self.info.people_array = []
        self.info.localization_error_array = []

        ####################

        # reset episode done info
        self.done = False

        while not self.done:
            # Execute one time step within the environment
            self.rate.sleep()

            # update space
            s_0 = self.info.path_executed[-1]
            s_1 = self.robot_pose.position
            delta_space = numpy.sqrt(
                pow((s_1.x - s_0.x), 2)+
                pow((s_1.y - s_0.y), 2))
            self.info.path_executed.append(s_1)
            self.info.delta_space.append(delta_space)
            self.info.total_space += delta_space

            # update time
            t_0 = self.info.delta_time[0]
            t_1 = rospy.Time.now()
            delta_time = (t_1 - t_0)
            self.info.delta_time.append(delta_time)
            self.info.total_time = delta_time.to_sec()

            # update people
            self.info.people_array.append(self.people)

            # check space restriction
            if(self.info.total_space > self.info.space_min*self.space_factor_tolerance):
                self.info.state = State.SPACE_EXCEEDED
                # self.scl_cancel_navigation()
                self.done = True

            # check time restriction
            if(self.info.total_time > self.info.time_min*self.time_factor_tolerance):
                self.info.state = State.TIME_EXCEEDED
                # self.scl_cancel_navigation()
                self.done = True

        rospy.loginfo("Space elapsed: {} meters".format(round(self.info.total_space,2)))
        rospy.loginfo("Time elapsed: {} seconds".format(round(self.info.total_time,2)))
        rospy.loginfo("State: {}".format(self.info.state.name))

        update_files(self.path_storage,self.info, self.episode)
        self.episode += 1
        return er

    def __find_new_path__(self,start,goal):
        path_plan = Path(Header(0,rospy.Time.now(),"map"),[])
        while(len(path_plan.poses) is 0):
            self.scl_clear_costmaps()
            ps_start = PoseStamped(Header(0,rospy.Time.now(),"map"), start)
            ps_goal = PoseStamped(Header(0,rospy.Time.now(),"map"), goal)
            path_plan.poses = self.scl_make_plan(ps_start, ps_goal, 0.1).plan.poses
        return path_plan

    def __get_min_dist_time__(self, poses):

        space_min = 0
        time_min = 0
        p = Point(poses[0].pose.position.x,poses[0].pose.position.y, 0)
        # set minimum space to reach a goal
        space_min += numpy.sqrt(pow((poses[0].pose.position.x - p.x), 2)+
                          pow((poses[0].pose.position.y - p.y), 2))
        for k in range(1,len(poses)):
            space_min += numpy.sqrt(
                pow((poses[k].pose.position.x - poses[k-1].pose.position.x), 2)+
                pow((poses[k].pose.position.y - poses[k-1].pose.position.y), 2))
        # set minimum time to reach a goal
        time_min = space_min/self.robot_max_vel;
        return space_min, time_min

if __name__ == '__main__':
    ed = None
    try:
        rospy.init_node('extract_data')
        ed = ExtractData()

    except KeyboardInterrupt:
        pass
