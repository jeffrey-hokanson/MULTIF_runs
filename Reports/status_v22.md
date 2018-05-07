# Status Report on MULTI-F v22


## Good Correlation Between Different Meshes at Same Fidelity
Looking at the sweeps, we see similar values for each QoI 
for coarse, medium, and fine meshes for 2D and 3D Euler.

![2D Euler](sweep3_00_2D_Euler_v22.png)
![3D Euler](sweep3_00_3D_Euler_v22.png)


## Substantial Differences Between Fidelities
However in some QoIs, notably thrust and Thermal Temperature,
we see substantial deviation between the sweeps. 
![Sweep](sweep3_00_v22.png)

To quantify how apart the various models are, 
the plot below shows the maximum difference 
between the output of each QoI normalized by the
difference between the smallest and largest value for each QoI.

![Max deviation](tab_corr_max_v22.png)
The numbers above denote the level in MULTI-F:

 0. 1D, Linear
 1. 1D, Nonlinear  

