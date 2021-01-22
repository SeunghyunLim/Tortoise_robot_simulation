xterm -e "roscore" &
xterm -e "gazebo --verbose tortoise/tortoise.world" &
xterm -e "./legtool.py -c tortoise_gazebo.cfg"
