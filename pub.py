import pygazebo
import sys
from pygazebo.msg.gz_string_pb2 import GzString
import time

n = 10
size = 1000
if len(sys.argv) > 2:
  n,size = map(int, sys.argv[1:3])

manager = pygazebo.Manager(('localhost', 11345))
manager.start()
topic = '/gazebo/default/test/request'
publisher = manager.advertise(topic, 'gazebo.msgs.GzString')

publisher.wait_for_listener()
for i in range(n):
  msg = GzString(data='%4d' % i  + ' '*(size-4))
  publisher.publish(msg)
  time.sleep(0.2)
