"""
Use the module to access mass function data.
"""
import numpy as np
import matplotlib.pyplot as plt
import aemulus_data as AD

if __name__ == "__main__":
    Volume = 1050.**3 #Mpc^3/h^3
    box = 2
    snapshot = 9
    sfs = AD.get_scale_factors()
    zs = 1./sfs - 1.
    a = sfs[snapshot]
    z = zs[snapshot]
    datapath = AD.path_to_building_box_data(box, snapshot)
    lMlo, lMhi, N, Mtot = np.genfromtxt(datapath, unpack=True)
    M_bins = 10**np.array([lMlo, lMhi]).T
    M = Mtot/N
    covpath = AD.path_to_building_box_covariance(box, snapshot)
    err = np.sqrt(np.diag(np.loadtxt(covpath)))*10
    plt.errorbar(M, N, err, ls='', marker='.', label=r"$z=%.2f$"%z)
    plt.xscale("log")
    plt.yscale("log")
    plt.legend(loc="lower left", frameon=False, fontsize=14)
    plt.xlabel(r"$\rm Mass\ [M_\odot]$")
    plt.ylabel(r"$\rm Number\ of\ Halos$")
    plt.title("Box%03d snapshot%d"%(box, snapshot))
    plt.subplots_adjust(left=0.15, bottom=0.15)
    plt.show()
