# Tortoise_robot_simulation
Simulation of tortoise-like robot's gait with inverse kinematics, using gazebo. 

This is a personalized version of 'Legtool'(by jpieper) for analyzing the gait of tortoise-like robot using inverse kinematics.

Overall methods such as inverse kinematics, UI, etc. are from opensource toolkit __legtool__, which is from https://github.com/jpieper/legtool. 


- In folder [tortoise](https://github.com/SeunghyunLim/Tortoise_robot_simulation/tree/master/tortoise), I made _tortoise.world_ which has sdf formatted tortoise robot model and some settings of environments, physics, sensors. 
- The _stl_ files were designed with Inventor 2021, and joints of the robot are composed of 12 _Dynamixel AX-12A_.


<center><img src="https://github.com/SeunghyunLim/Tortoise_robot_simulation/blob/master/img/tortoise_like_robot_gazebo.png" alt="drawing"></center>

| __Triangular__ gait | __Diagonal__ gait |
|---|---|
|![a](https://github.com/SeunghyunLim/Tortoise_robot_simulation/blob/master/gif/triangular_example.gif)|![a](https://github.com/SeunghyunLim/Tortoise_robot_simulation/blob/master/gif/diagonal_example.gif)|


## Features
- Inverse kinematics of 3 DoF tortoise-like robot.
- Graphical representation with opensource library __legtool__.
- You sholud use __pygazebo__, which make possible to simulate the robot.
- Tortoise-like robot has belly side, which makes contacts with floors during gaits.
- Friction of belly side has 0.001 mu and tip side has 1.0 mu in ode.
- All joints of the robot have torque sensors, so that we can measure the loaded torques.
- Measured torques can be used to caculate the __Work__ or CoT(Cost of transport), etc.


| Totrque from __Crawl-Triangular__ gait | Totrque from __Crawl-Diagonal__ gait |
|---|---|
|![a](https://github.com/SeunghyunLim/Tortoise_robot_simulation/blob/master/gif/crawl_triangular.gif)|![a](https://github.com/SeunghyunLim/Tortoise_robot_simulation/blob/master/gif/crawl_diagonal.gif)|


## Dependencies
- legtool (https://github.com/jpieper/legtool)
- pygazebo (https://github.com/jpieper/pygazebo)
- SCons
- Pyside
- pygame

## How to use
1. Firstly, build all dependencies. (current env: python 2.7, ubuntu 18.04, gazebo 9)
2. git clone this repository to your home directory. (You can change your directory, but then, you should change the roots in sim_paner_init.sh)
3. Build required files:

```bash
scons
```

4. In the terminal, run bellow code
```bash
/home/usr/legtool_tortoise_robot/sim_panel_init.sh
```
Or, you can just drag and drop the __sim_panel_init.sh__ to the terminal, and run it.

5. On UI panel, check if __Configure Gazebo__ has proper model name(_tortoise_).

6. You can change the parameters and models. 

- _tortoise.world_ : Coxa length 22mm, Femur length 68mm, Tibia length 75mm, leg position -95~95 mm
- _tortoise_rough.world_ : Coxa length 15mm, Femur length 60mm, Tibia length 75mm, leg position -95~95 mm
