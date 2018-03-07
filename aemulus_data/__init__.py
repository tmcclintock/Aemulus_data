"""
This file provides simple functions to get paths to various data.
"""
import inspect, os
import numpy as np
here = os.path.dirname(__file__)

def scale_factors():
    """Scale factors of snapshots.

    Returns:
        array: Scale factors of the snapshots.

    """
    return np.array([0.25, 0.333333, 0.5, 0.540541, 0.588235, 0.645161, 0.714286, 0.8, 0.909091, 1.0])

def highres_scale_factors():
    """Scale factors of snapshots of the highres simulations.

    Note: these are not the same scale factors as those of the building and test boxes.

    Returns:
        array: Scale factors of highres snapshots.

    """
    return np.array([0.165913, 0.246189, 0.323199, 0.486149, 0.513345, 0.564651, 0.612689, 0.683156, 0.761728, 0.804340, 0.849337, 0.896850, 0.934222, 1.0])
    
def building_box_cosmologies():
    """Cosmologies for the building boxes aka the aemulus simulations.

    Columns are: Omega_bh^2 Omega_ch^2 w0 ns ln10As H0[km/s/Mpc] Neff sigma8.

    Returns:
        numpy.array: 40 by 8 array of the cosmologies for each simulation.

    """
    return np.loadtxt(_path_to_building_box_cosmologies())

def test_box_cosmologies():
    """Cosmologies for the test boxes.

    Columns are: Omega_bh^2 Omega_ch^2 w0 ns ln10As H0[km/s/Mpc] Neff

    Returns:
        numpy.array: 7 by 8 array of the cosmologies for each simulation.

    """
    return np.loadtxt(_path_to_test_box_cosmologies())

def highres_box_cosmologies():
    """Cosmologies for the highres boxes.

    Note: this doesn't contain sigma8.

    Columns are: Omega_bh^2 Omega_ch^2 w0 ns ln10As H0[km/s/Mpc] Neff

    Returns:
        numpy.array: 40 by 7 array of the cosmologies for each simulation.

    """
    return np.loadtxt(_path_to_highres_box_cosmologies())


def building_box_binned_mass_function(box, snapshot):
    """The binned mass function for a snapshot of a box.

    Units are Msun/h. Columns are M_low, M_high, Number, Total_Mass. 
    To get the average mass of halos in a bin divide Total_Mass/Number.

    Args:
        box (int): Index of the simulation box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: Nbinsx4 array of binned mass function data.

    """
    return np.loadtxt(_path_to_building_box_binned_mass_function(box, snapshot))

def building_box_binned_mass_function_covariance(box, snapshot):
    """The covariance matrix for the binned mass function 
    for a snapshot of a simulation box.

    Units are Msun/h.

    Args:
        box (int): Index of the simulation box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: NbinsxNbins symmetric covariance matrix.

    """
    return np.loadtxt(_path_to_building_box_binned_mass_function_covariance(box, snapshot))

def test_box_binned_mass_function(box, snapshot):
    """The binned mass function for a snapshot of a test box.

    Units are Msun/h. Columns are M_low, M_high, Number, Total_Mass. 
    To get the average mass of halos in a bin divide Total_Mass/Number.

    Args:
        box (int): Index of the test box; from 0-6.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: Nbinsx4 array of binned mass function data.

    """
    return np.loadtxt(_path_to_test_box_binned_mass_function(box, snapshot))

def test_box_binned_mass_function_covariance(box, snapshot):
    """The covariance matrix for the binned mass function 
    for a snapshot of a test box.

    Units are Msun/h.

    Args:
        box (int): Index of the test box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: NbinsxNbins symmetric covariance matrix.

    """
    return np.loadtxt(_path_to_test_box_binned_mass_function_covariance(box, snapshot))

