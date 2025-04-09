.. _nam_ch_emis_pgd:

NAM_CH_EMIS_PGD
-----------------------------------------------------------------------------

This namelist is used to initialize chemistry components emissions. You can treat up to 999 such fields. These fields will be written on all the files you will use later (after prognostic fields initialization, or during and after run, etc...). Their name in the files are 'EMIS_GRnnn', where nnn goes from 001 to 999. During the execution of the programs, these fields are stored in the XEMIS_GR_FIELDS(:,:) (first dimension: spatial dimension, second dimension: total number of fields), in the module MODD_EMIS_GR_FIELDn. The temporal evolution, the aggregation of prescribed emissions and the link with the corresponding chemical prognostic variables are handled by the subroutine :file:`CH_EMISSION_FLUXn.f90`.

.. csv-table:: NAM_CH_EMIS_PGD content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NEMIS_PGD_NBR", "INTEGER", "0"
   "CEMIS_PGD_NAME(:)", "CHARACTER(LEN=20)", ""
   "CEMIS_PGD_FILE(:)", "CHARACTER(LEN=28)", ""
   "CEMIS_PGD_COMMENT(:)", "CHARACTER(LEN=40)", ""
   "NEMIS_PGD_TIME", "INTEGER", "0"
   "CEMIS_PGD_FILETYPE(:)", "CHARACTER(LEN=6)", "DIRECT"
   "CEMIS_PGD_AREA(:)", "CHARACTER(LEN=3)", "ALL"
   "CEMIS_PGD_ATYPE(:)", "CHARACTER(LEN=3)", "ARI"


Only the first NEMIS_PGD_NBR values in these arrays are meaningfull.

* :code:`NEMIS_PGD_NBR` : number of dummy fields.

* :code:`CEMIS_PGD_NAME(:)` : list of the dummy fields you want to initialize with your own data. You can give any name you want. This is a way to describe what is the field. This information is not used by the program. It is just written in the FM files.

* :code:`CEMIS_PGD_FILE(:)` : list of the names of the files containing the data for the fields you have specified in CEMIS_PGD_NAME(:).

* :code:`CEMIS_PGD_COMMENT(:)` : list of the comments associated to each emission field.

* :code:`NEMIS_PGD_TIME(:)` : list of the time of the files containing the data for the fields you have specified in CEMIS_PGD_NAME(:).

* :code:`CEMIS_PGD_FILETYPE(:)` : list of the types of the files containing the data for the fields you have specified in CEMIS_PGD_NAME(:) ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV').

* :code:`CEMIS_PGD_AREA(:)` : area of meaningfullness of the fields you have specified in CEMIS_PGD_NAME(:) ('ALL', 'NAT', 'TWN', 'SEA', 'WAT', 'LAN', respectively for everywhere, natural areas, town areas, sea, inland waters, land = natural cover + town). For example, oceanic emission of DNS is relevant on 'SEA'.

* :code:`CEMIS_PGD_ATYPE(:)` : type of averaging (during PGD for the fields you have specified in CEMIS_PGD_NAME(:) ('ARI', 'INV', 'LOG', respectively for arithmetic, inverse and logarithmic averaging).

.. note::

   Example:
   
   .. code-block:: fortran

      &NAM_CH_EMIS_PGD
         NEMIS_PGD_NBR = 2,
         CEMIS_PGD_NAME(1)='COE',
         NEMIS_PGD_TIME(1)=0,
         CEMIS_PGD_COMMENT(1)='CO_00h00',
         CEMIS_PGD_AREA(1)='LAN',
         CEMIS_PGD_ATYPE(1)='ARI',
         CEMIS_PGD_FILE(1)='co_00.asc',
         CEMIS_PGD_FILETYPE(1)='ASCLLV',
         CEMIS_PGD_NAME(2)='COE',
         NEMIS_PGD_TIME(2)=43200,
         CEMIS_PGD_COMMENT(2)='CO_12h00',
         CEMIS_PGD_AREA(2)='LAN',
         CEMIS_PGD_ATYPE(2)='ARI',
         CEMIS_PGD_FILE(2)='co_12.asc',
         CEMIS_PGD_FILETYPE(2)='ASCLLV',
         CEMIS_PGD_NAME(3)='DMSE',
         NEMIS_PGD_TIME(3)=0,
         CEMIS_PGD_COMMENT(3)='dms_cte',
         CEMIS_PGD_AREA(3)='SEA',
         CEMIS_PGD_ATYPE(3)='ARI',
         CEMIS_PGD_FILE(3)='dms.asc',
         CEMIS_PGD_FILETYPE(3)='ASCLLV'
      /
