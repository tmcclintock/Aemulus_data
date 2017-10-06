# Mass functions
This directory contains the halo mass functions measured in the building simulations and the testing simulations. There are forty building simulations, and the path to the mass function of an individual simulation is ```building_boxes/Box%03d/Box%03d_Z%d.txt```, where you need to specifiy a box index (0-40) and a snapshot index (0-9). ```Z0``` is a redshift of 3 and ```Z9``` is a redshift of 0. Files with ```cov``` are covariance matrices. A similar directory structure exists for the testboxes.

Note: The testboxes actually used for validation are in ```test_boxes/averaged```.