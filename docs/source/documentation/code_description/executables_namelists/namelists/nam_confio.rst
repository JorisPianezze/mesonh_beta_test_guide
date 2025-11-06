.. _nam_confio:

NAM_CONFIO
-----------------------------------------------------------------------------

.. csv-table:: NAM_CONFIO content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CIO_DIR", "CHARACTER(LEN=512)", ""
   "LVERB_OUTLST", "LOGICAL", ".TRUE."
   "LVERB_STDOUT", "LOGICAL", ".FALSE."
   "LVERB_ALLPRC", "LOGICAL", ".FALSE."
   "NGEN_VERB", "INTEGER", "4"
   "NGEN_ABORT_LEVEL", "INTEGER", "2"
   "NBUD_VERB", "INTEGER", "4"
   "NBUD_ABORT_LEVEL", "INTEGER", "2"
   "NIO_VERB", "INTEGER", "4"
   "NIO_ABORT_LEVEL", "INTEGER", "2"
   "LIO_COMPRESS", "LOGICAL", ".FALSE."
   "NIO_COMPRESS_LEVEL", "INTEGER", "4"
   "LDIAG_REDUCE_FLOAT_PRECISION", "LOGICAL", ".FALSE."
   "LIO_ALLOW_REDUCED_PRECISION_BACKUP", "LOGICAL", ".FALSE."
   "LIO_ALLOW_NO_BACKUP", "LOGICAL", ".FALSE."
   "LIO_NO_WRITE", "LOGICAL", ".FALSE."
   "NFILE_NUM_MAX", "INTEGER", "999"
   
   
.. warning::
   * If a file is not found in the netCDF fileformat, Meso-NH will check if it exists in the LFI format and use it if found. This could be useful if you need to mix the reading of different files with different fileformats.

* :code:`CIO_DIR` : directory used to write outputs, backups and diachronic files (current directory by default). It can be overridden by CBAK_DIR for backups and diachronic files and by COUT_DIR for outputs.

* :code:`LVERB_OUTLST` : flag to write application messages in :file:`OUTPUT_LISTINGn` files (in current directory, n is for the current model)

* :code:`LVERB_STDOUT` : flag to write application messages on the standard output

* :code:`NGEN_VERB` : set the verbosity level for generic messages

  * 0 : no messages
  * 1 : fatal messages
  * 2 : error messages (and lower values)
  * 3 : warning messages (and lower values)
  * 4 : info messages (and lower values)
  * 5 : debug messages (and lower values)
  
* :code:`NGEN_ABORT_LEVEL` : set the minimum level of generic message to abort the application (same levels as for NGEN_VERB)

* :code:`NBUD_VERB` : set the verbosity level for budget messages (same levels as for NGEN_VERB)

* :code:`NBUD_ABORT_LEVEL` : set the minimum level of budget message to abort the application (same levels as for NGEN_VERB)

* :code:`NIO_VERB` : set the verbosity level for IO messages (same levels as for NGEN_VERB)

* :code:`NIO_ABORT_LEVEL` : set the minimum level of IO message to abort the application (same levels as for NGEN_VERB)

.. warning::

   Not all messages use this infrastructure. Therefore, some of them are not affected by these options.

* :code:`LIO_COMPRESS` : enable lossless compression of data for all files. This can have a negative impact on performance. This option takes precedence over their equivalent NAM_BACKUP and NAM_OUTPUT namelists.

* :code:`LOUT_COMPRESS_LEVEL` : set the compression level. The value must be in the 0 to 9 interval (0 for no compression, 9 for maximum compression). This option takes precedence over their equivalent in NAM_BACKUP and NAM_OUTPUT namelists (only if LIO_COMPRESS=.TRUE.).

* :code:`LDIAG_REDUCE_FLOAT_PRECISION` : force writing of floating points numbers in single precision for diagnostic files (written by the :program:`DIAG` program)

* :code:`LIO_ALLOW_REDUCED_PRECISION_BACKUP` : flag to allow writing of backup files with a reduced precision as well as reading of reduced precision files and files written with Meso-NH compiled with a lower precision for integers or reals (ie MNH_INT=4 and MNH_REAL=4).

* :code:`LIO_ALLOW_NO_BACKUP` : allow to have no valid backup time (useful for some tests)

* :code:`LIO_NO_WRITE` : disable file writes (useful for benchs)

* :code:`NFILE_NUM_MAX` : maximum number for numbered files (mainly backup and output files). If less than 1000, the numbers will be on 3 digits. From 1000, they will be on the number of digits of NFILE_NUM_MAX (5 if NFILE_NUM_MAX=12345).
