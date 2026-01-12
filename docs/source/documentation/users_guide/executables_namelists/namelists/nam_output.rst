.. _nam_output:

NAM_OUTPUT
-----------------------------------------------------------------------------

This namelist allows to write selected fields in output files.

.. csv-table:: NAM_OUTPUT content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "COUT_VAR","CHARACTER(LEN=32)(:,:,:)","''"
   "XOUT_TIME","REAL(:,:,:)",|XNEGUNDEF|
   "NOUT_STEP","INTEGER(:,:,:)",|NNEGUNDEF|
   "XOUT_TIME_FREQ","REAL(:,:)",|XNEGUNDEF|
   "XOUT_TIME_FREQ_FIRST","REAL(:,:)","XOUT_TIME_FREQ"
   "NOUT_STEP_FREQ","INTEGER(:,:)",|NNEGUNDEF|
   "NOUT_STEP_FREQ_FIRST","INTEGER(:,:)","XOUT_TIME_FREQ"
   "LOUT_BEG","LOGICAL(:)",".FALSE."
   "LOUT_END","LOGICAL(:)",".FALSE."
   "LOUT_REDUCE_FLOAT_PRECISION","LOGICAL(:,:)",".FALSE."
   "LOUT_COMPRESS","LOGICAL(:,:)",".FALSE."
   "NOUT_COMPRESS_LEVEL","INTEGER(:,:)","4"
   "LOUT_COMPRESS_LOSSY","LOGICAL(:,:)",".FALSE."
   "COUT_COMPRESS_LOSSY_ALGO","CHARACTER(LEN=10)(:,:)","'GRANULARBR'"
   "NOUT_COMPRESS_LOSSY_NSD","INTEGER(:,:)","3"
   "NOUT_VAR_REDUCE_FLOAT_PRECISION","INTEGER(:,:,:)",|NCOMPRPARAMNOTSET|
   "NOUT_VAR_COMPRESS_LEVEL","INTEGER(:,:,:)",|NCOMPRPARAMNOTSET|
   "COUT_VAR_COMPRESS_LOSSY_ALGO","CHARACTER(LEN=10)(:,:,:)","'NOT_SET'"
   "NOUT_VAR_COMPRESS_LOSSY_NSD","INTEGER(:,:,:)",|NCOMPRPARAMNOTSET|
   "XOUT_VAR_THR_MIN","REAL(:,:,:)","not set"
   "XOUT_VAR_THR_MAX","REAL(:,:,:)","not set"
   "XOUT_VAR_THR_ABSMIN","REAL(:,:,:)","not set"
   "XOUT_VAR_THR_ABSMAX","REAL(:,:,:)","not set"
   "COUT_VAR_THR_MIN_BEHAVIOR","CHARACTER(LEN=9)(:,:,:)","'NOT_SET'"
   "COUT_VAR_THR_MAX_BEHAVIOR","CHARACTER(LEN=9)(:,:,:)","'NOT_SET'"
   "COUT_VAR_THR_ABSMIN_BEHAVIOR","CHARACTER(LEN=9)(:,:,:)","'NOT_SET'"
   "COUT_VAR_THR_ABSMAX_BEHAVIOR","CHARACTER(LEN=9)(:,:,:)","'NOT_SET'"
   "XOUT_VAR_RND_FACTOR","REAL(:,:,:)",|XNEGUNDEF|
   "COUT_DIR","CHARACTER(LEN=512)","''"
   "LOUT_FILESPLIT_DISABLE","LOGICAL(:,:)",".FALSE."
   "LOUT_BOTTOM_ABSORBING_LAYER_REMOVE","LOGICAL(:,:)",".TRUE."
   "LOUT_TOP_ABSORBING_LAYER_REMOVE","LOGICAL(:,:)",".TRUE."
   "LOUT_UNPHYSICAL_HOR_CELLS_REMOVE","LOGICAL(:,:)",".TRUE."
   "LOUT_UNPHYSICAL_VER_CELLS_REMOVE","LOGICAL(:,:)",".TRUE."
   "LOUT_PHYSICAL_SIMPLIFIED","LOGICAL(:,:)",".FALSE."
   "NOUT_BOXES","INTEGER(:,:)","0"
   "COUT_BOX_NAME","CHARACTER(LEN=32)(:,:,:)","'Box_nnnn'"
   "NOUT_BOX_IINF","INTEGER(:,:,:)",|XNEGUNDEF|
   "NOUT_BOX_ISUP","INTEGER(:,:,:)",|XNEGUNDEF|
   "NOUT_BOX_JINF","INTEGER(:,:,:)",|XNEGUNDEF|
   "NOUT_BOX_JSUP","INTEGER(:,:,:)",|XNEGUNDEF|
   "NOUT_BOX_KINF","INTEGER(:,:,:)",|XNEGUNDEF|
   "NOUT_BOX_KSUP","INTEGER(:,:,:)",|XNEGUNDEF|
   "COUT_BOX_VAR_SUPP","CHARACTER(LEN=32)(:,:,:,:)","''"
   "LOUT_MAINDOMAIN_WRITE","LOGICAL(:,:)",".FALSE."
   "NOUT_BOX_VAR_REDUCE_FLOAT_PRECISION","INTEGER(:,:,:,:)",|NCOMPRPARAMNOTSET|
   "NOUT_BOX_VAR_COMPRESS_LEVEL","INTEGER(:,:,:,:)",|NCOMPRPARAMNOTSET|
   "COUT_BOX_VAR_COMPRESS_LOSSY_ALGO","CHARACTER(LEN=10)(:,:,:,:)","'NOT_SET'"
   "NOUT_BOX_VAR_COMPRESS_LOSSY_NSD","INTEGER(:,:,:,:)",|NCOMPRPARAMNOTSET|
   "XOUT_BOX_VAR_THR_MIN","REAL(:,:,:,:)","not set"
   "XOUT_BOX_VAR_THR_MAX","REAL(:,:,:,:)","not set"
   "XOUT_BOX_VAR_THR_ABSMIN","REAL(:,:,:,:)","not set"
   "XOUT_BOX_VAR_THR_ABSMAX","REAL(:,:,:,:)","not set"
   "COUT_BOX_VAR_THR_MIN_BEHAVIOR","CHARACTER(LEN=9)(:,:,:,:)","'NOT_SET'"
   "COUT_BOX_VAR_THR_MAX_BEHAVIOR","CHARACTER(LEN=9)(:,:,:,:)","'NOT_SET'"
   "COUT_BOX_VAR_THR_ABSMIN_BEHAVIOR","CHARACTER(LEN=9)(:,:,:,:)","'NOT_SET'"
   "COUT_BOX_VAR_THR_ABSMAX_BEHAVIOR","CHARACTER(LEN=9)(:,:,:,:)","'NOT_SET'"
   "XOUT_BOX_VAR_RND_FACTOR","REAL(:,:,:,:)",|XNEGUNDEF|

