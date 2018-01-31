"""
This file provides simple functions to get paths to various data.
"""
import inspect, os
import numpy as np
here = os.path.dirname(__file__)

def scale_factors():
    """Scale factors of snapshots.

    Returns:
        array: The scale factors of the snapshots.

    """
    return np.array([0.25, 0.333333, 0.5, 0.540541, 0.588235, 0.645161, 0.714286, 0.8, 0.909091, 1.0])

def building_box_cosmologies():
    """Cosmologies for the building boxes aka the aemulus simulations.

    Columns are: Omega_bh^2 Omega_ch^2 w0 ns ln10As H0[km/s/Mpc] Neff sigma8.

    Returns:
        numpy.array: 40 by 8 array of the cosmologies for each simulation.

    """
    return np.loadtxt(path_to_building_box_cosmologies())

def test_box_cosmologies():
    """Cosmologies for the test boxes aka the aemulus simulations.

    Columns are: Omega_bh^2 Omega_ch^2 w0 ns ln10As H0[km/s/Mpc] Neff sigma8.

    Returns:
        numpy.array: 7 by 8 array of the cosmologies for each simulation.

    """
    return np.loadtxt(path_to_test_box_cosmologies())

def building_box_binned_mass_function(box, snapshot):
    """The binned mass function for a snapshot of a box.

    Units are Msun/h. Columns are M_low, M_high, Number, Total_Mass. 
    To get the average mass of halos in a bin divide Total_Mass/Number.

    Args:
        box (int): Index of the simulation box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: 10x4 array of binned mass function data.

    """
    return np.loadtxt(path_to_building_box_binned_mass_function(box, snapshot))

def building_box_binned_mass_function_covariance(box, snapshot):
    """The covariance matrix for the binned mass function 
    for a snapshot of a simulation box.

    Units are Msun/h.

    Args:
        box (int): Index of the simulation box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: 10x10 symmetric covariance matrix.

    """
    return np.loadtxt(path_to_building_box_binned_mass_function_covariance(box, snapshot))

def test_box_binned_mass_function(box, snapshot):
    """The binned mass function for a snapshot of a test box.

    Units are Msun/h. Columns are M_low, M_high, Number, Total_Mass. 
    To get the average mass of halos in a bin divide Total_Mass/Number.

    Args:
        box (int): Index of the test box; from 0-6.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: 10x4 array of binned mass function data.

    """
    return np.loadtxt(path_to_test_box_binned_mass_function(box, snapshot))

def test_box_binned_mass_function_covariance(box, snapshot):
    """The covariance matrix for the binned mass function 
    for a snapshot of a test box.

    Units are Msun/h.

    Args:
        box (int): Index of the test box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: 10x10 symmetric covariance matrix.

    """
    return np.loadtxt(path_to_test_box_binned_mass_function_covariance(box, snapshot))

########################
# Path functions below #
########################

def path_to_building_box_cosmologies():
    return here+"/building_box_cosmologies.txt"

def path_to_building_box_mass_functions(box):
    return here+"/mass_functions/building_boxes/Box%03d"%box

def path_to_building_box_binned_mass_function(box, snapshot):
    return path_to_building_box_mass_functions(box)+"/Box%03d_Z%d.txt"%(box, snapshot)

def path_to_building_box_binned_mass_function_covariance(box, snapshot):
    return path_to_building_box_mass_functions(box)+"/Box%03d_cov_Z%d.txt"%(box, snapshot)

def path_to_test_box_cosmologies():
    return here+"/test_box_cosmologies.txt"

def path_to_test_box_mass_functions(box):
    return here+"/mass_functions/test_boxes/combined/TestBox%03d"%box

def path_to_test_box_binned_mass_function(box, snapshot):
    return path_to_test_box_mass_functions(box)+"/TestBox%03d_mean_Z%d.txt"%(box, snapshot)

def path_to_test_box_binned_mass_function_covariance(box, snapshot):
    return path_to_test_box_mass_functions(box)+"/TestBox%03d_cov_Z%d.txt"%(box, snapshot)
