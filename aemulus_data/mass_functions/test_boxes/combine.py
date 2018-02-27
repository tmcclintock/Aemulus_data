import numpy as np
import sys, os
import pandas as pd

inbase = "/nfs/slac/g/ki/ki22/cosmo/tmcclint/NEWTESTMF/TestBox%03d-%03d/"
outbase = "/nfs/slac/g/ki/ki22/cosmo/tmcclint/NEWTESTMF/combined/TestBox%03d/"
op = outbase+"TestBox%03d_Z%d.txt"
oc = outbase+"TestBox%03d_Z%d_cov.txt"

def combine(box, snap):
    os.system("mkdir -p %s"%(outbase%(box)))

    d1 = np.loadtxt(inbase%(box,0)+"/TestBox%03d-%03d_Z%d.txt"%(box,0, snap))
    c1 = np.loadtxt(inbase%(box,0)+"/TestBox%03d-%03d_Z%d_cov.txt"%(box,0, snap))

    lo, hi, N, Ma = d1.T
    L = len(lo)
    Ms = np.zeros((5, L))
    Ms[0] = Ma
    Ns = np.zeros((5, L))
    Ns[0] = N
    cs = np.zeros((5, L, L))
    cs[0] = c1
    for real in range(1, 5):
        dname = inbase%(box,real)+"/TestBox%03d-%03d_Z%d.txt"%(box,real, snap)
        cname = inbase%(box,real)+"/TestBox%03d-%03d_Z%d_cov.txt"%(box,real, snap)
        _,_,Ni,Mi = np.loadtxt(dname).T
        Ns[real] = Ni
        cs[real] = np.loadtxt(cname)
        Ms[real] = Mi
    Nfinal = np.mean(Ns, 0)
    cfinal = np.mean(cs, 0)/5.
    Mfinal = np.max(Ms,0)
    out = np.array([lo,hi,Nfinal,Mfinal]).T
    good = (Nfinal>0)
    out = out[good]
    cfinal = cfinal[good]
    cfinal = cfinal[:,good]
    np.savetxt(op%(box, box, snap), out, header = "logM_lo logM_hi N Mave")
    np.savetxt(oc%(box, box, snap), cfinal)
    print "Saved combined TextBox%03d snap%d"%(box, snap)
    return

if __name__=="__main__":
    for box in range(0,7):
        for snap in range(0, 10):
            combine(box, snap)
    
