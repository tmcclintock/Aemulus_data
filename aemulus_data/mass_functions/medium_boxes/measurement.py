import numpy as np
import sys, os
import pandas as pd


inbase = "/nfs/slac/g/ki/ki22/cosmo/tmcclint/Medbox_halos/halo_cats/Medbox_halos_%03d-%03d_a%.2f.txt"

outbase = "/nfs/slac/g/ki/ki22/cosmo/tmcclint/Medbox_halos/mass_functions/"
ob = outbase+"Medbox_mf_%03d-%03d_Z%d.txt"
oc = outbase+"Medbox_mf_%03d-%03d_Z%d_cov.txt"

sfs = np.array([0.25,0.33,0.50,0.54,0.59,0.65,0.71,0.80,0.91,1.00])

def run(box, real, snap):
    
    try:
        sf = sfs[snap]
        indata = pd.read_csv(inbase%(box, real, sf), dtype='float64', header=0, delim_whitespace=True)
        data = indata.as_matrix()
        data = np.copy(data, order='C')
        M = data[:,3]
        x, y, z = data[:, :3].T
        Nps = data[:,4] #Number of particles
    except ValueError:
        print "Exiting with value error."
        return
    os.system("mkdir -p %s"%(outbase))

    SIDE_LENGTH = 6000. #Mpc/h side of the whole simulation

    lM = np.log10(M)
    lMmax = 16.
    print "log bin edges:",np.min(lM), lMmax
    Nbins = 20
    edgesall = np.linspace(np.min(lM)-0.0001, lMmax, Nbins+1)
    edges = edgesall[1:]
    #edges = np.linspace(np.min(lM)-0.0001, lMmax, Nbins+1)[1:] #only right edges
    lMi = np.digitize(lM, edges, True)
    N = np.bincount(lMi, minlength=Nbins)
    Mave = np.zeros_like(N)
    Npave = np.zeros_like(N)
    correction = np.zeros_like(N, dtype='float64')
    for i in range(len(Mave)):
        inds = (lMi==i)
        Mi = M[inds]
        print len(Mi), N[i]
        Mhere = Mi/N[i]
        Mave[i] = np.sum(Mhere)
        Nphere = Nps[inds]/N[i]
        Npave[i] = np.sum(Nphere)
        if Npave[i] > 0:
            #correction[i] = -np.exp(-(np.log10(Npave[i])+0.175)/0.704)
            #print "Npave[%d]"%i,Npave[i], correction[i]
            correction[i] = -np.exp(-(np.log10(Npave[i])-0.25401982)/0.55696121)
            #print "Npave[%d]"%i,Npave[i], correction[i]
        else:
            correction[i] = 0

    print "N truth:", N
    print "total number ", N.sum()
    print "total input ", M.size

    Ndivs = 8
    Njk = Ndivs*Ndivs*Ndivs
    print "N per jk:",N/float(Njk)
    Vfactor = Njk/(Njk-1.) #gotta increase everything by this when we do the LOO
    L = SIDE_LENGTH/Ndivs #Mpc/h per side of jk subregion
    jk = np.floor(x/L) + Ndivs*np.floor(y/L) + Ndivs*Ndivs*np.floor(z/L)
    jk = jk.astype(int)
    Nsub = np.ones((Njk, Nbins))
    #print "Jk facts: ",Njk, min(jk), max(jk)

    #Find the number in each subregion
    for i in range(Njk):
        lMjk = lM[jk==i] #the halos in the ith subregion
        lMj = np.digitize(lMjk, edges, True)
        Nsub[i] = np.bincount(lMj, minlength=len(N))#number in this subregion
        
    print "Resum from subs: ",np.sum(Nsub, axis=0).astype(int)
    Nloo = np.ones_like(Nsub)
    Nloo[:] *= N
    Nloo -= Nsub

    Nloo *= Vfactor #Rescale for the appropriate volume
    Nmean = np.mean(Nloo, axis=0)
    #print "Nmean - N: ",Nmean - N
    X = Nloo[:] - Nmean

    C = np.zeros((Nbins, Nbins))
    for i in range(Nbins):
        for j in range(Nbins):
            C[i,j] = np.sum(X[:,i]*X[:,j])

    err = np.sqrt(np.diag(C))

    edges = np.linspace(min(lM), max(lM), Nbins+1)
    lMbins = (edges[1:] + edges[:-1])/2.
    out = np.zeros((Nbins, 4 ))

    #APPLY THE CORRECTION
    N = N.astype('float64')
    for i in range(Nbins):
        N[i] = N[i]/(1+correction[i])
        for j in range(Nbins):
            C[i,j]  = C[i,j]/((1+correction[i])*(1+correction[j]))

    for i in range(Nbins):
        out[i, 0] = edgesall[i]
        out[i, 1] = edgesall[i+1]
        out[i, 2] = N[i]
        out[i, 3] = Mave[i]
    good = N > 0
    out = out[good]
    C = C[good]
    C = C[:,good]
    lMa = np.log10(Mave[good])
    print "Mean masses:",np.log10(Mave[good])
    print "Kept indices:",(lMa>out[:,0]), (lMa < out[:,1])

    oboxes = [0,2,4]#Mapping from box to outbox index to match testboxes
    obox = oboxes[box]
    np.savetxt(ob%(obox, real, snap), out, header = "logM_lo logM_hi N Mave")
    np.savetxt(oc%(obox, real, snap), C)
    print "DONE with box%d real%d snap%d"%(box, real, snap)

if __name__ == "__main__":
    for box in range(1,2):
        for real in range(0, 1):
            for snap in range(0,10):
                run(box, real, snap)
