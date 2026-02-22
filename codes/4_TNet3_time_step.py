# -*- coding: utf-8 -*-
# %%
"""
Created on Mon May 23 13:17:36 2022

@author: ps28866
"""
import tsnet
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime 

plt.close('all') 

# %% TNet3: Use default time step
#-------------------------------------------------
start = datetime.now()

# open an example network and create a transient model
inp_file = 'networks/Tnet3.inp'
tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
#-------------------------------------------------
wavespeed = 1200
tm.set_wavespeed(wavespeed)

# Set simulation duration
#-------------------------------------------------
tf = 20 # simulation period [s]
tm.set_time(tf)

# Add burst
#-------------------------------------------------
ts = 1 # burst start time
tc = 1 # time for burst to fully develop
final_burst_coeff = 0.01 # final burst coeff [ m^3/s/(m H20)^(1/2)]
tm.add_burst('JUNCTION-73', ts, tc, final_burst_coeff)

# Initialize steady state simulation
#-------------------------------------------------
t0 = 0. # initialize the simulation at 0s
engine = 'DD' # or Epanet
tm = tsnet.simulation.Initializer(tm, t0, engine)

# Transient simulation
#-------------------------------------------------
result_obj = 'Tnet3_default_time_step' # name of the object for saving simulation results
tm_default= tsnet.simulation.MOCSimulator(tm, result_obj)

sim_time = datetime.now() - start

# Print timestep and simulation time
#-------------------------------------------------
print('Actual simulation time for time step =%.5f s is %s' %(tm.time_step, sim_time) ) 

# %% User defined time step

# Large timestep is not allowed
#-------------------------------------------------

tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
#-------------------------------------------------
wavespeed = 1200
tm.set_wavespeed(wavespeed)

# Set time step
#-------------------------------------------------
tf = 20 # simulation period [s]
dt = 1
tm.set_time(tf, dt)

# %% User defined time step

# Speficy time step dt = 0.005s
#-------------------------------------------------

start = datetime.now()
# open an example network and create a transient model
tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
#-------------------------------------------------
wavespeed = 1200
tm.set_wavespeed(wavespeed)

# Set time step
#-------------------------------------------------
tf = 20 # simulation period [s]
dt = 0.005 
tm.set_time(tf, dt)

# Add burst
#-------------------------------------------------
ts = 1 # burst start time
tc = 1 # time for burst to fully develop
final_burst_coeff = 0.01 # final burst coeff [ m^3/s/(m H20)^(1/2)]
tm.add_burst('JUNCTION-73', ts, tc, final_burst_coeff)

# Initialize steady state simulation
#-------------------------------------------------
t0 = 0. # initialize the simulation at 0s
engine = 'DD' # or Epanet
tm = tsnet.simulation.Initializer(tm, t0, engine)

# Transient simulation
#-------------------------------------------------
result_obj = 'Tnet3_timestep_005' # name of the object for saving simulation results
tm_005= tsnet.simulation.MOCSimulator(tm, result_obj)
sim_time = datetime.now() - start

# Print timestep and simulation time
#-------------------------------------------------
print('Actual simulation time for time step =%.5f s is %s' %(tm.time_step, sim_time) ) 
# %% User defined time step

# Speficy (a smaller) time step dt = 0.002s
#-------------------------------------------------
start = datetime.now()
# open an example network and create a transient model
tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
#-------------------------------------------------
wavespeed = 1200
tm.set_wavespeed(wavespeed)

# Set time step
#-------------------------------------------------
tf = 20 # simulation period [s]
dt = 0.002 
tm.set_time(tf, dt)

# Add burst
#-------------------------------------------------
ts = 1 # burst start time
tc = 1 # time for burst to fully develop
final_burst_coeff = 0.01 # final burst coeff [ m^3/s/(m H20)^(1/2)]
tm.add_burst('JUNCTION-73', ts, tc, final_burst_coeff)

# Initialize steady state simulation
#-------------------------------------------------
t0 = 0. # initialize the simulation at 0s
engine = 'DD' # or Epanet
tm = tsnet.simulation.Initializer(tm, t0, engine)

# Transient simulation
#-------------------------------------------------
result_obj = 'Tnet3_default_time step' # name of the object for saving simulation results
tm_002= tsnet.simulation.MOCSimulator(tm,result_obj)
sim_time = datetime.now() - start

# Print timestep and simulation time
#-------------------------------------------------
print('Actual simulation time for time step =%.5f s is %s' %(tm.time_step, sim_time) ) 

