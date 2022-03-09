
from myrospy import rospy

string="chatter"

print(rospy.init_node("talker", True))
print(rospy.Publisher("chatter",string))
print(rospy.get_time())
print(rospy.is_shutdown())

str="helloworld"
print(rospy.loginfo(str))
print(rospy.publish(str))
print(rospy.sleep())

data="aa"
print(rospy.loginfo('I heard'))
print(rospy.init_node("chattet",True))
    

def _base_logger(msg, args, kwargs, throttle=None,
                 throttle_identical=False, level=None, once=False):

    rospy_logger = logging.getLogger('rosout')
    name = kwargs.pop('logger_name', None)
    if name:
        rospy_logger = rospy_logger.getChild(name)
    logfunc = getattr(rospy_logger, level)
    
    if once:
        caller_id = _frame_to_caller_id(inspect.currentframe().f_back.f_back)
        if _logging_once(caller_id):
            logfunc(msg, *args, **kwargs)
    elif throttle_identical:
        caller_id = _frame_to_caller_id(inspect.currentframe().f_back.f_back)
        throttle_elapsed = False
        if throttle is not None:
            throttle_elapsed = _logging_throttle(caller_id, throttle)
        if _logging_identical(caller_id, msg) or throttle_elapsed:
            logfunc(msg, *args, **kwargs)
    elif throttle:
        caller_id = _frame_to_caller_id(inspect.currentframe().f_back.f_back)
        if _logging_throttle(caller_id, throttle):
            logfunc(msg, *args, **kwargs)
    else:
        logfunc(msg, *args, **kwargs)
    return msg


def loginfo(msg, *args, **kwargs):
   _base_logger(msg, args, kwargs, level='info')
##print(rospy.Subscriber("chatter", str))
##print(rospy.spin())




















