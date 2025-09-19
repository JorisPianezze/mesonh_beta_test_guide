.. _nam_backup:

NAM_BACKUP
-----------------------------------------------------------------------------

.. csv-table:: NAM_BACKUP content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XBAK_TIME","REAL(:,:)","8*192*-999.0"
   "NBAK_STEP","INTEGER(:,:)","8*192* -999"
   "XBAK_TIME_FREQ","REAL(:)","-999.0"
   "XBAK_TIME_FREQ_FIRST","REAL(:)","-999.0"
   "NBAK_STEP_FREQ","INTEGER(:)","-999"
   "NBAK_STEP_FREQ_FIRST","INTEGER(:)","-999"
   "LBAK_BEG","LOGICAL",".FALSE."
   "LBAK_END","LOGICAL",".FALSE."
   "LBAK_REDUCE_FLOAT_PRECISION","LOGICAL(:)",".FALSE."
   "LBAK_COMPRESS","LOGICAL(:)",".FALSE."
   "NBAK_COMPRESS_LEVEL","INTEGER(:)","4"
   "CBAK_DIR","CHARACTER(LEN=512)",""

* :code:`XBAK_TIME(m,i)` : array of increments in seconds from the beginning of the segment to the instant where the i-th backup is realized by the model m

* :code:`NBAK_STEP(m,i)` : array of increments in timesteps from the beginning of the segment to the instant where the i-th backup is realized by the model m

* :code:`XBAK_TIME_FREQ(m)` : time between 2 backups for each model m

* :code:`XBAK_TIME_FREQ_FIRST(m)` : time of the first backup for each model m (if XBAK_TIME_FREQ(m) is set). If not set, the first backup will be at time = XBAK_TIME_FREQ.

* :code:`NBAK_STEP_FREQ(m)` : number of timesteps between 2 backups for each model m

* :code:`NBAK_STEP_FREQ_FIRST(m)` : timestep number of the first backup for each model m (if NBAK_STEP_FREQ(m) is set). If not set, the first backup will be at time = NBAK_STEP_FREQ.

* :code:`LBAK_BEG` : force a backup at the first timestep

* :code:`LBAK_END` : force a backup at the last timestep

* :code:`LBAK_REDUCE_FLOAT_PRECISION(m)` : force writing of floating points numbers in single precision for each model m (only for files in netCDF format, not for LFI format). This option can not be enabled if LIO_ALLOW_REDUCED_PRECISION_BACKUP has not been forced to .TRUE. in :ref:`nam_confio`. Be careful, this loss of precision could impact restarted computations. This option should only be used if you understand the risks.

* :code:`LBAK_COMPRESS(m)` : enable lossless compression of data for each model m (only for files in netCDF format, not for LFI format). This can have a negative impact on performance. This option loses precedence over LIO_COMPRESS of :ref:`nam_confio`. 

* :code:`LBAK_COMPRESS_LEVEL(m)` : set the compression level for each model m (only for files in netCDF format, not for LFI format). The value must be in the 0 to 9 interval (0 for no compression, 9 for maximum compression). This option loses precedence over LIO_COMPRESS_LEVEL of :ref:`nam_confio` if  LIO_COMPRESS=.TRUE.

* :code:`CBAK_DIR` : directory used to write backups and diachronic files (current directory by default). It overrides CIO_DIR.

.. note::

   * A choosen time must be a multiple of the timestep.
   * Different ways to choose the backup times can be combined: a regular series (given with a frequency) + irregular times. Duplicate times will be automatically removed.
   * In grid-nesting, backup times are propagated from the parent model to its children (children are allowed to have other backup times). Children regular series must be aligned with parent ones. A regular parent backup must always be at the same time than a regular children backup. However, children may have more frequent regular backups (parent time frequency must be a multiple of children frequencies).
