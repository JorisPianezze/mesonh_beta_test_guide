.. _nam_conf_pre:

NAM_CONF_PRE
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.
   
.. csv-table:: NAM_CONF_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LCARTESIAN","LOGICAL",".TRUE."
   "LPACK","LOGICAL",".TRUE."
   "CEQNSYS","CHARACTER(LEN=3)","'DUR'"
   "NVERB","INTEGER","5"
   "CIDEAL","CHARACTER(LEN=4)","'CSTN'"
   "CZS","CHARACTER(LEN=4)","'FLAT'"
   "LBOUSS","LOGICAL",".FALSE."
   "LPERTURB","LOGICAL",".FALSE."
   "LFORCING","LOGICAL",".FALSE."
   "LSHIFT","LOGICAL",".FALSE."
   "L2D_ADV_FRC","LOGICAL",".FALSE."
   "L2D_REL_FRC","LOGICAL",".FALSE."
   "NHALO","INTEGER","1"
   "JPHEXT","INTEGER","1"
   "LOCEAN","LOGICAL",".FALSE."

* :code:`LCARTESIAN` : Flag for cartesian geometry 

  * .TRUE. for cartesian geometry
  * .FALSE. for conformal projection

* :code:`LPACK` : Flag to compact 1D or 2D fields

* :code:`CEQNSYS` : Equation system resolved by Meso-NH

  * 'LHE' Lipps and HEmler anelastic system
  * 'DUR' approximated form of the DURran version of the anelastic sytem
  * 'MAE' classical Modified Anelastic Equations but with not any approximation in the momentum equation

* :code:`NVERB` : verbosity level

  * 0 for minimum of prints
  * 5 for intermediate level of prints
  * 10 for maximum of prints.

  .. note::

     If CSURF='EXTE' in namelist :ref:`nam_grn_pre`, NVERB=10 prints two LaTeX files containing the initialisation of surface scheme variables for each type of surface cover.

* :code:`CIDEAL` : kind of idealized fields 

  * 'CSTN' : Constant moist Brunt Vaisala frequency case 
  * 'RSOU' : radiosounding case

* :code:`CZS` : orography selector. The formulae are given below in the description of the namelist :ref:`nam_gridh_pre`.

  * 'FLAT' : constant XHMAX orography (zero by default)
  * 'SINE' : sine-shaped orography 
  * 'BELL' : bell-shaped orography
  * 'AGNE' : orography with :math:`h*a^2/(x^2+a^2)` shape
  * 'DATA' : discretized orography. The data describing the orography are given in the free format part (:ref:`freeformat_prep_ideal_case`).

* :code:`LBOUSS` : Flag for a Boussinesq version. 

  * .TRUE. The reference anelastic state is :math:`\theta _{ref} = cte = \theta _{ref} (z=0)` and :math:`\rho _{ref} = cte = \rho _{ref} (z=0)`.  In this case, the stratification is taken into account in the Meso-NH model in the flottability term. The typical length, on which this stratification varies, is much greater than the domain heigth and the :math:`\theta_{ref}` variation can be therefore neglected.
  * .FALSE. The reference anelastic state varies with the altitude.

* :code:`LPERTURB` : Flag to add a perturbation on the initially horizontally homogeneous fields. This perturbation is not balanced. 3 perturbation types are implemented in the routine :file:`set_perturb.f90`:

  * a spherical perturbation  on the dry potential temperature  and the moisture  fields (typical for convection initialization).
  * a perturbation on the horizontal components of the wind derived from a streamfunction (typical for large scale studies). This prevents the wind from becoming divergent. 
  * a perturbation on the dry potential temperature field at the first mass level near the ground, corresponding to a white noise (uniform amplitude in the spectral space) (typical for Large Eddy Simulations initialization)  

  .. note::

     When set to .TRUE., the parameters for the exact definition of the perturbation can be set in the namelist :ref:`nam_pert_pre` or sometimes can be modified directly in the subroutine :file:`set_perturb.f90`.

* :code:`LFORCING` : Flag to specify forcing sources. When .TRUE., the precise definition of the forcing is set in the free-format part of :file:`PRE_IDEA1.nam`. LFORCING must be then set to .TRUE. in :file:`EXSEG1.nam` (:ref:`nam_conf`).

* :code:`LSHIFT` : flag to shift altitudes in boundary layer. If LGEOSBAL=TRUE, LSHIFT will be set to FALSE.

* :code:`L2D_ADV_FRC` : flag to activate advecting forcing (2D simulation only). When .TRUE., the precise definition of the advecting forcing is set in the free-format part of :file:`PRE_IDEA1.nam`.

* :code:`L2D_REL_FRC` : flag to activate relaxation forcing (2D simulation only). When .TRUE., the precise definition of the relaxation forcing is set in the free-format part of :file:`PRE_IDEA1.nam`.

* :code:`NHALO` : Size of the halo for parallel distribution. This variable is related to computer performance but has no impact on simulation results.

* :code:`JPHEXT` : Horizontal External points number JPHEXT must be equal to 3 for cyclic cases with WENO5.

* :code:`LOCEAN` : flag to activate the Ocean version of Meso-NH. Pronostic variables are: Current (U and V), Vertical velocity (W), Temperature (TH), Subgrid Turbulent Kinetic Energy (TKE). Salinity (RV) can be activated with LUSERV=T. The Z-axis is directed upward (as in the atmosphere version), i.e. top of model domain corresponds to the sea surface. The initial profile must be defined in the :ref:`freeformat_prep_ideal_case`.
