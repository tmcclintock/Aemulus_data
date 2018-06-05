import numpy as np
import sys, os
import pandas as pd

inbase = "./TestBox%03d-%03d/"
outbase = "./combined/TestBox%03d/"
op = outbase+"TestBox%03d_Z%d.txt"
oc = outbase+"TestBox%03d_Z%d_cov.txt"

def combine(box, snap):
    os.system("mkdir -p %s"%(outbase%(box)))

    d1 = np.loadtxt(inbase%(box,0)+"/TestBox%03d-%03d_Z%d.txt"%(box,0, snap))
    c1 = np.loadtxt(inbase%(box,0)+"/TestBox%03d-%03d_Z%d_cov.txt"%(box,0, snap))

    Nreal = 5
    lo, hi, N, Ma = d1.T
    L = len(lo)
    Ms = np.zeros((Nreal, L))
    Ms[0] = Ma
    Ns = np.zeros((Nreal, L))
    Ns[0] = N
    cs = np.zeros((Nreal, L, L))
    cs[0] = c1
    for real in range(1, Nreal):
        dname = inbase%(box,real)+"/TestBox%03d-%03d_Z%d.txt"%(box,real, snap)
        cname = inbase%(box,real)+"/TestBox%03d-%03d_Z%d_cov.txt"%(box,real, snap)
        _,_,Ni,Mi = np.loadtxt(dname).T
        Ns[real] = Ni
        cs[real] = np.loadtxt(cname)
        Ms[real] = Mi
    if box == 0 and snap == 0:
        Ms = np.delete(Ms, 2, 0)
        cs = np.delete(cs, 2, 0)
        Ns = np.delete(Ns, 2, 0)
    Nfinal = np.mean(Ns, 0)
    cfinal = np.mean(cs, 0)/float(Nreal)
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
    for box in range(0,1): #7
        for snap in range(0, 1): #10
            combine(box, snap)
    
