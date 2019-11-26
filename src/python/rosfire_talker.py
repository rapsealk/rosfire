#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

import rosfire


def callback(data):
    rospy.loginfo(data)


def talker():
    rospy.init_node("talker", anonymous=True)
    pub = rosfire.Publisher("chatter", String, queue_size=10)
    sub = rosfire.Subscriber("chatter", String, callback)
    sub2 = rosfire.FirebaseSubscriber("chatter", callback)
    rate = rospy.Rate(10)   # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rospy.loginfo(sub.once())
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException as e:
        rospy.logerr(e)