.. note::

   Most of the parameters of this namelist have several dimensions. The first one is for the series number (noted s in the description below).
   It allows to define several output series with different times and variables. This dimension has been introduced in the 6.0.0 version of MesoNH and
   is always of size 1 for the moment (the possibility to have several series is not yet available).
   The second dimension is for the model number (noted m in the description below, of size 1 if the simulation is not using grid-nesting).
   The other dimensions depends on the parameter (b for boxes, f for fields, i for irregular times)


* :code:`COUT_VAR(s,m,f)`: list of the field names to output for each model m (all listed in :file:`mode_field.f90`). If boxes/subdomains are selected (NOUT_BOXES > 0), these fields will also be written in all the boxes (use COUT_BOX_VAR_SUPP to be more specific)

* :code:`XOUT_TIME(s,m,i)`: array of increments in seconds from the beginning of the segment to the instant where the i-th output is REALized by the model m

* :code:`NOUT_STEP(s,m,i)`: array of increments in timesteps from the beginning of the segment to the instant where the i-th output is REALized by the model m

* :code:`XOUT_TIME_FREQ(s,m)`: time between 2 outputs for each model m

* :code:`XOUT_TIME_FREQ_FIRST(s,m)`: time of the first output for each model m (if XOUT_TIME_FREQ(m) is set). If not set, the first output will be at time = XOUT_TIME_FREQ.

