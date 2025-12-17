.. _nam_tebn:

NAM_TEBn
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. csv-table:: NAM_TEBn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CZ0H", "CHARACTER(LEN=6)", "'KAND07'"
   "CCH_BEM", "CHARACTER(LEN=5)", "'DOE-2'"
   "CURB_LM", "CHARACTER(LEN=4)", "'LMEZ'"
   "CZ0EFF_GD", "CHARACTER(LEN=4)", "'NONE'"
   
* :code:`CZ0H` : TEB option for z0h roof and road:

  * 'MASC95' : Mascart et al 1995
  * 'BRUT82' : Brustaert 1982
  * 'KAND07' : Kanda 2007

* :code:`CCH_BEM` : BEM option for roof / wall outside convective coefficient :

  * 'DOE-2' : DOE-2 model from EnergyPlus Engineering reference, p65

* :code:`CURB_LM` : option to compute urban mixing length

  * 'SM10' : Urban mixing lenght is calculated following Santiago and Martili (2010).
  * 'LMEZ' : Urban mixing lenght is equaal to height above ground. Default is LMEZ.

* :code:`CZ0EFF_GD` : TEB option for effective roughness length for low urban vegetation
  
  * 'LR21' : Lemonsu, Redon et al 2021
  * 'NONE' : only vegetation roughness length is used, not taking into account the environment   
