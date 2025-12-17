.. _nam_lunit2_spa:

NAM_LUNIT2_SPA
-----------------------------------------------------------------------------

.. csv-table:: NAM_LUNIT2_SPA content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CINIFILE","CHARACTER(LEN=128)","'INIFILE'"
   "CINIFILEPGD","CHARACTER(LEN=128)",""
   "YDOMAIN","CHARACTER(LEN=128)",""
   "YSPAFILE","CHARACTER(LEN=128)",""
   "YSPANBR","CHARACTER(LEN=2)","'00'"
   "YDADINIFILE","CHARACTER(LEN=128)",""
   "YDADSPAFILE","CHARACTER(LEN=128)",""
   "YSONFILE","CHARACTER(LEN=128)",""


* :code:`CINIFILE` : name of the initial Meso-NH file of model 1 (parent domain) which will be used to spawn model 2.

* :code:`CINIFILEPGD` : name of the PGD associated to the initial Meso-NH file 1 CINIFILE (father domain).

* :code:`YDOMAIN` : name of the file which defines the domain for model 2. If a domain file is provided for YDOMAIN, then all the information of namelist NAM\_GRID2\_SPA will be ignored. 

* :code:`YSPAFILE` : optional name of the spawned Meso-NH file 2 (output file). If the user does not specify this name, or if YSPAFILE = CINIFILE, the code builds the spawned Meso-NH file name as:

  * YSPAFILE = CINIFILE.spaYSPANBR
  * YSPAFILE = CINIFILE.sprYSPANBR if YSONFILE is provided.
  
* :code:`YSPANBR` : NumBeR which will be added to CINIFILE to generate the Meso-NH file name of the SPAwned file (string of 2 characters)

* :code:`YDADINIFILE` : if GBAL_ONLY=.TRUE. : name of the CINIFILE dad.

* :code:`YDADSPAFILE` : if GBAL_ONLY=.TRUE. : name of the YSPAFILE dad. 

.. note::

   Program will check that YDADINIFILE and YDADSPAFILE have the same characteristics, before replacing the dad name of YSPAFILE by YDADSPAFILE instead of YDADINIFILE. YDADSPAFILE must exist before running the spawning job. 

* :code:`YSONFILE` : optional name of a spawned Meso-NH file (input file). It must have the same resolution as the spawned Meso-NH file 2 (output file). The fields of YSONFILE will be used at points included in the domain defined by YDOMAIN or NAM_GRID2_SPA, instead of interpolated fields  of CINIFILE. This allows to keep finest information when defining a new finest domain to follow atmospheric system.
