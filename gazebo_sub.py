from trollius import From
import trollius
import pygazebo
import pygazebo.msg.joint_cmd_pb2

TOPIC_NAME = '/gazebo/default/tortoise/joint_cmd'
TOPIC_MSG_TYPE = 'gazebo.msgs.JointCmd'


def callback(data):
    print('callback')
    message = pygazebo.msg.joint_cmd_pb2.JointCmd(position)
    print('Received message:', message.position)

@trollius.coroutine
def subscribe_loop():
    manager = yield From(pygazebo.connect())
    manager.start()
    subscriber = manager.subscribe(TOPIC_NAME, TOPIC_MSG_TYPE, callback)

    while True:
        print("Listening")
        print(subscriber)
        yield From(trollius.sleep(1.0))

#@trollius.coroutine
def request_and_listen():
    loop = trollius.get_event_loop()
    loop.run_until_complete(subscribe_loop())


if __name__ == "__main__":
    print("started")
    request_and_listen()
