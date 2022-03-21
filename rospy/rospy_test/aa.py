import rospy

if __name__ == '__main__':
    # initialize node
    rospy.init_node("chattet", anonymous=True)

    # logging test

    rospy.logdebug('I heard message!')
    rospy.loginfo('I heard message!')
    rospy.logwarn('I heard message!')
    rospy.logerr('I heard message!')
    rospy.logfatal('I heard message!')

rospy.is_shutdown()
rospy.spin()

rospy.Subscriber("a1",'a2','a3')
rospy.unregister("a2")

rospy.Publisher('b1')
# publish data interface
rospy.Publish('a4')

rospy.Rate("a5",'a6')
rospy.sleep()
rospy.get_time()