def individual_test_box_binned_mass_function(box, snapshot, realization):
    """The binned mass function for a snapshot of a test box.

    Units are Msun/h. Columns are M_low, M_high, Number, Total_Mass. 
    To get the average mass of halos in a bin divide Total_Mass/Number.

    Args:
        box (int): Index of the test box; from 0-6.
        snapshot (int): Index of the snapshot; from 0-9.
        realization (int): Index of the realization; from 0-4.

    Returns:
        numpy.array: Nbinsx4 array of binned mass function data.

    """
    data = np.loadtxt(_path_to_individual_test_box_binned_mass_function(box, snapshot, realization))
    Mtot = data[:,-1]
    inds = (Mtot > 0)
    data = data[inds]
    data[:,-1] /= data[:,-2] #Convert Mtot to Mmean
    return data

def individual_test_box_binned_mass_function_covariance(box, snapshot, realization):
    """The covariance matrix for the binned mass function 
    for a snapshot of a test box.

    Units are Msun/h.

    Args:
        box (int): Index of the test box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.
        realization (int): Index of the realization; from 0-4.

    Returns:
        numpy.array: NbinsxNbins symmetric covariance matrix.

    """
    cov = np.loadtxt(_path_to_individual_test_box_binned_mass_function_covariance(box, snapshot, realization))
    inds = (np.fabs(cov[0]) > 0)
    cov = cov[inds]
    cov = cov[:,inds]
    return cov

def big_box_binned_mass_function(box, snapshot):
    """The binned mass function for a snapshot of a big box.

    Units are Msun/h. Columns are M_low, M_high, Number, Total_Mass. 
    To get the average mass of halos in a bin divide Total_Mass/Number.

    Args:
        box (int): Index of the big box; from 0-6.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: Nbinsx4 array of binned mass function data.

    """
    return np.loadtxt(_path_to_big_box_binned_mass_function(box, snapshot))


def big_box_binned_mass_function_covariance(box, snapshot):
    """The covariance matrix for the binned mass function 
    for a snapshot of a big box.

    Units are Msun/h.

    Args:
        box (int): Index of the big box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: NbinsxNbins symmetric covariance matrix.

    """
    return np.loadtxt(_path_to_big_box_binned_mass_function_covariance(box, snapshot))

def medium_box_binned_mass_function(box, snapshot):
    """The binned mass function for a snapshot of a medium box.

    Units are Msun/h. Columns are M_low, M_high, Number, Total_Mass. 
    To get the average mass of halos in a bin divide Total_Mass/Number.

    Args:
        box (int): Index of the medium box; from 0-6.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: Nbinsx4 array of binned mass function data.

    """
    return np.loadtxt(_path_to_medium_box_binned_mass_function(box, snapshot))


def medium_box_binned_mass_function_covariance(box, snapshot):
    """The covariance matrix for the binned mass function 
    for a snapshot of a medium box.

    Units are Msun/h.

    Args:
        box (int): Index of the medium box; from 0-39.
        snapshot (int): Index of the snapshot; from 0-9.

    Returns:
        numpy.array: NbinsxNbins symmetric covariance matrix.

    """
    return np.loadtxt(_path_to_medium_box_binned_mass_function_covariance(box, snapshot))

def highres_box_binned_mass_function(box, snapshot):
    """The binned mass function for a snapshot of a highres box.

    Units are Msun/h. Columns are M_low, M_high, Number, Mean_Mass. 

    Args:
        box (int): Index of the medium box; 11 or 14.
        snapshot (int): Index of the snapshot; from 0-13.

    Returns:
        numpy.array: Nbinsx4 array of binned mass function data.

    """
    if box not in [11,14]:
        raise Exception("Highres Box %d hasn't been run yet."%box)
    return np.loadtxt(_path_to_highres_box_binned_mass_function(box, snapshot))


