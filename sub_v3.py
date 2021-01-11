from trollius import From
import trollius as asyncio
import pygazebo
import pygazebo.msg.joint_cmd_pb2
import logging
import eventlet

@asyncio.coroutine


class GazeboController(object):
    def __init__(self, model_name, servo_name_map=None):
        self.model_name = model_name

        self.servo_name_map = dict(
            (key, model_name + '::' + value)
            for key, value in servo_name_map.iteritems())
        print(servo_name_map)

    @asyncio.coroutine
    def start(self):
        model_name = self.model_name

        self.manager = yield From(pygazebo.connect())

        self.subscriber = self.manager.subscribe(
            '/gazebo/default/%s/joint_cmd' % model_name,
            'gazebo.msgs.JointCmd',
            self._receive_joint_cmd)

        self.joint_cmd = joint_cmd_pb2.JointCmd()
        self.joint_cmd.axis = 0
        self.joint_cmd.position.target = 0
        self.joint_cmd.position.p_gain = 10.0
        self.joint_cmd.position.i_gain = 2.0
        self.joint_cmd.position.d_gain = 0.2

        self._servo_angles = {}

    def _receive_joint_cmd(self, data):
        joint_cmd = joint_cmd_pb2.JointCmd.FromString(data)
        index = self.servo_name_map.index(self.joint_cmd.name)
        if index < 0:
            return

        if (not joint_cmd.HasField('position') or
            not joint_cmd.position.HasField('target')):
            return
        self._servo_angles[index] = joint_cmd.position.target
        print(self._servo_angles)


def main():
    GC = GazeboController('tortoise', {0: 'coxa_hinge0', 1: 'femur_hinge0', 2: 'tibia_hinge0', 3: 'coxa_hinge1', 4: 'femur_hinge1', 5: 'tibia_hinge1', 6: 'coxa_hinge2', 7: 'femur_hinge2', 8: 'tibia_hinge2', 9: 'coxa_hinge3', 10: 'femur_hinge3', 11: 'tibia_hinge3'})
    print(GC)

if __name__ == "__main__":
    mygen = main()
    for i in mygen:
        print(i)
