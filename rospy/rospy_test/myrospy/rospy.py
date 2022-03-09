import logging


##definitions
def init_node(name, argv=None, anonymous=False, log_level=None, disable_rostime=False, disable_rosout=False, disable_signals=False, xmlrpc_port=0, tcpros_port=0):
  print(anonymous)

def Publisher(name, data_class):
  print("cde")
  print("ced")
  

def Rate(self, hz, reset=False):
  return 2 

def get_time():
  return 3

def is_shutdown():
  print("abc")




    

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
   
  


def publish(self, *args, **kwds):
  return 3

def sleep():
  return None

import logging

##definitions
def init_node(name, argv=None, anonymous=False, log_level=None, disable_rostime=False, disable_rosout=False, disable_signals=False, xmlrpc_port=0, tcpros_port=0):
  print(anonymous)

def Publisher(name, data_class):
  print("cde")

def Rate(self, hz, reset=False):
  return 2 

def get_time():
  return 3

def is_shutdown():
  print("abc")




    



def publish(self, *args, **kwds):
  return 3

def sleep():
  return None


