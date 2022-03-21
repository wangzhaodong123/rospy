import logging

def configlogging(level_=logging.DEBUG):
  logging.basicConfig(filemode='w',datafmt='%(asctime)s', format = '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s',level=level_)

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
        # call logging
        logfunc(msg, *args, **kwargs)
    return msg

# info interface
def logdebug(msg, *args, **kwargs):
    _base_logger(msg, args, kwargs, level='debug')

def loginfo(msg, *args, **kwargs):
    _base_logger(msg, args, kwargs, level='info')

def logwarn(msg, *args, **kwargs):
    _base_logger(msg, args, kwargs, level='warn')

def logerr(msg, *args, **kwargs):
    _base_logger(msg, args, kwargs, level='error')

def logfatal(msg, *args, **kwargs):
    _base_logger(msg, args, kwargs, level='critical')