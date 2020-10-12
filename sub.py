from pygazebo.msg.gz_string_pb2 import GzString
import eventlet
import pygazebo

def callback(data):
    message = GzString.FromString(data)
    print('got message %s' % message.data[:4])

topic='/gazebo/default/test/request'
manager = pygazebo.Manager(('localhost', 11345))
manager.start()
sub = manager.subscribe(topic, 'gazebo.msgs.GzString', callback)

while True:
  eventlet.sleep(1)
