.. _nam_ver_grid:

NAM_VER_GRID
-----------------------------------------------------------------------------


There are three ways to compute the vertical grid:

* **constant grid mesh:** only the number of levels :code:`NKMAX` and the grid mesh sizes :code:`ZDZGRD` and :code:`ZDZTOP` are used. :code:`ZDZGRD` and :code:`ZDZTOP` must have the same value. The type of grid :code:`YZGRID_TYPE` has to be set to 'FUNCTN'.

* **two layers are defined, with different stretching in each layer:** the grid mesh size is given near the ground with :code:`ZDZGRD` and at top of the model with :code:`ZDZTOP` and the stretching coefficients :code:`ZSTRGRD`, :code:`ZSTRTOP` and :code:`ZZMAX_STRGRD` has to be defined. It is possible that the top grid size is never reached if the number of points is not enough for the prescribed stretchings. The type of grid :code:`YZGRID_TYPE` has to be set to 'FUNCTN'.

* **the vertical discretization is given by the user:** the type of grid :code:`YZGRID_TYPE` has to be set to 'MANUAL' and only the number of levels NKMAX is used.

The variables of this namelist are:

.. csv-table:: NAM_VER_GRID content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LTHINSHELL","LOGICAL",".FALSE."
   "NKMAX","INTEGER","10"
   "YZGRID_TYPE","CHARACTER(LEN=6)","'FUNCTN'"
   "ZDZGRD","REAL","300.0"
   "ZDZTOP","REAL","300.0"
   "ZZMAX_STRGRD","REAL","0.0"
   "ZSTRGRD","REAL","0.0"
   "ZSTRTOP","REAL","0.0"
   "LSLEVE","LOGICAL",".FALSE."
   "XLEN1","REAL","7500.0"
   "XLEN2","REAL","2500.0"


* :code:`LTHINSHELL` : Flag for the thinshell approximation

* :code:`NKMAX` : number of points in z-direction of the required physical domain. The total size of the array written in initial file will be NKMAX + 2*JPVEXT (JPVEXT is fixed to 1 for the present version of Meso-NH).

* :code:`YZGRID_TYPE` : type of vertical grid definition:

  * 'FUNCTN': the vertical grid is given by a regular logarithmic function, whose variation is determined by the values of free parameters :code:`ZDZGRD`, :code:`ZDZTOP`, :code:`ZSTRGRD`, :code:`ZSTRTOP` and :code:`ZZMAX_STRGRD`.
  * 'MANUAL': the levels are explicitly given in the :ref:`free-formatted part <freeformat_prep_ideal_case>` with the keyword ZHAT by entering the heights of the different levels from  K=2 to K= KMAX + 2).

* :code:`ZDZGRD` : mesh length in z-direction near the ground

* :code:`ZDZTOP` : mesh length in z-direction near the top of the model

* :code:`ZZMAX_STRGRD` : Altitude separating the two constant stretching layers

* :code:`ZSTRGRD` : Constant imposed stretching (in %) in the lower layer (below :code:`ZZMAX_STRGRD`)

* :code:`ZSTRTOP` : Constant imposed stretching (in %) in the upper layer (above :code:`ZZMAX_STRGRD`)

* :code:`LSLEVE` : flag for Sleve vertical coordinate.

* :code:`XLEN1` : decay scale for smooth topography (in meters)

* :code:`XLEN2` : decay scale for smale-scale topography deviation (in meters)
