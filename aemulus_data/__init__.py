"""
This file provides simple functions to get paths to various data.
"""
import inspect, os
here = os.path.dirname(__file__)

def get_scale_factors():
    import numpy
    return numpy.array([0.25, 0.333333, 0.5, 0.540541, 0.588235, 0.645161, 0.714286, 0.8, 0.909091, 1.0])

def path_to_building_box_cosmologies():
    return here+"/building_box_cosmologies.txt"

def path_to_test_box_cosmologies():
    return here+"/test_box_cosmologies.txt"

def path_to_mass_functions():
    """Return the path to the mass function directories.
    """
    return here+"/mass_functions"

def path_to_building_boxes():
    """Return the path to the building box mass function directories.
    """
    return path_to_mass_functions()+"/building_boxes/"

def path_to_building_box(index):
    """Return the path to a building box mass function.
    """
    return path_to_building_boxes()+"Box%03d"%index

def path_to_building_box_data(index, snapindex):
    """Return the path to a building box mass function data file.
    """
    return path_to_building_box(index)+"/Box%03d_Z%d.txt"%(index, snapindex)

def path_to_building_box_covariance(index, snapindex):
    """Return the path to a building box mass function covariance.
    """
    return path_to_building_box(index)+"/Box%03d_cov_Z%d.txt"%(index, snapindex)

def path_to_test_boxes():
    """Return the path to the test box mass function directories.
    """
    return path_to_mass_functions()+"/test_boxes/averaged/"

def path_to_test_box(index):
    """Return the path to a test box mass function.
    """
    return path_to_test_boxes()+"TestBox%03d"%index

def path_to_test_box_data(index, snapindex):
    """Return the path to a test box mass function data file.
    """
    return path_to_test_box(index)+"/TestBox%03d_mean_Z%d.txt"%(index, snapindex)

def path_to_test_box_covariance(index, snapindex):
    """Return the path to a test box mass function covariance.
    """
    return path_to_test_box(index)+"/TestBox%03d_cov_Z%d.txt"%(index, snapindex)



if __name__ == "__main__":
    index, snapindex = 0, 9
    path = path_to_building_box_data(index, snapindex)
    print path
    import numpy as np
    data = np.genfromtxt(path)
    print data.shape

    path = path_to_building_box_covariance(index, snapindex)
    print path
    import numpy as np
    data = np.genfromtxt(path)
    print data.shape

    path = path_to_test_box_data(index, snapindex)
    print path
    import numpy as np
    data = np.genfromtxt(path)
    print data.shape

    path = path_to_test_box_covariance(index, snapindex)
    print path
    import numpy as np
    data = np.genfromtxt(path)
    print data.shape