* :code:`NOUT_STEP_FREQ(s,m)`: number of timesteps between 2 outputs for each model m

* :code:`NOUT_TIME_FREQ_FIRST(s,m)`: timestep number of the first output for each model m (if NOUT_STEP_FREQ(m) is set). If not set, the first output will be at time = NOUT_STEP_FREQ.

* :code:`LOUT_BEG(s)`: force an output at the first timestep

* :code:`LOUT_END(s)`: force an output at the last timestep

* :code:`LOUT_REDUCE_FLOAT_PRECISION(s,m)`: force writing of floating points numbers in single precision for each model m

* :code:`LOUT_COMPRESS(s,m)`: enable lossless compression of data for each model mThis can have a negative impact on performance. This option loses precedence over LIO_COMPRESS of :ref:`nam_confio`.

* :code:`LOUT_COMPRESS_LEVEL(s,m)`: set the compression level for each model m. The value must be in the 0 to 9 interval (0 for no compression, 9 for maximum compression). This option loses precedence over LIO_COMPRESS_LEVEL of :ref:`nam_confio` if  LIO_COMPRESS=.TRUE.

* :code:`LOUT_COMPRESS_LOSSY(s,m)`: enable lossy compression of data for each model m

* :code:`COUT_COMPRESS_LOSSY_ALGO(s,m)`: algorithm used to reduce the number of significants digits or bits. Available algorithms: 'BitGroom', 'GranularBR', 'BitRound' and 'None' (case insensitive). Default: 'GranularBR'

* :code:`NOUT_COMPRESS_LOSSY_NSD(s,m)`: number of significants digits (for 'BitGroom', 'GranularBR') or bits (for 'BitRound') to keep. Allowed values for 'BitGroom', 'GranularBR': 1 to 15 for floats stored with 64 bits and 1 to 7 on 32 bits. And for 'BitRound', 1 to 23 for 32-bit floats and 1 to 52 for 64-bit floats. Default value: 3

* :code:`NOUT_VAR_REDUCE_FLOAT_PRECISION(s,m,f)`: force writing of floating points numbers in single precision for the selected variables. If set to 0, no reduction of precision will be done. If set to 1 (or > 0), reduction of precision will be done. By default, the value for the file (LOUT_REDUCE_FLOAT_PRECISION) is taken into account.

* :code:`NOUT_VAR_COMPRESS_LEVEL(s,m,f)`: set the compression level per variable. The value must be in the 0 to 9 interval (0 for no compression, 9 for maximum compression). By default, the value for the file (LOUT_COMPRESS and LOUT_COMPRESS_LEVEL) is taken into account.

* :code:`COUT_VAR_COMPRESS_LOSSY_ALGO(s,m,f)`: algorithm used to reduce the number of significants digits or bits per variable. Set to 'NONE' to disable lossy compression. By default, the value for the file (LOUT_COMPRESS_LOSSY and LOUT_COMPRESS_LOSSY_ALGO) is taken into account.

* :code:`NOUT_VAR_COMPRESS_LOSSY_NSD(s,m,f)`: number of significants digits (for 'BitGroom', 'GranularBR') or bits (for 'BitRound') to keep per variable. By default, the value for the file (LOUT_COMPRESS_LOSSY_ALGO_NSD) is taken into account.

* :code:`XOUT_VAR_THR_MIN(s,m,f)`: minimum threshold per variable. If a value of the variable is strictly below this threshold, it is set to the one chosen with the COUT_VAR_THR_MIN_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`XOUT_VAR_THR_MAX(s,m,f)`: maximum threshold per variable. If a value of the variable is strictly above this threshold, it is set to the one chosen with the COUT_VAR_THR_MAX_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`XOUT_VAR_THR_ABSMIN(s,m,f)`: absolute minimum threshold per variable. If an absolute value of the variable is strictly below this threshold, it is set to the one chosen with the COUT_VAR_THR_ABSMIN_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`XOUT_VAR_THR_ABSMAX(s,m,f)`: absolute maximum threshold per variable. If an absolute value of the variable is strictly above this threshold, it is set to the one chosen with the COUT_VAR_THR_ABSMAX_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`COUT_VAR_THR_MIN_BEHAVIOR(s,m,f)`: behavior to apply when a value is below the minimum threshold. Allowed values (described later in this section): 'ZERO', 'MIN' (default if threshold is not negative), 'FILLVALUE' (default if threshold is negative), 'VALIDMIN', 'UNDEF', 'NEGUNDEF', 'EXCLRANGE' and 'NONE' (default if no threshold is set).

