MULTIF Run Database
===================

This git repository contains a number of input ouput pairs from [MULTIF](https://github.com/vmenier/MULTIF/tree/develop).


File Format
-----------
Input and outputs to MULTIF are encoded in files named `*.input` and `*.output` respectively where each row corresponds to one run.
Output files also specify the fidelity level (0-13) and version in the format `*level6_v13.output`.

The input contains 175 variables corresponding to the 3D parameterization of the nozzle as specified in `general-3d.cfg`.
The output contains either 71 or 72 variables depending on the version, where the last column is the log10 of the residual decrease in SU2.

Levels
------
MULTIF supports a variety of fidelity levels involving different models (1D, 2D, 3D) as well as different mesh refinements.
Here we use the table of levels specified below and specified in `general-3d.cfg`:

0. NONIDEALNOZZLE, 1e-8, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
1. NONIDEALNOZZLE, 1e-8, AEROTHERMOSTRUCTURAL, NONLINEAR, 0.5
2. EULER, 2D, COARSE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
3. EULER, 2D, MEDIUM, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
4. EULER, 2D, FINE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
5. EULER, 3D, COARSE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
6. EULER, 3D, MEDIUM, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
7. EULER, 3D, FINE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
8. RANS, 2D, COARSE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
9. RANS, 2D, MEDIUM, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
10. RANS, 2D, FINE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
11. RANS, 3D, COARSE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
12. RANS, 3D, MEDIUM, AEROTHERMOSTRUCTURAL, LINEAR, 0.5
13. RANS, 3D, FINE, AEROTHERMOSTRUCTURAL, LINEAR, 0.5


Versions
--------
MULTIF is under active development and the output is known the vary between versions.
Here, version numbers correspond to the docker container builds of MULTIF featured on [docker hub](https://hub.docker.com/r/jeffreyhokanson/multif/tags/).


Campaigns
---------
Input sets have been generated in a number of campaigns, described below.
Numbers denote additional attemps using the same approach

* baseline: baseline design plus random samples in the random variables
* design: designs that approximately solve the design under uncertainty problem; similarly fixed design plus random samples of random variables.
* rand: randomly sampled points on the measure associated with the domain
* sweep: parameter sweeps starting at a random point and pointed in a random direction; each sweep contains 100 points.
* stretch: evenly spaced samples along identified ridge directions and randomly sampled in the orthogonal complement. Typically 10 points per ridge and 5 samples at each point.  Letters denote that the ridge directions were determined using rand and the preceeding stretches;
for example, `stretch2c_l0_v13` samples ridges built from level 0  version 13 data in `rand2`, `stretch2a_l0_v13`, and `stretch2b_l0_v13`.
* uniform: samples the domain using [Mitchell's best candidate](https://bl.ocks.org/mbostock/1893974) to attempt to evenly sample the 175 dimensional input space.
* extend: a greedy approach that attempts to sample each of the ridge directions with an equal number of points using Mitchell's best candidate.  Similar to stretch, letters denote samples built by refining the domain; e.g., `extend1c_l0_v13` was built using level 0 version 13 data for `uniform1`, `extend1a_l0_v13`, and `extend1b_l0_v13`.


Computational Effort
--------------------
In addition to the input output mappings, I've also recorded the total run time for each simulation I've performed.
In this directory is a file named `total_runtime.txt` that contains a record of every simulation run since November 2017.
Each row describes a single run of MULTI-F with each column encoding

* Total run time in seconds
* Basename of file run on (e.g., if run on `baseline.input` the row lists `baseline`)
* The md5sum has of this input file 
* The level of MULTI-F being run 
* The line number in the input file being run
* The data and time of completion
* (optional) the version of MULTIF being run (e.g., v24)
* (optional) the SST perturbation being run (e.g., false or SSTC1)



