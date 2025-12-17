.. _nam_flaken:

NAM_FLAKEn
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. csv-table:: NAM_FLAKEn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LSEDIMENTS", "LOGICAL", ".TRUE."
   "CSNOW_FLK", "CHARACTER(LEN=3)", "'DEF'"
   "CFLK_FLUX", "CHARACTER(LEN=3)", "'DEF'"
   "CFLK_ALB", "CHARACTER(LEN=4)", "'DEF'"
   "LSKINTEMP", "LOGICAL", ".FALSE."
   
* :code:`LSEDIMENTS` : to use the bottom sediments scheme of Flake (default)

* :code:`CSNOW_FLK` : snow scheme to be used. For the time being only option 'DEF' is active

* :code:`CFLK_FLUX` : scheme to be used to compute surface fluxes of moment, energy and water vapor:

  * 'DEF' : to activate the classic watflux 
  * 'FLAKE' : to use flake parameterization

* :code:`CFLK_ALB` : type of albedo for FLake.

  * 'UNIF' : a uniform value of 0.135 is used for water albedo
  * 'TA96' : :cite:t:`taylor_studies_1996` formula for water direct albedo, depending on solar zenith angle
  * 'MK10' : albedo from Marat Khairoutdinov

* :code:`LSKINTEMP` : flag to use or not the skin temperature computation.   
