import os

inpath = "Box%03d/Box%03d_cov_Z%d.txt"
outpath = "Box%03d/Box%03d_Z%d_cov.txt"

for i in range(0, 40):
    for j in range(0, 10):
        inp = inpath%(i, i, j)
        outp = outpath%(i, i, j)
        os.system("mv %s %s"%(inp, outp))
