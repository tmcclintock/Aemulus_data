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

.. _raw-simulation-data:

.. toctree::
   :maxdepth: 2
   :caption: Raw Simulation Data
	      
   Cosmologies<source/cosmologies>
   Particles and halos (in progress)<source/particles_and_halos>

.. _available-emulators:

.. toctree::
   :maxdepth: 2
   :caption: Available Emulators

   Halo Mass Function (in progress)<emulators/halo_mass_function>
   GG Correlation Function (in progress)<emulators/gg_correlation_function>
   HOD (in progress)<emulators/halo_occupation_distribution>

.. _data-files:
   
.. toctree::
   :maxdepth: 1
   :caption: Data Files
	      
   Mass Functions (in progress)<source/mass_functions>
   HOD Configurations (in progress)<source/hod_configurations>

.. _reference-api:

.. toctree::
   :maxdepth: 1
   :caption: Reference/API

   Aemulus_data Reference/API<api/modules>

Citation Information
==========================

If you use any of these emulators in your work please cite DeRose et al. (in prep) which introduced the simulations and the associated paper for that emulator.

 * Mass function - McClintock et al. (in prep.)
 * Galaxy-galaxy correlation function at :math:`z=0.57` - Zhai et al. (in prep.)
 * HOD - McLaughlin et al. (in prep.)
