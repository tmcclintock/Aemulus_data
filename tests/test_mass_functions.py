import pytest
import aemulus_data as ad
from os.path import dirname, join
import numpy as np
import numpy.testing as npt

sfs = ad.scale_factors()
Nz = len(sfs)
Nbb = 40
Ntb = 7

def test_mf_shapes():
    for box in xrange(0, 40):
        for snap in xrange(0, 10):
            bbmf = ad.building_box_binned_mass_function(box, snap)
            Nbins = len(bbmf)
            assert Nbins >= 0
            npt.assert_equal(4, len(bbmf[0]))
    for box in xrange(0, 7):
        for snap in xrange(0, 10):
            tbmf = ad.test_box_binned_mass_function(box, snap)
            Nbins = len(tbmf)
            assert Nbins >= 0
            npt.assert_equal(4, len(tbmf[0]))

def test_edges():
    for box in xrange(0, 40):
        for snap in xrange(0, 10):
            bbmf = ad.building_box_binned_mass_function(box, snap)
            Mlo = bbmf[:,0]
            Mhi = bbmf[:,1]
            npt.assert_array_less(Mlo, Mhi)
    for box in xrange(0, 7):
        for snap in xrange(0, 10):
            tbmf = ad.test_box_binned_mass_function(box, snap)
            Mlo = tbmf[:,0]
            Mhi = tbmf[:,1]
            npt.assert_array_less(Mlo, Mhi)

def test_covs():
    for box in xrange(0, 40):
        for snap in xrange(0, 10):
            cov = ad.building_box_binned_mass_function_covariance(box, snap)
            assert len(cov)==len(cov[0])
            npt.assert_array_equal(cov.transpose(), cov) #Symmetric
    for box in xrange(0, 7):
        for snap in xrange(0, 10):
            cov = ad.test_box_binned_mass_function_covariance(box, snap)
            assert len(cov)==len(cov[0])
            npt.assert_array_equal(cov.transpose(), cov) #Symmetric