* :code:`COUT_VAR_THR_MAX_BEHAVIOR(s,m,f)`: behavior to apply when a value is above the maximum threshold. Allowed values (described later in this section): 'ZERO', 'MAX', 'FILLVALUE' (default if threshold is set), 'VALIDMAX', 'UNDEF', 'NEGUNDEF', 'EXCLRANGE' and 'NONE' (default if no threshold is set).

* :code:`COUT_VAR_THR_ABSMIN_BEHAVIOR(s,m,f)`: behavior to apply when an absolute value is below the absolute minimum threshold. Allowed values (described later in this section): 'ZERO' (default if threshold is set), 'ABSMIN', 'FILLVALUE', 'UNDEF', 'NEGUNDEF' and 'NONE' (default if no threshold is set).

* :code:`COUT_VAR_THR_ABSMAX_BEHAVIOR(s,m,f)`: behavior to apply when an absolute value is above the absolute maximum threshold. Allowed values (described later in this section): 'ABSMAX', 'FILLVALUE' (default if threshold is set), 'UNDEF', 'NEGUNDEF', 'ZERO' and 'NONE' (default if no threshold is set).

* :code:`XOUT_VAR_RND_FACTOR(s,m,f)`: rounding factor per variable. This factor is applied to the variable values. Each value is rounded to a multiple of it. It has to be positive. This allows to significantly reduce the size of the output files if compression is enabled with a loss of precision. This approach is complementary to the lossy compression which manage the number of significant digits or bits.

* :code:`COUT_DIR`: directory used to write outputs and diachronic files (current directory by default). It overrides CIO_DIR in :ref:`nam_confio`.

