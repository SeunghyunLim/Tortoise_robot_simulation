import rospy
import re
from std_msgs.msg import String

def callback(data):
    data = str(data)
    data = data.replace("data: ", "")
    data = data.replace("\\", "")
    data = data.replace("\n", "")
    data = data.replace("  ", "")
    test = re.split(', |"{|: |}"', data)
    test.pop(0)
    test.pop()
    test = [float(i) for i in test]
    print(test)

def listener():
    rospy.init_node('Listener', anonymous=True)
    rospy.Subscriber("/cmd", String, callback)
    rospy.spin()

if __name__ == "__main__":
	try:
		listener()

	except KeyboardInterrupt:
		print("Interrupted by keyboard")
