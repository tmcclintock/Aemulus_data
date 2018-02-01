"""
This file takes in the test box data and combines the bins
and the covariance matrices.
"""
import numpy as np
import os, sys

Ntests = 7 #7 different test boxes
Nreals = 5 #5 realizations
Nreds = 10 #10 redshifts
Nbins = 10 #10 mass bins
lMedges = np.linspace(12.88527, 16, Nbins+1)

scale_factors = np.array([0.25,0.333333,0.5,0.540541,0.588235,
                          0.645161,0.714286,0.8,0.909091,1.0])
redshifts = 1./scale_factors - 1.0

inboxname = "TestBox%03d-%03d"
data_base = "./"
data_path = data_base+"full_mf_data/%s_full/%s_full_Z%d.txt"
cov_path = data_base+"covariances/%s_cov/%s_cov_Z%d.txt"

outboxname = "TestBox%03d"
outbase = data_base+"combined/"+outboxname
out_data_path = outbase+"/"+outboxname+"_mean_Z%d.txt"
out_cov_path = outbase+"/"+outboxname+"_cov_Z%d.txt"

for box in xrange(0, Ntests):
    #Define this outboxname
    thisoutbox = outboxname%(box)

    print "Combining %s"%thisoutbox
    for snap in xrange(0, Nreds):
        Nhalos = np.zeros(Nbins)
        Mmean = np.zeros(Nbins)
        cov = np.zeros((Nbins, Nbins))
        lMlo = np.copy(lMedges[:-1])
        lMhi = np.copy(lMedges[1:])

        print "\tfor Z%d"%snap
        #First try to make the ouput directory
        outpath = outbase%(box)
        os.system("mkdir -p %s"%outpath)
        
        #Nreals=1
        for r_index in xrange(0, Nreals):
            Ml, Mh, Nr, Mtot = np.loadtxt(data_path%(inboxname%(box,r_index),inboxname%(box,r_index),snap)).T
            Nhalos += Nr
            Mmean += Mtot
            cov_in = np.loadtxt(cov_path%(inboxname%(box,r_index),inboxname%(box,r_index),snap))
            cov += cov_in/Nreals**2
            continue
        inds = (Nhalos > 0)
        lMlo = lMlo[inds]
        lMhi = lMhi[inds]
        Nhalos = Nhalos[inds]
        Mmean = Mmean[inds]
        cov = cov[inds]
        cov = cov[:,inds]
        Mmean /= Nhalos #Go from Mtot to Mmean
        Nhalos /= Nreals
        out = np.array([lMlo, lMhi, Nhalos, Mmean]).T
        #Save the combined data and the combined covariance
        np.savetxt(out_data_path%(box,box,snap), out, header="M_low[Msun/h] M_high[Msun/h] Number M_total[Msun/h]")
        np.savetxt(out_cov_path%(box, box, snap), cov)
        continue
    print "\tcompleted %s"%thisoutbox
    continue # end box
