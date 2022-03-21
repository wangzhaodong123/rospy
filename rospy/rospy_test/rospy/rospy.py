import loggingfunc

# initialize node
def init_node(name, argv=None, anonymous=False, log_level=None, disable_rostime=False, disable_rosout=False, disable_signals=False, xmlrpc_port=0, tcpros_port=0):
  # configure logging 
  loggingfunc.configlogging();

# close interface
def is_shutdown():
  print("is_shutdown")

def spin():
  print("spin")
