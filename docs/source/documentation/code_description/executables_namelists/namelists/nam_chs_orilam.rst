.. _nam_chs_orilam:

NAM_CHS_ORILAM
----------------------------------------------------------------------------- 

Chemical aerosol scheme ORILAM.

.. csv-table:: NAM_CHS_ORILAM content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LCH_AERO_FLUX", "LOGICAL", ".FALSE."
   "LCO2PM", "LOGICAL", ".FALSE."
   "XEMISRADIUSI", "REAL", "0.036"
   "XEMISRADIUSJ", "REAL", "0.385"
   "XEMISSIGI", "REAL", "1.86"
   "XEMISSIGJ", "REAL", "1.29"
   "CRGUNIT", "CHARACTER(LEN=4)", "NUMB"
   
* :code:`LCH_AERO_FLUX` : switch to active aerosol surface flux for ORILAM

* :code:`LCO2PM` : switch to activate emission of primary aerosol (Black and Organic carbon) compute from CO emssion. Uses only if CO emission is defined in the surface field (see :ref:`prep_pgd`) and if there is no data for primary aerosol emissison.

* :code:`XEMISRADIUSI` : Aerosol flux, mean radius of aitken mode in μm (only if LCH_AERO_FLUX=T).

* :code:`XEMISRADIUSJ` : Aerosol flux, mean radius of accumulation mode in μm (only if LCH_AERO_FLUX=T).

* :code:`XEMISSIGI` : Aerosol flux, standard deviation of aitken mode in μm (only if LCH_AERO_FLUX=T).

* :code:`XEMISSIGJ` : Aerosol flux, standard deviation of accumulation mode in μm (only if LCH_AERO_FLUX=T).

* :code:`CRGUNIT` : Aerosol flux, Definition of XEMISRADIUSI or XEMISRADIUSJ: mean radius can be define in mass ("MASS") or in number (NUMB).
