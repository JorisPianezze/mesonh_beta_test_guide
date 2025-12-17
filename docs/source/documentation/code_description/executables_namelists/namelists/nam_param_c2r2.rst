.. _nam_param_c2r2:

NAM_PARAM_C2R2
-----------------------------------------------------------------------------

It contains the control parameters for the C2R2 warm microphysical scheme (CCLOUD = "C2R2" or "KHKO" in :ref:`nam_paramn`).

.. csv-table:: NAM_PARAM_C2R2 content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "HPARAM_CCN","CHARACTER(LEN=3)","'XXX'"
   "HINI_CCN","CHARACTER(LEN=3)","'XXX'"
   "HTYPE_CCN","CHARACTER(LEN=1)","'X'"
   "XCHEN","REAL","0.0"
   "XKHEN","REAL","0.0"
   "XMUHEN","REAL","0.0"
   "XBETAHEN","REAL","0.0"
   "XCONC_CCN","REAL","0.0"
   "XR_MEAN_CCN","REAL","0.0"
   "XLOGSIG_CCN","REAL","0.0"
   "XFSOLUB_CCN","REAL","1.0"
   "XACTEMP_CCN","REAL","280.0"
   "XALPHAC","REAL","3.0"
   "XNUC","REAL","1.0"
   "XALPHAR","REAL","1.0"
   "XNUR","REAL","2.0"
   "LRAIN","LOGICAL",".TRUE."
   "LSEDC","LOGICAL",".TRUE."
   "LACTIT","LOGICAL",".FALSE."
   "LSUPSAT","LOGICAL",".FALSE."
   "LDEPOC","LOGICAL",".FALSE."
   "XVDEPOC","REAL","0.02"
   "LACTTKE","LOGICAL",".TRUE."

* :code:`HPARAM_CCN` : Acronym of the CCN activation parameterization to use ('CPB','TFH' or 'TWO'). The 'TFH' and 'TWO' need only to prescribe the XCHEN and XKHEN parameters.

  * 'TWO' refers to the classical activation spectrum of Twomey in the form :math:`N_{CCN}(s)= C s^k`
  * 'TFH' includes some improvements brought by :cite:t:`feingold_parameterizations_1992` to the original activation spectrum of Twomey.
  * 'CPB' refers to an activation spectrum in the form defined in :cite:t:`cohard_extending_1998` with 
  
  .. math::

     N_{CCN}(s)= C s^k F(\mu,\frac{\displaystyle{k}}{\displaystyle{2}},\frac{\displaystyle{k}}{\displaystyle{2}}+1;-\beta s^2)
   
  where F is the hypergeometric function and :math:`[C, k, \mu, \beta]`, four adjustable  coefficients.

* :code:`HINI_CCN` : If HPARAM_CCN='CPB' then the initial CCN characteristics are given in the 'CCN' or 'AER' format. In the 'CCN' case, the parameters XCHEN, XKHEN, XMUHEN and XBETAHEN must be given while it is the case for XCONC_CCN, XR_MEAN_CCN, XLOGSIG_CCN, XFSOLUB_CCN and XACTEMP_CCN if the 'AER' option is  chosen. 

  * 'CCN' The aerosols are directly characterized by their activation spectrum :math:`N_{CCN}(s)` in the form :math:`C s^k` or 
  
  .. math::

     C s^k F(\mu,\frac{\displaystyle{k}}{\displaystyle{2}},\frac{\displaystyle{k}}{\displaystyle{2}}+1;-\beta s^2)
                  
  * 'AER' The aerosols are particles which are characterized by a lognormal  distribution law in the form: 

  .. math::

     {\displaystyle N}/{\displaystyle {\sqrt {2 \pi}} {\rm ln}(\sigma)} exp \Big ( - {\displaystyle {\rm ln} (r/\overline{r})^2}/{\displaystyle 2 {\rm ln}(\sigma)^2} \Big )
                   
  with distribution parameters (:math:`\overline{r}` is the geometric mean radius, :math:`\sigma` the geometric standard deviation and N the total particle number), by their solubility (:math:`\epsilon_m`) and by their activation temperature (T) as described by :cite:t:`cohard_parameterization_2000`.

* :code:`HTYPE_CCN` : Aerosol type ('M' or 'C') if HPARAM_CCN=='CPB' and HINI_CCN=='AER' is chosen.

  * 'M': NaCl composition (large size maritime aerosols)
  * 'C': (NH4)2SO4 composition (small size continental aerosols)

* :code:`XCHEN` : C parameter  in the generic activation spectrum :math:`N_{CCN}(s)`

* :code:`XKHEN` : k parameter in the generic activation spectrum :math:`N_{CCN}(s)`

* :code:`XMUHEN` : :math:`\mu` parameter in the hypergeometric function of the CPB form of the activation spectrum :math:`N_{CCN}(s)`

* :code:`XBETAHEN:  :math:`\beta` parameter in the hypergeometric function of the CPB form of the activation spectrum :math:`N_{CCN}(s)`

* :code:`XCONC_CCN` : aerosol concentration number (N)

* :code:`XR_MEAN_CCN` : geometric mean radius of the aerosol distribution (:math:`\overline{r}`)

* :code:`XLOGSIG_CCN` : natural logarithm of the geometric standard deviation of  the aerosol distribution (:math:`{\rm ln}(\sigma)`)

* :code:`XFSOLUB_CCN` : Mean solubility of the aerosols (:math:`\epsilon_m`)

* :code:`XACTEMP_CCN` : Mean air temperature at which activation will occur.

* :code:`XALPHAC` : First dispersion parameter (:math:`\alpha_c`) of the :math:`\gamma`-distribution law of the cloud droplets : 

  .. math::
  
     \gamma_c (D)=\frac{\displaystyle{\alpha_c}}{\displaystyle{\Gamma(\nu_c)}} \lambda_c^{\alpha_c \nu_c} D ^{\alpha_c \nu_c -1} exp\big(-(\lambda_c D)^{\alpha_c}\big)

* :code:`XNUC` : Second dispersion parameter (:math:`\nu_c`) of the :math:`\gamma`-distribution law of the cloud droplets

* :code:`XALPHAR` : First dispersion parameter (:math:`\alpha_r`) of the :math:`\gamma`-distribution law of the rain drops

  .. math::
  
     \gamma_r (D)=\frac{\displaystyle{\alpha_r}}{\displaystyle{\Gamma(\nu_r)}} \lambda_r^{\alpha_r \nu_r} D ^{\alpha_r \nu_r -1} exp\big(-(\lambda_r D)^{\alpha_r}\big))

* :code:`XNUR` : Second dispersion parameter (:math:`\nu_r`) of the :math:`\gamma`-distribution law of the rain drops

* :code:`LRAIN` : Enables the rain formation (by cloud droplet autoconversion) if set to TRUE

* :code:`LSEDC` : Cloud droplets are allowed to sediment if set to TRUE

* :code:`LACTIT` : Activation by radiative cooling is taken into account if set to  TRUE

* :code:`LSUPSAT` : Pseudo-prognostic supersaturation according to :cite:t:`thouron_supersaturation_2012` taken into account if set to  TRUE

* :code:`LDEPOC` : TRUE to enable cloud droplet deposition

* :code:`XVDEPOC` : Droplet deposition velocity

* :code:`LACTTKE` : TRUE to take into account TKE in the calculation of vertical velocity for activation
