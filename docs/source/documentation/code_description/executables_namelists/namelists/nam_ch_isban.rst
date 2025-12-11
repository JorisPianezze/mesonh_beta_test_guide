.. _nam_ch_isban:

NAM_CH_ISBAn
----------------------------------------------------------------------------- 

Chemical deposition and biogenic emissions over vegetation.

.. csv-table:: NAM_CH_ISBAn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CCH_DRY_DEP", "CHARACTER(LEN=6)", "'WES89'"
   "LCH_BIO_FLUX", "LOGICAL", ".FALSE."
   "LCH_NO_FLUX", "LOGICAL", ".FALSE."
   
* :code:`CCH_DRY_DEP` : type of deposition scheme.
  
  * 'NONE' : no chemical deposition scheme. 
  * 'WES89' : :cite:t:`wesely_parameterization_1989` deposition scheme.

* :code:`LCH_BIO_FLUX` : flag to activate the biogenic emissions.

* :code:`LCH_NO_FLUX` : flag to activate the NO emissions.   
