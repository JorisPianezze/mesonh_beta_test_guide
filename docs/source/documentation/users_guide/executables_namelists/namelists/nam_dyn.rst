.. _nam_dyn:

NAM_DYN
-----------------------------------------------------------------------------

It contains the dynamics parameters common to all models. They are included in the module MODD_DYN.

.. csv-table:: NAM_DYN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XSEGLEN","REAL","43200.0"
   "XASSELIN","REAL","0.2"
   "XASSELIN_SV","REAL","0.02"
   "LCORIO","LOGICAL",".TRUE."
   "LNUMDIFU","LOGICAL",".TRUE."
   "LNUMDIFTH","LOGICAL",".FALSE."
   "LNUMDIFSV","LOGICAL",".FALSE."
   "LZDIFFU","LOGICAL",".FALSE."
   "XALKTOP","REAL","0.01"
   "XALZBOT","REAL","4000.0"
   "XALKGRD","REAL","0.01"
   "XALZBAS","REAL","0.01"

* :code:`XSEGLEN` : Segment length in seconds, corresponding to the duration of the segment simulation.

* :code:`XASSELIN` : Amplitude of the Asselin temporal  filter for meteorological variables

* :code:`XASSELIN_SV` : Same as XASSELIN but for scalar variables

* :code:`LCORIO` : Flag to set the Coriolis parameters :math:`f` and :math:`f^*` to zero

  * .TRUE.  the Earth rotation is taken into account
  * .FALSE. the Earth rotation effects are neglected  

* :code:`LNUMDIFU` : Flag to activate the numerical diffusion for momentum : advised to activate if CUVW_ADV_SCHEME='CEN4TH' or 'CEN2ND', and to not activate if CUVW_ADV_SCHEME='WENO_K' (XT4DIFU in :ref:`nam_dynn` defines the intensity of this diffusion).

* :code:`LNUMDIFTH` : Flag to activate the numerical diffusion for meteorological scalar variables (temperature, water substances and TKE) (XT4DIFTH in NAM_DYNn defines the intensity of this diffusion). If CMET_ADV_SCHEME is PPM_01, it is not necessary to activate numerical diffusion.

* :code:`LNUMDIFSV` : Same as LNUMDIFTH but for scalar variables

* :code:`LZDIFFU` : Flag to apply the horizontal diffusion to potential temperature and vapor mixing ratio according to :cite:t:`zangl_stratified_2002` adapted to mountainous topography. No amplitude is applied for this type of diffusion.

  * .TRUE. : This horizontal diffusion is applied 
  * .FALSE. : This horizontal diffusion is not applied           

.. note::

   This flag is independant from LNUMDIFU and LNUMDIFSV, applied to the dynamical variables and the scalar variables respectively.

* :code:`XALKTOP` : Maximum value of the Rayleigh damping (in :math:`s^{-1}`) for the upper absorbing layer. 
The shape of the absorbing layer is a :math:`\sin^2` of :math:`\hat{z}` (see the scientific documentation for more details).
To use with :code:`LVE_RELAX=T` in :ref:`nam_dynn`.

* :code:`XALZBOT` : Height (in meters) in the physical space of the base of the upper absorbing layer. 
  To use with :code:`LVE_RELAX=T` in :ref:`nam_dynn`.

* :code:`XALKGRD` : Maximum value of the Rayleigh damping (in :math:`s^{-1}`) for the lower absorbing layer.
  To use with :code:`LVE_RELAX_GRD=T` in :ref:`nam_dynn`.

* :code:`XALZBAS` : Height (in meters) in the physical space of the top of the ground absorbing layer.
  To use with :code:`LVE_RELAX_GRD=T` in :ref:`nam_dynn`.

