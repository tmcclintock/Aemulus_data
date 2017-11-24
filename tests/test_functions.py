import pytest
import aemulus_data as ad
from os.path import dirname, join
import numpy as np
import numpy.testing as npt

scale_factors = [0.25, 0.333333, 0.5, 0.540541, 0.588235, 0.645161, 0.714286, 0.8, 0.909091, 1.0]

z = 1./np.array(scale_factors) - 1

def test_scale_factors():
    npt.assert_array_equal(scale_factors, ad.get_scale_factors())

def test_redshifts():
    ztest = 1./ad.get_scale_factors() - 1
    npt.assert_array_equal(ztest, z)

def test_cosmology_shapes():
    bbcos = ad.get_building_box_cosmologies()
    npt.assert_array_equal((40,8), bbcos.shape)
    tbcos = ad.get_test_box_cosmologies()
    npt.assert_array_equal((7,8), tbcos.shape)