def highres_box_binned_mass_function_covariance(box, snapshot):
    """The covariance matrix for the binned mass function 
    for a snapshot of a highres box.

    Units are Msun/h.

    Args:
        box (int): Index of the medium box; 11 or 14.
        snapshot (int): Index of the snapshot; from 0-13.

    Returns:
        numpy.array: symmetric covariance matrix.

    """
    if box not in [11,14]:
        raise Exception("Highres Box %d hasn't been run yet."%box)
    return np.loadtxt(_path_to_highres_box_binned_mass_function_covariance(box, snapshot))

########################
# Path functions below #
########################

def _path_to_building_box_cosmologies():
    return here+"/building_box_cosmologies.txt"

def _path_to_building_box_mass_functions(box):
    return here+"/mass_functions/building_boxes/Box%03d"%box

def _path_to_building_box_binned_mass_function(box, snapshot):
    return _path_to_building_box_mass_functions(box)+"/Box%03d_Z%d.txt"%(box, snapshot)

def _path_to_building_box_binned_mass_function_covariance(box, snapshot):
    return _path_to_building_box_mass_functions(box)+"/Box%03d_Z%d_cov.txt"%(box, snapshot)

def _path_to_test_box_cosmologies():
    return here+"/test_box_cosmologies.txt"

def _path_to_test_box_mass_functions(box):
    return here+"/mass_functions/test_boxes/combined/TestBox%03d"%box

def _path_to_highres_box_cosmologies():
    return here+"/highres_box_cosmologies.txt"

def _path_to_test_box_binned_mass_function(box, snapshot):
    return _path_to_test_box_mass_functions(box)+"/TestBox%03d_Z%d.txt"%(box, snapshot)

def _path_to_test_box_binned_mass_function_covariance(box, snapshot):
    return _path_to_test_box_mass_functions(box)+"/TestBox%03d_Z%d_cov.txt"%(box, snapshot)

def _path_to_individual_test_box_mass_functions(box, realization):
    return here+"/mass_functions/test_boxes/TestBox%03d-%03d"%(box,realization)

def _path_to_individual_test_box_binned_mass_function(box, snapshot, realization):
    return _path_to_individual_test_box_mass_functions(box, realization)+"/TestBox%03d-%03d_Z%d.txt"%(box, realization, snapshot)

def _path_to_individual_test_box_binned_mass_function_covariance(box, snapshot, realization):
    return here+"/mass_functions/test_boxes/TestBox%03d-%03d/TestBox%03d-%03d_Z%d_cov.txt"%(box, realization, box, realization, snapshot)

def _path_to_big_box_binned_mass_function(box, snapshot):
    return _path_to_big_box_mass_functions(box)+"Bigbox_mf_%03d-000_Z%d.txt"%(box, snapshot)

def _path_to_big_box_binned_mass_function_covariance(box, snapshot):
    return _path_to_big_box_mass_functions(box)+"Bigbox_mf_%03d-000_Z%d_cov.txt"%(box, snapshot)

def _path_to_big_box_mass_functions(box):
    return here+"/mass_functions/big_boxes/"

def _path_to_medium_box_binned_mass_function(box, snapshot):
    return _path_to_medium_box_mass_functions(box)+"Medbox_mf_%03d-000_Z%d.txt"%(box, snapshot)

def _path_to_medium_box_binned_mass_function_covariance(box, snapshot):
    return _path_to_medium_box_mass_functions(box)+"Medbox_mf_%03d-000_Z%d_cov.txt"%(box, snapshot)

def _path_to_medium_box_mass_functions(box):
    return here+"/mass_functions/medium_boxes/"

def _path_to_highres_box_binned_mass_function(box, snapshot):
    return _path_to_highres_box_mass_functions(box)+"HRBox%03d_Z%d.txt"%(box, snapshot)

def _path_to_highres_box_binned_mass_function_covariance(box, snapshot):
    return _path_to_highres_box_mass_functions(box)+"HRBox%03d_Z%d_cov.txt"%(box, snapshot)

def _path_to_highres_box_mass_functions(box):
    return here+"/mass_functions/highres_boxes/HRBox%03d/"%box

