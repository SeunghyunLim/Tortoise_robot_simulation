import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

PATH = "./crawl_diagonal_csv/"
Format = ".csv"


# data title clarification
coxa_t_header = ["sim_time", "torque"]
femur_t_header = ["sim_time", "torque"]
tibia_t_header = ["sim_time", "torque"]

coxa_w_header = ["sim_time", "ang_vel"]
femur_w_header = ["sim_time", "ang_vel"]
tibia_w_header = ["sim_time", "ang_vel"]


# data load
coxa_t = pd.read_csv(PATH + 'coxa_torque' + Format, header = 0, names = coxa_t_header)
femur_t = pd.read_csv(PATH + 'femur_torque' + Format, header = 0, names = femur_t_header)
tibia_t = pd.read_csv(PATH + 'tibia_torque' + Format, header = 0, names = femur_t_header)

coxa_w = pd.read_csv(PATH + 'coxa_w' + Format, header = 0, names = coxa_w_header)
femur_w = pd.read_csv(PATH + 'femur_w' + Format, header = 0, names = femur_w_header)
tibia_w = pd.read_csv(PATH + 'tibia_w' + Format, header = 0, names = tibia_w_header)


# sim_time calibration
simtime_list = [coxa_t.sim_time[0], coxa_w.sim_time[0],
                     femur_t.sim_time[0], femur_w.sim_time[0],
                    tibia_t.sim_time[0], tibia_w.sim_time[0]]
max_simt = max(simtime_list)
max_index = simtime_list.index(max_simt)


#calibrated_simt = int(max_simt - simtime_list)*1000
start_simt_list = np.int64((max_simt - simtime_list)*1000)

time_sync = [coxa_t.sim_time[start_simt_list[0]],
             coxa_w.sim_time[start_simt_list[1]],
             femur_t.sim_time[start_simt_list[2]],
             femur_w.sim_time[start_simt_list[3]],
            tibia_t.sim_time[start_simt_list[4]],
            tibia_w.sim_time[start_simt_list[5]]]
standard_t = time_sync[max_index]
i = 0
for t in time_sync:
    if t != standard_t:
        start_simt_list[i] = start_simt_list[i] + 1
    i += 1
# simulation time and index are synced as start_simt_list

coxa_work = 0
femur_work = 0
tibia_work = 0
time_shift = 3440
for i in range(stride_time):
    coxa_work = coxa_work + abs(coxa_t.torque[start_simt_list[0] + i+ time_shift] *
                                coxa_w.ang_vel[start_simt_list[1] + i+ time_shift] * 0.001)
    femur_work = femur_work + abs(femur_t.torque[start_simt_list[2] + i+ time_shift] *
                                  femur_w.ang_vel[start_simt_list[3] + i+ time_shift] * 0.001)
    tibia_work = tibia_work + abs(tibia_t.torque[start_simt_list[4] + i+ time_shift] *
                                  tibia_w.ang_vel[start_simt_list[5] + i+ time_shift] * 0.001)

work = coxa_work + femur_work + tibia_work


print('---Required Work---')
print('coxa : ', coxa_work)
print('femur : ', femur_work)
print('tibia : ', tibia_work)
print('total work : ', work)

print()

print('---Maximum torque---')
print('coxa : ', max(coxa_t.torque))
print('femur : ', max(femur_t.torque))
print('tibia : ', max(tibia_t.torque))
