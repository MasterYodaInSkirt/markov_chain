import matplotlib
from functools import partial
from matplotlib import pylab
from mcmc import *

# # MCMC and Gibbs Sampling, by Walsh, 2004, p.8
# # proposal dist. is uniform (symmetric) -> metropolis
# f = partial(inv_chi_sq, n = 5, a = 4)
f = partial(inv_chi_sq, n = 5, a = 4)
prop = partial(uni_prop, frm=0, to = 100)
smpls = run_chain(metropolis, f, prop, 1, 500)
pylab.plot(smpls[0])

# # MCMC and Gibbs Sampling, Walsh, p. 9
# f = partial(inv_chi_sq, n = 5, a = 4)
# prop = partial(chi_sq, n=1))
# smpls = run_chain(metropolis, f, prop, 1, 500)
# pylab.plot(smpls[0])
