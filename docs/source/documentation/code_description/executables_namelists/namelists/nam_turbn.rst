.. _nam_turbn:

NAM_TURBn
----------------------------------------------------------------------------- 

It contains the characteristics of the turbulence scheme used by the model n. They are included in the declarative module MODD_TURBn.

.. csv-table:: NAM_TURBn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XIMPL","REAL","1.0"
   "CTURBLEN","CHARACTER(LEN=4)","'BL89'"
   "CTURBDIM","CHARACTER(LEN=4)","'1DIM'"
   "XCADAP","REAL","0.5"
   "LTURB_FLX","LOGICAL",".FALSE."
   "LTURB_DIAG","LOGICAL",".FALSE."
   "LSIG_CONV","LOGICAL",".FALSE."
   "LRMC01","LOGICAL",".FALSE."
   "CTOM","CHARACTER(LEN=4)","'NONE'"
   "XTKEMIN","REAL","0.01"
   "XCED","REAL","0.84"
   "LLEONARD","LOGICAL",".FALSE."
   "XCOEFHGRADTHL","REAL","1.0"
   "XCOEFHGRADRM","REAL","1.0"
   "XALTHGRAD","REAL","2000.0"
   "XCLDTHOLD","REAL","-1.0"
   "LCLOUDMODIFLM","LOGICAL",".FALSE."
   "CTURBLEN_CLOUD","CHARACTER(LEN=4)","'DELT'"
   "XCOEF_AMPL_SAT","REAL","5.0"
   "XCEI_MIN","REAL","0.001E-6"
   "XCEI_MAX","REAL","0.01E-6"
   "XLINI","REAL","0.1"
   "XCTP","REAL","4.0 if LSTATNW"
   "","","else 4.65"
   "XMINSIGS","REAL","1.E-12"
   "LHARAT","LOGICAL",".FALSE."
   "LPROJQITURB","LOGICAL",".TRUE."
   "LSMOOTH_PRANDTL","LOGICAL",".TRUE."
   "NTURBSPLIT","INTEGER","1"
   "LTURB_PRECIP","LOGICAL",".FALSE."

* :code:`XIMPL` : degree of implicitness of the vertical part of the turbulence scheme. (XIMPL = 0.5 corresponds to the Cranck-Nicholson scheme for the vertical turbulent diffusion and  0. to a purely explicit scheme)

* :code:`CTURBDIM` : turbulence dimensionality. 

  * '1DIM'  Only the vertical turbulent fluxes are taken into account. This has to be done for relatively large horizontal gridsizes.
  * '3DIM'  All the turbulent fluxes are computed, this is necessary for small horizontal gridsizes ( meso-:math:`\gamma` scales or LES)

* :code:`CTURBLEN` : type of turbulent mixing length.

  * 'DELT' If CTURBDIM='3DIM', the cubic root of the grid volum is used in 3D simulations and  the squared root of the volum in 2D simulations.
  * '1DIM', we take :math:`\Delta z` in simulation of any dimensionality. This length is always limited to :math:`\kappa * z`  near the ground.
  * 'BL89' The mixing length is computed according to the Bougeault and Lacarrère scheme (refer to the scientific documentation)
  * 'DEAR' the mixing length is given by the mesh size depending on the model dimensionality, this length is limited to the ground distance and also by the Deardorff mixing length pertinent in the stable cases.
  * 'RM17' The mixing length is computed according to Rodier et al. (2017). It is a non-local mixing length combining BL89 with a wind shear term.
  * 'HM21' resolution-adaptative mixing length is computed according to Honnert et al. (2021) and given by the minimum between RM17 and the horizontal resolution XCADAP :math:`\sqrt{\Delta x \Delta y}`, where XCADAP is a namelist parameter set to 0.5.

* :code:`XCADAP` : coefficient applied to the HM21 adaptative mixing length

* :code:`LTURB_FLX` : flag to compute and store all the turbulent fluxes  on every output synchronous file.

* :code:`LTURB_DIAG` : flag to  store diagnostic quantities related to the turbulent scheme  on every output synchronous file. (mesh length, Prandtl number, Schmidt number, sources of TKE\ldots)

* :code:`LSIG_CONV` : Flag for computing Sigma_s due to convection in ice subgrid condensation scheme

* :code:`LRMC01` : Flag for computing separate mixing and dissipative length in the SBL according to Redelsperger, Mahe and Carlotti 2001

* :code:`CTOM` : Consideration of Third Order Moments.

  * 'NONE': No Third Order moments                             
  * 'TM06': Parameterization of Third Order moments of heat fluxes for dry CBL according to Tomas and Masson (2006).

* :code:`XTKEMIN` : minimum value for the TKE (:math:`m^{2}.s^{-2}`).

* :code:`XCED` : Constant for TKE dissipation (with CTURBLEN='RM17' it is better to use XCED=0.34 according to Rodier et al., 2017).

* :code:`LLEONARD` : Flag to compute the Leonard terms (instead of K-gradient terms) applied to the vertical fluxes of :math:`\theta_l` and :math:`r_{np}` (:math:`r_c` + :math:`r_i` + :math:`r_v`). The main effects are an increase of TKE and a decrease of vertical velocity.

* :code:`XCOEFHGRADTHL` : coefficient applied to the vertical turbulent flux of :math:`\theta_l`.

* :code:`XCOEFHGRADRM` : coefficient applied to the vertical turbulent flux of non precipitating total water mixing ratio :math:`r_{np}`.

* :code:`XALTHGRAD` : height above ground from which the Leonard terms are applied.

* :code:`XCLDTHOLD` : mixing ratios threshold (:math:`r_c + r_i`) from which the Leonard terms are applied. For instance, XCLDTHOLD :math:`10^{-6}` kg/kg to apply only on clouds. XCLDTHOLD=-1 to apply everywhere.

* :code:`LCLOUDMODIFLM` : model number where the modification of the mixing length in the clouds is computed.

* :code:`CTURBLEN_CLOUD` : type of turbulent mixing length in the clouds  ('BL89','DELT','DEAR': see CTURBLEN for meanings),

* :code:`XCOEF_AMPL_SAT` : saturation of the amplification coefficient,

* :code:`XCEI_MIN` : minimum threshold for the instability index (in kg/kg/m/s,  beginning of the amplication),

* :code:`XCEI_MAX` : maximum threshold for the instability index (in kg/kg/m/s, beginning of the saturation of the amplification).

* :code:`XCTP` : Constant for temperature and vapor pressure-correlations (if not defined, the value depends on LSTATNW)

* :code:`XMINSIGS` : minimum value of the variance of the deficit to the saturation out of the turbulence scheme :math:`kg^2.kg^{-2}`)

* :code:`LHARAT` : flag to activate the RACMO turbulence scheme

* :code:`LPROJQITURB` : flag to project the :math:`r_t` tendency on :math:`r_c` and :math:`r_i`

* :code:`LSMOOTH_PRANDTL` : flag to smooth the Prandtl functions

* :code:`NTURBSPLIT` : number of time-splitting for the computation of horizontal turbulent fluxes

* :code:`LTURB_PRECIP` : flag to activate the turbulent mixing of mixing ratios of snow, graupel, hail and liquid droplets :math:`r_s`, :math:`r_g`, :math:`r_h`, and :math:`r_r`

.. note::

   Diagnostic quantities are written on every synchronuous files (mixing length in clear sky, mixing length modified, amplification coefficient, ...) if LTURB_DIAG=.TRUE. in :ref:`nam_turbn`.

