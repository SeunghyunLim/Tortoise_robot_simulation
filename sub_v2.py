from trollius import From
import trollius
import pygazebo
import pygazebo.msg.joint_cmd_pb2
import logging
import eventlet

@trollius.coroutine
def callback(data):
    joint_cmd = joint_cmd_pb2.JointCmd.FromString(data)
    print(joint_cmd.name)


TOPIC_NAME = '/gazebo/default/tortoise/joint_cmd'
TOPIC_MSG_TYPE = 'gazebo.msgs.JointCmd'

@trollius.coroutine
def start():
    print('what')
    model_name = coxa_hinge0
    manager = yield From(pygazebo.connect())

    subscriber = manager.subscribe(TOPIC_NAME % model_name, TOPIC_MSG_TYPE, callback)
    print('2')
    while True:
        print('loop')
        eventlet.sleep(1)



if __name__ == "__main__":
    print("started")
    print(start())
