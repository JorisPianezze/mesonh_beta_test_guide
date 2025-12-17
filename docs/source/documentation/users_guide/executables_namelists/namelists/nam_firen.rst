.. _nam_firen:

NAM_FIREn
-----------------------------------------------------------------------------

The Blaze fire model is configured by editing this namelist. In grid-nesting, it is only allowed (LBLAZE=T) on the finest models (without child). It contains the variables and types for the Blaze fire model. More informations about the scheme and on input data construction with python Pyrolib package on https://pypi.org/project/pyrolib/ and https://pyrolib.readthedocs.io/en/latest/.

.. csv-table:: NAM_FIREn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LBLAZE","LOGICAL",".FALSE."
   "NREFINX","INTEGER","1"
   "NREFINY","INTEGER","1"
   "CFIRE_CPL_MODE","CHARACTER(LEN=7)","'2WAYCPL'"
   "CBMAPFILE","CHARACTER(LEN=128)","CINIFILE"
   "CPROPAG_MODEL","CHARACTER(LEN=11)","'SANTONI2011'"
   "CHEAT_FLUX_MODEL","CHARACTER(LEN=3)","'EXS'"
   "CLATENT_FLUX_MODEL","CHARACTER(LEN=3)","'EXP'"
   "XFERR","REAL","0.8"
   "LSGBAWEIGHT","LOGICAL",".FALSE."
   "XFLUXZEXT","REAL","3.0"
   "XFLUXZMAX","REAL","4.*XFLUXZEXT"
   "XFLXCOEFTMP","REAL","1.0"
   "NFIRE_WENO_ORDER","INTEGER","3"
   "NFIRE_RK_ORDER","INTEGER","3"
   "XCFLMAXFIRE","REAL","0.8"
   "XLSDIFFUSION","REAL","0.1"
   "XROSDIFFUSION","REAL","0.05"
   "LINTERPWIND","LOGICAL",".TRUE."
   "LWINDFILTER","LOGICAL",".FALSE."
   "CWINDFILTER","CHARACTER(LEN=4)","'EWAM'"
   "XEWAMTAU","REAL","20.0"
   "XWLIMUTH","REAL","8.0"
   "XWLIMUTMAX","REAL","9.0"
   "NNBSMOKETRACER","INTEGER","1"
   "NWINDSLOPECPLMODE","INTEGER","0"

* :code:`LBLAZE` : flag to activate the Blaze fire model.

* :code:`NREFINX` : Refinement ratio for fire mesh in the x direction.

* :code:`NREFINY` : Refinement ratio for fire mesh in the y direction.

* :code:`CFIRE_CPL_MODE` : atmosphere/fire coupling mode. Three options are available:

  * 2WAYCPL: two-way coupled mode. Fire spread and heat fluxes computations are activated
  * ATM2FIR: one way coupling where atmosphere forces the fire. Only fire spread computation is activated.
  * FIR2ATM: fire replay mode where the fire spread is derived from an arrival time map and the heat fluxes computation is activated.

* :code:`CBMAPFILE` : File name of arrival time map (burning map) for FIR2ATM mode (current initialisation file as default file).

* :code:`CPROPAG_MODEL` : Rate of spread parameterization. Following options are available:

  * SANTONI2011: Balbi's model based on :cite:t:`santoni_wildland_2011` formulation.

* :code:`CHEAT_FLUX_MODEL` : sensible heat flux parameterization. Following options are available:

  * EXS: Exponential and smoldering flux model.
  * EXP: Exponential flux model.
  * CST: Constant flux model.

* :code:`CLATENT_FLUX_MODEL` : latent heat flux parameterization. Following options are available:

  * EXP: Exponential flux model.
  *  CST: Constant flux model.

* :code:`XFERR` : fraction of energy reservoir released during the flaming time (:math:`0 < \mathrm{XFERR} < 1`).

* :code:`LSGBAWEIGHT` : flag to use to use the weighted averaged method to compute the sub-grid burning area instead of the explicite fire front reconstruction (EFFR) method (Recommended to FALSE).

* :code:`XFLUXZEXT` : Characteristic height :math:`z_f` for vertical exponential distribution of fire heat fluxes.

* :code:`XFLUXZMAX` : maximum height :math:`z_{\mathrm{max}}` for vertical exponential distribution of fire heat fluxes.

* :code:`XFLXCOEFTMP` : heat fluxes multiplier.

* :code:`NFIRE_WENO_ORDER` : WENO scheme order for fire spread computation. Orders 1 and 3 available (order 3 recommended).

* :code:`NFIRE_RK_ORDER` : Runge-Kutta scheme order for fire spread computation. Orders 1, 2, 3, 4, 5, 6 available (order 3 recommended).

* :code:`XCFLMAXFIRE` : maximum CFL for fire spread computation. If computed CFL is above this value, fire time step is split to match the required maximum CFL.

* :code:`XLSDIFFUSION` : level-set function diffusion coefficient :math:`\epsilon_\phi`.

* :code:`XROSDIFFUSION` : rate of spread diffusion coefficient :math:`\epsilon_{\mathcal R}`.

* :code:`LINTERPWIND` : flag to use horizontal interpolation of surface wind (recommended to .TRUE.).

* :code:`LWINDFILTER` : flag to use temporal filter for surface wind. Recommended for highly fluctuating surface wind.

* :code:`CWINDFILTER` : Method for temporal filtering of surface wind. Follong options are available:

  * EWAM: exponential weighted average method used of each wind component (Recommended)
  * WLIM: limiter of surface wind on fire spread direction.

* :code:`XEWAMTAU` : averaging time constant for EWAM method. Equivalent to averaging time window for simple moving average method.

* :code:`XWLIMUTH` : wind threshold value for WLIM method.

* :code:`XWLIMUTMAX` : maximum surface wind value for WLIM method.

* :code:`NNBSMOKETRACER` : number of smoke passive scalar fluxes. Made for futur implementation of different smoke flux models. Only 1 smoke passive scalar is currently implemented.

* :code:`NWINDSLOPECPLMODE` : flag for wind/slope use for rate of spread computation. Suitable for testing/sensitivity analysis purposes. Following options are available:
  
  * 0: Wind and slope values are used to compute the rate of spread.
  * 1: Only wind is used to compute the rate of spread (slope value is ignored).
  * 2: Only slope is used to compute the rate of spread (wind value is ignored).