# %% Plot results

# report results
#-------------------------------------------------
node1 = 'JUNCTION-16'
node2 = 'JUNCTION-20'
node3 = 'JUNCTION-30'
node4 = 'JUNCTION-45'
node5 = 'JUNCTION-90'

fig, axs = plt.subplots(1,3,figsize=(15,5), dpi=80, facecolor='w', edgecolor='k')
axs[0].plot(tm_default.simulation_timestamps,tm_default.get_node(node1).head-tm_default.get_node(node1).head[0],'C0-',label='JUNCTION-16', linewidth=2.5)
axs[0].plot(tm_default.simulation_timestamps,tm_default.get_node(node2).head-tm_default.get_node(node2).head[0],'C1-',label='JUNCTION-20', linewidth=2.5)
axs[0].plot(tm_default.simulation_timestamps,tm_default.get_node(node3).head-tm_default.get_node(node3).head[0],'C2-', label='JUNCTION-30',linewidth=2.5)
axs[0].plot(tm_default.simulation_timestamps,tm_default.get_node(node4).head-tm_default.get_node(node4).head[0],'C3-', label='JUNCTION-45',linewidth=2.5)
axs[0].plot(tm_default.simulation_timestamps,tm_default.get_node(node5).head-tm_default.get_node(node5).head[0],'C4-',label='JUNCTION-90', linewidth=2.5)
axs[0].set_xlim([tm_default.simulation_timestamps[0],tm_default.simulation_timestamps[-1]])
axs[0].set_ylim([-45,15])
axs[0].set_xlabel("Time [s]", fontsize=14)
axs[0].set_ylabel("Head change [m]", fontsize=14)
axs[0].legend(loc='best')
axs[0].set_title('Time step = 0.01154s', fontsize=14)

axs[1].plot(tm_005.simulation_timestamps,tm_005.get_node(node1).head-tm_005.get_node(node1).head[0],'C0',label='JUNCTION-16', linewidth=2.5)
axs[1].plot(tm_005.simulation_timestamps,tm_005.get_node(node2).head-tm_005.get_node(node2).head[0],'C1',label='JUNCTION-20', linewidth=2.5)
axs[1].plot(tm_005.simulation_timestamps,tm_005.get_node(node3).head-tm_005.get_node(node3).head[0],'C2',label='JUNCTION-30', linewidth=2.5)
axs[1].plot(tm_005.simulation_timestamps,tm_005.get_node(node4).head-tm_005.get_node(node4).head[0],'C3',label='JUNCTION-45', linewidth=2.5)
axs[1].plot(tm_005.simulation_timestamps,tm_005.get_node(node5).head-tm_005.get_node(node5).head[0],'C4',label='JUNCTION-90', linewidth=2.5)
axs[1].set_xlim([tm_005.simulation_timestamps[0],tm_005.simulation_timestamps[-1]])
axs[1].set_ylim([-45,15])
axs[1].set_xlabel("Time [s]", fontsize=14)
axs[1].legend(loc='lower right')
axs[1].set_title('Time step = 0.00517s', fontsize=14)

axs[2].plot(tm_002.simulation_timestamps,tm_002.get_node(node1).head-tm_002.get_node(node1).head[0],'C0',label='JUNCTION-16', linewidth=2.5)
axs[2].plot(tm_002.simulation_timestamps,tm_002.get_node(node2).head-tm_002.get_node(node2).head[0],'C1',label='JUNCTION-20', linewidth=2.5)
axs[2].plot(tm_002.simulation_timestamps,tm_002.get_node(node3).head-tm_002.get_node(node3).head[0],'C2',label='JUNCTION-30', linewidth=2.5)
axs[2].plot(tm_002.simulation_timestamps,tm_002.get_node(node4).head-tm_002.get_node(node4).head[0],'C3',label='JUNCTION-45', linewidth=2.5)
axs[2].plot(tm_002.simulation_timestamps,tm_002.get_node(node5).head-tm_002.get_node(node5).head[0],'C4',label='JUNCTION-90', linewidth=2.5)
axs[2].set_xlim([tm_002.simulation_timestamps[0],tm_002.simulation_timestamps[-1]])
axs[2].set_xlabel("Time [s]", fontsize=14)
axs[2].set_ylim([-45,15])
axs[2].legend(loc='lower right')
axs[2].set_title('Time step = 0.00202s', fontsize=14)

plt.show()
plt.tight_layout()
fig.savefig('./networks/Tnet3_burst_timestep.pdf', format='pdf',dpi=100)