************************************************************
Aemulus Simulation Data
************************************************************

The Aemulus simulations are a suite of simulations used for cosmological inference. They form the building blocks of a set of predictors, cosmic emulators, used to model various cosmological observables.

The emulators are located in various repositories associated to this one and include:

 * Halo mass function :math:`\frac{{\rm d}n}{{\rm d}M}(M, z)`
 * Galaxy-galaxy correlation function at :math:`\xi_{gg}(r, z=0.57)`
 * Halo occupation distribution (HOD) and assembly bias models :math:`P(N|M,x)`
 * Matter power spectrum :math:`P(k)` (in development)
 * Matter-matter correlation functions :math:`\xi_{mm}` (in development)
 * Halo-matter correlation functions :math:`\xi_{hm}` (in development)
 * Scale dependent halo bias :math:`b(M,r)` (in development)

Here you will find details on how to use these various emulators and some of the theory behind them. In addition, this repository contains the data used to train the Gaussian Processes that make up the emulators as well as the routines used to create some of the figures used in our papers.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Simulations
==========================

We ran fourty simulations and an additional thirty five simulations for testing. In addition to the cosmological parameters we also provide certain observables from the simulations as well as directions on how to obtain full particle catalogs.

.. toctree::
   :maxdepth: 2
	      
   Cosmologies (nearly complete)<data_files/cosmologies>
   Particles and halos (in progress)<data_files/particles_and_halos>

Available Emulators
==========================

Full documentation for the Aemulus emulators  are found here. You can find links to those specific repositories within these pages.

.. toctree::
   :maxdepth: 2

   Halo Mass Function (in progress)<emulators/halo_mass_function>
   GG Correlation Function (in progress)<emulators/gg_correlation_function>
   HOD (in progress)<emulators/halo_occupation_distribution>


Data files
==========================

.. toctree::
   :maxdepth: 1

   Mass Functions (in progress)<data_files/mass_functions>
   HOD Configurations (in progress)<data_files/hod_configurations>

Citation Information
==========================

If you use any of these emulators in your work please cite DeRose et al. (in prep) which introduced the simulations and the associated paper for that emulator.

 * Mass funciton - McClintock et al. (in prep.)
 * Galaxy-galaxy correlation function at :math:`z=0.57` - Zhai et al. (in prep.)
 * HOD - McLaughlin et al. (in prep.)
