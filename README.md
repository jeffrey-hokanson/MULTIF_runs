MULTIF Run Database
===================

This git repository contains a number of input ouput pairs from [MULTIF](https://github.com/vmenier/MULTIF/tree/develop).


File Format
-----------
Input and outputs to MULTIF are encoded in files named `*.input` and `*.output` respectively where each row corresponds to one run.
Output files also specify the fidelity level (0-13) and version in the format `*level6_v13.output`.
The input contains 175 variables corresponding to the 3D parameterization of the nozzle.


Levels
------
MULTIF supports a variety of fidelity levels involving different models (1D, 2D, 3D) as well as different mesh refinements.
Here we use the table of levels specified below:

0. NONIDEALNOZZLE,1e-8,AEROTHERMOSTRUCTURAL,LINEAR,0.5
1. NONIDEALNOZZLE,1e-8,AEROTHERMOSTRUCTURAL,NONLINEAR,0.5
2. EULER,2D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5
3. EULER,2D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5
4. EULER,2D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5
5. EULER,3D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5
6. EULER,3D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5
7. EULER,3D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5
8. RANS,2D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5
9. RANS,2D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5
10. RANS,2D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5
11. RANS,3D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5
12. RANS,3D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5
13. RANS,3D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5





Versions
--------
MULTIF is under active development and the output is known the vary between versions.
Here, version numbers correspond to the docker container builds of MULTIF featured on [docker hub](https://hub.docker.com/r/jeffreyhokanson/multif/tags/).





