.. _nam_zs:

NAM_ZS
-----------------------------------------------------------------------------

This namelist defines the orography file and orographic treatment to be done.

.. csv-table:: NAM_ZS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XUNIF_ZS", "REAL", ""
   "YZS", "CHARACTER(LEN=28)", ""
   "YZSFILETYPE", "CHARACTER(LEN=6)", ""
   "COROGTYPE", "CHARACTER(LEN=3)", "'ENV'"
   "XENV", "REAL", "0.0"
   "LIMP_ZS", "LOGICAL", ".FALSE."
   "YSLOPE", "CHARACTER(LEN=28)", ""
   "YSLOPEFILETYPE", "CHARACTER(LEN=6)", "'NETCDF'"
   "LEXPLICIT_SLOPE", "LOGICAL", ".FALSE."
   "LORORAD", "LOGICAL", "F"
   "NSECTORS", "INTEGER", "8"
   "XRFSSO", "REAL", "1.0"
   "XHALORADIUS", "REAL", "20000.0"
   "NFSSOMAX", "INTEGER", "30"
   "CSVF", "CHARACTER(LEN=16)", "MANNERS"
   "LFSSOVF", "LOGICAL", ".FALSE."


* :code:`XUNIF_ZS` : uniform value of orography imposed on all points (real,meters). If XUNIF_ZS is set, file YZS is not used.

* :code:`YZS` : data file name. If XUNIF_ZS is set, file YZS is not used. If neither XUNIF_ZS and YZS is set, then orography is set to zero.

* :code:`YZSFILETYPE` : type of data file

* :code:`COROGTYPE` : type of orography:

  * 'AVG': mean orography Zs.
  * 'ENV': envelope relief, defined from mean orography and the subgrid orography standard deviation as: Zs + XEN V ∗ σ(Zs)
  * 'SIL': silhouette relief, defined as the mean of the two subgrid silhouettes in directions x and y (if two main directions can be defined for the grid chosen).
  * 'MAX': maximum orography over grid box (avoid averaging in case of sea/land grid box).
  
* :code:`XENV` : enhance factor in envelope orography definition (real).

* :code:`LIMP_ZS` : reads orography from an existing PGD file

* :code:`YSLOPE` : file name for slope

* :code:`YSLOPEFILETYPE` : data file type for slope

* :code:`LEXPLICIT_SLOPE` : Slope is computed from explicit ZS field and not subgrid orography

* :code:`LORORAD` : flag to activate orographic radiation parameters in PGD step. New fields are created in the PGD and used in the simulation if orographic shadowing is activated (with LDSV, LDSL or LDSH)

* :code:`NSECTORS` : number of aspect sectors

* :code:`XRFSSO` : reduction factor for computing NFSSO

* :code:`XHALORADIUS` : radius of the halo in which the horizon is computed (m)

* :code:`NFSSOMAX` : max for NFSSO (limit for memory reasons)

* :code:`CSVF` : formula for SVF computation

  * 'SENKOVA' = Senkova et al. 2007
  * 'MANNERS' = Manners et al. 2012 (default)
  
* :code:`LFSSOVF` : compute SVF (sky view factor) on fractional slopes if possible
