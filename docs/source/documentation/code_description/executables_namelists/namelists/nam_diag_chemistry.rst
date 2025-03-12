.. _nam_diag_chemistry:

NAM_DIAG - Chemistry
-----------------------------------------------------------------------------

Only available if LUSECHEM=T in YINIFILE.des

* add :code:`LCHEMDIAG=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "O3...", ""Chemical scalar variables as defined in BASIC.f90 (ppb)", "3D"

.. note::

   Following options can be used in NAM_DIAG when LCHEMDIAG is activated :

   .. csv-table::
      :header: "Fortran name", "Fortran type", "Default value"
      :widths: 30, 30, 30
      
      "XCHEMLAT", "REAL", "XUNDEF"
      "XCHEMLON", "REAL", "XUNDEF"
      "CSPEC_DIAG", "character(*1024)", ""
      "CSPEC_BU_DIAG", "character(*1024)", ""
      
  * write chemicals species on vertical profile defined by (XCHEMLAT,XCHEMLON)
  
  * CSPEC_DIAG :list of the chemical species for production/loss terms computation. Each species is separated by a comma. Ex : CSPEC_DIAG=’O3,CO,BIO’
  
  * CSPEC_BU_DIAG :list of the chemical species for production/loss terms computation in all the reactions where the species is involved. Each species is separated by a comma. Ex : CSPEC_BU_DIAG=’O3,CO,BIO’