* :code:`LOUT_FILESPLIT_DISABLE(s,m)`: disable splitting of files in vertical levels (in the case it was enabled with NB_PROCIO_W > 1 in :ref:`nam_confz`. Default: .FALSE.

* :code:`LOUT_BOTTOM_ABSORBING_LAYER_REMOVE(s,m)`: remove the grid layers corresponding to the bottom absorbing layer (if they exist) for each model m. Default: .TRUE.

* :code:`LOUT_TOP_ABSORBING_LAYER_REMOVE(s,m)`: remove the grid layers corresponding to the top absorbing layer (if they exist) for each model m. Default: .TRUE.

* :code:`LOUT_UNPHYSICAL_HOR_CELLS_REMOVE(s,m)`: remove the non-physical horizontal grid cells on the borders of the domain for each model m. Default: .TRUE.

* :code:`LOUT_UNPHYSICAL_VER_CELLS_REMOVE(s,m)`: remove the non-physical vertical grid cells on the top and upper borders of the domain for each model m. Default: .TRUE.

* :code:`LOUT_PHYSICAL_SIMPLIFIED(s,m)`: simplify the domain by removing 1 extra layer of grid points for some fields located on non mass-point positions on the C-grid in the Arakawa convention. Enabling this option provides the advantage to get the same number of points for all fields in a given direction at the cost of losing some physical data on the borders. If disabled (default behaviour), some fields will have one more point in some directions.

* :code:`NOUT_BOXES(s,m)`: number of subdomains/boxes to write for each model m. If set to 0 (default value), the whole domain will be written. If set to more than 0, the whole domain will not be written except if forced with LOUT_MAINDOMAIN_WRITE=.TRUE. The maximum number of boxes is 20 (can be modified with the modification of a parameter and a recompilation of Meso-NH).

* :code:`COUT_BOX_NAME(s,m,b)`: name of the boxes for each model m

* :code:`NOUT_BOX_IINF(s,m,b)`: lower i index of the cartesian subdomain in the physical domain. This value must be provided (if the box is enabled).

* :code:`NOUT_BOX_ISUP(s,m,b)`: upper i index of the cartesian subdomain in the physical domain. This value must be provided (if the box is enabled).

* :code:`NOUT_BOX_JINF(s,m,b)`: lower j index of the cartesian subdomain in the physical domain. This value must be provided (if the box is enabled).

* :code:`NOUT_BOX_JSUP(s,m,b)`: upper j index of the cartesian subdomain in the physical domain. This value must be provided (if the box is enabled).

* :code:`NOUT_BOX_KINF(s,m,b)`: lower k index of the cartesian subdomain in the physical domain. This value must be provided (if the box is enabled).

* :code:`NOUT_BOX_KSUP(s,m,b)`: upper k index of the cartesian subdomain in the physical domain. This value must be provided (if the box is enabled).

* :code:`COUT_BOX_VAR_SUPP(s,m,b,f)`: list of the variables to write for the model m and the box b. List of fields common to all the boxes can be provided with the COUT_VAR parameter.

* :code:`LOUT_MAINDOMAIN_WRITE(s,m)`: write also the main domain in the case when NOUT_BOXES>0 (no effect if NOUT_BOXES=0). Default: .FALSE.

* :code:`NOUT_BOX_VAR_REDUCE_FLOAT_PRECISION(s,m,b,f)`: force writing of floating points numbers in single precision for the selected variables in the box. If set to 0, no reduction of precision will be done. If set to 1 (or > 0), reduction of precision will be done. By default, the value for the file (LOUT_REDUCE_FLOAT_PRECISION) is taken into account.

* :code:`OUT_BOX_VAR_COMPRESS_LEVEL(s,m,b,f)`: set the compression level per variable in the box. The value must be in the 0 to 9 interval (0 for no compression, 9 for maximum compression). By default, the value for the file (LOUT_COMPRESS and LOUT_COMPRESS_LEVEL) is taken into account.

* :code:`COUT_BOX_VAR_COMPRESS_LOSSY_ALGO(s,m,b,f)`: algorithm used to reduce the number of significants digits or bits per variable in the box. Set to 'NONE' to disable lossy compression. By default, the value for the file (LOUT_COMPRESS_LOSSY and LOUT_COMPRESS_LOSSY_ALGO) is taken into account.

* :code:`NOUT_BOX_VAR_COMPRESS_LOSSY_NSD(s,m,b,f)`: number of significants digits (for 'BitGroom', 'GranularBR') or bits (for 'BitRound') to keep per variable in the box. By default, the value for the file (LOUT_COMPRESS_LOSSY_ALGO_NSD) is taken into account.

* :code:`XOUT_BOX_VAR_THR_MIN(s,m,b,f)`: minimum threshold per variable in the box. If a value of the variable is strictly below this threshold, it is set to the one chosen with the COUT_BOX_VAR_THR_MIN_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`XOUT_BOX_VAR_THR_MAX(s,m,b,f)`: maximum threshold per variable in the box. If a value of the variable is strictly above this threshold, it is set to the one chosen with the COUT_BOX_VAR_THR_MAX_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`XOUT_BOX_VAR_THR_ABSMIN(s,m,b,f)`: absolute minimum threshold per variable in the box. If an absolute value of the variable is strictly below this threshold, it is set to the one chosen with the COUT_BOX_VAR_THR_ABSMIN_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`XOUT_BOX_VAR_THR_ABSMAX(s,m,b,f)`: absolute maximum threshold per variable in the box. If an absolute value of the variable is strictly above this threshold, it is set to the one chosen with the COUT_BOX_VAR_THR_ABSMAX_BEHAVIOR parameter. By default, no threshold is applied.

* :code:`COUT_BOX_VAR_THR_MIN_BEHAVIOR(s,m,b,f)`: behavior to apply when a value is below the minimum threshold in the box. Allowed values (described later in this section): 'ZERO', 'MIN' (default if threshold is not negative), 'FILLVALUE' (default if threshold is negative), 'VALIDMIN', 'UNDEF', 'NEGUNDEF', 'EXCLRANGE' and 'NONE' (default if no threshold is set).

* :code:`COUT_BOX_VAR_THR_MAX_BEHAVIOR(s,m,b,f)`: behavior to apply when a value is above the maximum threshold in the box. Allowed values (described later in this section): 'ZERO', 'MAX', 'FILLVALUE' (default if threshold is set), 'VALIDMAX', 'UNDEF', 'NEGUNDEF', 'EXCLRANGE' and 'NONE' (default if no threshold is set).

* :code:`COUT_BOX_VAR_THR_ABSMIN_BEHAVIOR(s,m,b,f)`: behavior to apply when an absolute value is below the absolute minimum threshold in the box. Allowed values (described later in this section): 'ZERO' (default if threshold is set), 'ABSMIN', 'FILLVALUE', 'UNDEF', 'NEGUNDEF' and 'NONE' (default if no threshold is set).

* :code:`COUT_BOX_VAR_THR_ABSMAX_BEHAVIOR(s,m,b,f)`: behavior to apply when an absolute value is above the absolute maximum threshold in the box. Allowed values (described later in this section): 'ABSMAX', 'FILLVALUE' (default if threshold is set), 'UNDEF', 'NEGUNDEF', 'ZERO' and 'NONE' (default if no threshold is set).

* :code:`XOUT_BOX_VAR_RND_FACTOR(s,m,b,f)`: rounding factor per variable in the box. This factor is applied to the variable values. Each value is rounded to a multiple of it. It has to be positive. This allows to significantly reduce the size of the output files if compression is enabled with a loss of precision. This approach is complementary to the lossy compression which manage the number of significant digits or bits.

.. note::

   The following behaviors are available for thresholds (allowed choices depend on the type of the threshold):

   * 'ZERO': set the value to 0
   * 'MIN': set the value to the minimum threshold
   * 'MAX': set the value to the maximum threshold
   * 'ABSMIN': set the value to the absolute minimum threshold with the sign of the original value 
   * 'ABSMAX': set the value to the absolute maximum threshold with the sign of the original value
   * 'FILLVALUE': set the value to the fill value (seen as an empty value in netCDF files)
   * 'VALIDMIN': set the value to the valid minimum value of the variable (netCDF metadata attribute)
   * 'VALIDMAX': set the value to the valid maximum value of the variable (netCDF metadata attribute)
   * 'UNDEF': set the value to the undefined value XUNDEF (999.0)
   * 'NEGUNDEF': set the value to the negative undefined value XNEGUNDEF (-999.0)
   * 'EXCLRANGE': exclude the value from the range defined by the min and max thresholds (if used, it must be set for both the min and max thresholds). Replacement value is the fill value.
   * 'NONE': do nothing

.. warning::

   * Not all fieldnames are possible. If a field is not (yet) known, it is possible to add a personalized one by modifying the IO_WRITE_FIELD_USER subroutine.
   * A choosen time must be a multiple of the timestep.
   * Different ways to choose the output times can be combined: a regular series (given with a frequency) + irregular times. Duplicate times will be automatically removed.
   * In grid-nesting, output times are propagated from the parent model to its children (children are allowed to have other output times). Children regular series must be aligned with parent ones. A regular parent output must always be at the same time than a regular children output. However, children may have more frequent regular backups (parent time frequency must be a multiple of children frequencies).
   * Lossy compression is possible for output files. This kind of compression leads to a loss of data but allows high reduction in the size of the output files. The procedure to reduce filespace is a two-phase process. Firstly, the last bits of each array elements are all set to 0 or 1 (alternatively to try to keep the average value). And secondly, standard compression is applied. Three algorithms are available. They are provided by the netCDF library. For each of them, it is possible to choose the number of significants digits or bits to keep.
   * Data in boxes (if NOUT_BOXES>0) is not written in Z-split files even if NB_PROCIO_W > 1
   * Lossy compression is only available for float numbers.
   * Thresholds and rounding factors are available only for float numbers.
   * Rounding factors are applied after thresholds.
   * It is not recommended (but not forbidden) to mix lossy compression and rounding factor for a variable.

