.. _nam_ch_controln:

NAM_CH_CONTROLn
----------------------------------------------------------------------------- 

Chemical settings control.

.. csv-table:: NAM_CH_CONTROLn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CCHEM_SURF_FILE", "CHARACTER(LEN=28)", ""

* CCHEM_SURF_FILE: name of general chemical ASCII input file. Whatever the choice for the type of calculation of the emissions (either by mapping of emissions at different times CCH_EMIS='AGGR' or computation by SNAPs, CCH_EMIS='SNAP'), the user needs to define :

  * how to do the translation: from the emitted chemical species that are in the inventory to the chemical species that are emitted to the atmospheric chemical scheme (that of course are usually not the same)
  * the information for the deposition scheme basic information on the chemical species (example: molar mass)

This translation is done in an ASCII file that contains a lot of information on the chemical schemes. This file should be done by an expert in air chemistry, that also has knowledge on the inventories. Here is an example of this file, for only two chemical species (CO2 and CO) :

.. code-block::

   ================================================================
   *** the following section will be used by ch_init_emissionn.f90 ***
   ================================================================
   EMISDATA
   emission fluxes (in nMole/m2/day) from SHIP data DMS(flux) = 1.7 nmol/m2/d
   MOL
   1 species
   1 records
   DMS
   (F10.0,/,99(5E10.2))
   0.
   1.7
   ================================================================
   *** the following section will be used by ch_init_emissionn.F90 and ch_init_snapn.F90 ***
   ================================================================
   EMISUNIT
   Emission Stut. Univ. EUROPE 10KM
   MIX
   AGREGATION
   Schema reduit ReLACS
   CO2 1.0 CO2
   END_AGREGATION
   =====================================================================
   *** the following section will be read by ch_init_dep_isban.F90 ***
   =====================================================================
   SURF_RES
   surface resistances (s/m), refer to Seinfeld and Pandis, 1998, p. 975, Tab.19.2
   1
   (1X,A12,1X,F7.1)
   'NONE' 2500.1
   =====================================================================
   *** the following section will be read by ch_init_depconst.F90 ***
   =====================================================================
   MASS_MOL
   molecular mass (in g/mol) for molecular diffusion, from Stockwell et al., 1997
   2
   (1X,A12,1X,F11.3)
   'CO2' 44.000
   'CO' 28.000
   REA_FACT
   reactivity factor with biology, Seinfeld and Pandis, 1998, p. 975, Tab. 19.3
   2
   (1X,A12,1X,F4.1)
   'CO2' 0.0
   'CO' 0.0
   HENRY_SP
   Henry specific constant, CO2 according to Seinfeld p347
   2
   (1X,A12,1X,E18.2,1X,F8.0)
   'CO2' 3.40E-2 0.
   'CO' 9.50E-4 -1300.
