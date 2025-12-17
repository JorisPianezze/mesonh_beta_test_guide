.. _nam_les:

NAM_LES
-----------------------------------------------------------------------------

This namelist controls the diagnostics of turbulence, especially for Large Eddy Simulations. The diagnostics are saved in the diachronic file (.000).

.. csv-table:: NAM_LES content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LLES_MEAN","LOGICAL",".FALSE."
   "LLES_RESOLVED","LOGICAL",".FALSE."
   "LLES_SUBGRID","LOGICAL",".FALSE."
   "LLES_UPDRAFT","LOGICAL",".FALSE."
   "LLES_DOWNDRAFT","LOGICAL",".FALSE."
   "LLES_SPECTRA","LOGICAL",".FALSE."
   "LLES_CS_MASK","LOGICAL",".FALSE."
   "NLES_LEVELS","INTEGER(:)","all levels in physical domain"
   "XLES_ALTITUDES","REAL(:)",""
   "NSPECTRA_LEVELS","INTEGER(:)",""
   "XSPECTRA_ALTITUDES","REAL(:)",""
   "CLES_NORM_TYPE","CHARACTER(LEN=4)","'NONE'"
   "CBL_HEIGHT_DEF","CHARACTER(LEN=3)","'KE '"
   "XLES_TEMP_SAMPLING","REAL","60 s if CTURB='3DIM'"
   "","","300 s if CTURB='1DIM'"
   "XLES_TEMP_MEAN_START","REAL",""
   "XLES_TEMP_MEAN_END","REAL",""
   "XLES_TEMP_MEAN_STEP","REAL","3600 s"
   "LLES_CART_MASK","LOGICAL",".FALSE."
   "NLES_IINF","INTEGER","1 (physical domain boundary)"
   "NLES_ISUP","INTEGER","NIMAX physical domain boundary)"
   "NLES_JINF","INTEGER","1 (physical domain boundary)"
   "NLES_JSUP","INTEGER","NJMAX (physical domain boundary)"
   "LLES_NEB_MASK","LOGICAL",".FALSE."
   "LLES_CORE_MASK","LOGICAL",".FALSE."
   "LLES_MY_MASK","LOGICAL",".FALSE."
   "NLES_MASKS_USER","INTEGER","NUNDEF"

* :code:`LLES_MEAN` : flag for computation of the mean vertical profiles of the model variables

* :code:`LLES_RESOLVED` : flag for computation of the mean vertical profiles of the resolved fluxes, variances and covariances

* :code:`LLES_SUBGRID` : flag for computation of the  mean vertical profiles of the subgrid fluxes, variances and covariances

* :code:`LLES_UPDRAFT` : flag for computation of the updraft vertical profiles of some resolved and subgrid fluxes, variances and covariances

* :code:`LLES_DOWNDRAFT` : Same as LLES_UPDRAFT but for downdrafts.

* :code:`LLES_SPECTRA` : flag for computation of the non-local diagnostics (2 points correlations and spectra)

* :code:`LLES_CS_MASK` : flag for computation of the conditional sampling diagnostics                           

* :code:`NLES_LEVELS` : list of model levels in physical domain where the local quantities are computed. Default is: all physical model levels (by default, the vertical profiles are computed on the Meso-NH grid).

* :code:`XLES_ALTITUDES` : list of constant altitude levels where the local quantities are computed. Not used by default.

* :code:`NSPECTRA_LEVELS` : list of model levels in physical domain where the non-local quantities are computed. Any number is allowed, but too many will be costly in CPU time and memory.

* :code:`XSPECTRA_ALTITUDES` : list of constant altitude levels where the non-local quantities are computed. Any number is allowed, but too many will be costly in CPU time and memory.

* :code:`CLES_NORM_TYPE` : type of normalization for the fluxes and variances:

  * 'NONE': no normalization is computed (however, the quantities necessary to perform these are computed, and stored in the file)
  * 'CONV': convective normalization, using :math:`Q_0`, :math:`w_*`, h, :math:`<\overline{w'r'_v}>_{surf}`.
  * 'EKMA': Ekman normalization, using :math:`u_*` and :math:`L_{Ekman}`.
  * 'MOBU': Monin-Obukhov normalization, using :math:`L_{MO}`, :math:`u_*`, :math:`Q_0`, :math:`<\overline{w'r'_v}>_{surf}`.

* :code:`CBL_HEIGHT_DEF` : definition of the Boundary Layer height h:

  * 'KE ': test on total kinetic energy: :math:`E(h) + e(h) =  0.05 \frac{1}{h} \int_0^h{(E(z)+e(z))dz}`
  * 'WTV': test on :math:`<w'\theta'_v + \overline{w'\theta'_v }>`: height h where this flux is most negative.
  * 'DTH' : test on :math:`\theta` profile.
  * 'FRI' : test on the momentum flux, h is the height where the momentum flux is 5% its value at the surface.

* :code:`XLES_TEMP_SAMPLING` : time (seconds) between two samplings of the LES profiles and non-local quantities

* :code:`XLES_TEMP_MEAN_START` : time (seconds from the beginning of the simulation) at which the averaging begins. If not defined, no averaging is performed.

* :code:`XLES_TEMP_MEAN_END` : time (seconds from the beginning of the simulation) at which the averaging ends. If not defined, no averaging is performed.

* :code:`XLES_TEMP_MEAN_STEP` : time step (seconds) for averaging.                     

* :code:`LLES_CART_MASK` : flag to compute the LES diagnostics only inside a cartesian subdomain defined with the indexes of the model 1. Both local and non-local quantities can be computed.

* :code:`NLES_IINF` : lower i index of the cartesian subdomain in the physical domain. The default value is the physical domain left boundary.

* :code:`NLES_ISUP` : upper i index of the cartesian subdomain in the physical domain. The default value is the physical domain right  boundary.

* :code:`NLES_JINF` : lower j index of the cartesian subdomain in the physical domain. The default value is the physical domain bottom boundary.

* :code:`NLES_JSUP` : upper j index of the cartesian subdomain in the physical domain. The default value is the physical domain top boundary.

* :code:`LLES_NEB_MASK` : Flag to compute the LES diagnostics separately inside and outside  the model columns where clouds are present. Only local quantities can be computed.

* :code:`LLES_CORE_MASK` : Flag to compute the LES diagnostics separately inside and outside  the model columns where cloud core is present. Only local quantities can be computed.

* :code:`LLES_MY_MASK` : Flag to compute the LES diagnostics on a mask defined by the user as a 2D horizontal mask. It must be coded at the beginning of the LES monitor routine. Only local quantities can be computed with this mask.

* :code:`NLES_MASKS_USER` : number of user's masks
