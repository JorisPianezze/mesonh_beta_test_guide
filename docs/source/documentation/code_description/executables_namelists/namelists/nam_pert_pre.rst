.. _nam_pert_pre:

NAM_PERT_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_PERT_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CPERT_KIND","CHARACTER(LEN=2)","'TH'"
   "XAMPLITH","REAL","1.5"
   "XAMPLIRV","REAL","0.0"
   "XAMPLIUV","REAL","1.0834"
   "XAMPLIWH","REAL","0.1"
   "NKWH","INTEGER","2"
   "LSET_RHU","LOGICAL",".TRUE."
   "XCENTERZ","REAL","2000.0"
   "XRADX","REAL","10000.0"
   "XRADY","REAL","10000.0"
   "XRADZ","REAL","2000.0"
   "LWH_LBXU","LOGICAL",".FALSE."
   "LWH_LBYV","LOGICAL",".FALSE."

* :code:`CPERT_KIND` : Defines the type of the perturbation

  * 'TH' : thermodynamical fields perturbation (:math:`\theta` and :math:`r_v`)
  * 'UV' : horizontal wind fields perturbation (U and V)
  * 'WH' :  white noise applied to :math:`\theta`
  * 'WW' :  white noise applied to wind components

* :code:`XAMPLITH` : maximum perturbation for :math:`\theta`

* :code:`XAMPLIRV` : maximum perturbation  for :math:`r_v`

* :code:`XAMPLIUV` : maximum perturbation for U and V

* :code:`XAMPLIWH` : maximum perturbation for the normalized white noise (temperature or wind)

* :code:`NKWH` : Upper level of the layer starting from the ground where the white noise is applied

* :code:`LSET_RHU` : Conservation of the relative humidity

  * TRUE the relative humidity is conserved in the :math:`\theta` perturbation
  * FALSE the :math:`r_v` perturbation is computed with the XAMPLIRV amplitude

* :code:`XCENTERZ` : Height of the maximum of the :math:`\theta` perturbation (m)

* :code:`XRADX` : radius of the perturbation along X (m)

* :code:`XRADY` : radius of the perturbation along Y (m)

* :code:`XRADZ` : radius of the perturbation along Z (m)

* :code:`LWH_LBXU` : White noise in inflow and outflow LBC of U

* :code:`LWH_LBXV` : White noise in inflow and outflow LBC of V
