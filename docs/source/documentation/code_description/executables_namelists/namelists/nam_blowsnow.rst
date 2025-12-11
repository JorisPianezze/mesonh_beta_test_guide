.. _nam_blowsnow:

NAM_BLOWSNOW
-----------------------------------------------------------------------------

.. csv-table:: NAM_BLOWSNOW content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LBLOWSNOW","LOGICAL",".FALSE."
   "NBLOWSNOW3D","INTEGER","2"
   "NBLOWSNOW_2D","INTEGER","3"
   "XALPHA_SNOW","REAL","3"
   "XRSNOW","REAL","4"


* :code:`LBLOWSNOW` : Flag to active pronostic blowing snow 

* :code:`NBLOWSNOW3D` : Number of blowing snow variables as scalar in Meso-NH. The curent version of the model use two scalars: number concentration and mass concentration (kg/kg)

* :code:`NBLOWSNOW_2D` :  Number of 2D blowing snow variables advected in Meso-NH. The curent version of the model advectes three variables: total number concentration in canopy, total mass concentration in canopy and equivalent concentration in the saltation layer

* :code:`XALPHA_SNOW` : Gamma distribution shape factor

* :code:`XRSNOW` : Ratio between diffusion coefficient for scalar variables and blowing snow variables

  * XRSNOW = KSCA/KSNOW = 4. (if :cite:t:`redelsperger_methode_1981` used in :file:`ini_cturb.f90`)
  * XRSNOW = KSCA/KSNOW = 2.5 ( if :cite:t:`cheng_improved_2002` used in :file:`ini_cturb.f90`)
