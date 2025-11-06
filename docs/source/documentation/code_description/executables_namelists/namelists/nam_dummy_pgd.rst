.. _nam_dummy_pgd:

NAM_DUMMY_PGD
-----------------------------------------------------------------------------

This namelist allows to incorporate into the physiographic file any surface field. You can treat up to 999 such fields. These fields will be written on all the files you will use later(after prognostic fields initialization, or during and after run, etc...). Their name in the files are 'DUMMY_GRnnn', where nnn goes from 001 to 999. During the execution of the programs, these fields are stored in the XDUMMY_FIELDS(:,:) (first dimension: spatial dimension, second dimension: total number of fields), in the module MODD_DUMMY_SURF_FIELDn. You must modify the fortran source, where you want to use them.

.. csv-table:: NAM_DUMMY_PGD content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NDUMMY_NBR", "INTEGER", "0"
   "CDUMMY_NAME(:)", "CHARACTER(LEN=20)", ""
   "CDUMMY_FILE(:)", "CHARACTER(LEN=28)", ""
   "CDUMMY_FILETYPE(:)", "CHARACTER(LEN=6)", ""
   "CDUMMY_AREA(:)", "CHARACTER(LEN=3)", "'ALL'"
   "CDUMMY_ATYPE(:)", "CHARACTER(LEN=3)", "'ARI'"

Only the first NDUMMY_NBR values in these arrays are meaningfull.

* :code:`NDUMMY_NBR` : number of dummy fields.

* :code:`CDUMMY_NAME(:)` : list of the dummy fields you want to initialize with your own data. You can give any name you want. This is a way to describe what is the field. This information is not used by the program. It is just written in the Meso-NH files.

* :code:`CDUMMY_FILE(:)` : list of the names of the files containing the data for the fields you have specified in CDUMMY_NAME(:).

* :code:`CDUMMY_FILETYPE(:)` : list of the types of the files containing the data for the fields you have specified in CDUMMY_NAME(:) ('DIRECT', 'LATLON', 'BINLLF', 'BINLLV', 'ASCLLV').

* :code:`CDUMMY_AREA(:)` : area of meaningfullness of the fields you have specified in CDUMMY_NAME(:) ('ALL', 'NAT', 'TWN', 'SEA', 'WAT', 'LAN', respectively for everywhere, natural areas, town areas, sea, inland waters, land = natural cover + town). For example, oceanic emission of DNS is relevant on 'SEA'.

* :code:`CDUMMY_ATYPE(:)` : type of averaging (during PGD for the fields you have specified in CDUMMY_NAME(:) ('ARI', 'INV', 'LOG', respectively for arithmetic, inverse and logarithmic averaging).
