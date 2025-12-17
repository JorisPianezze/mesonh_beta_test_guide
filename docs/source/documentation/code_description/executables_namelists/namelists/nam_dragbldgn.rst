.. _nam_dragbldgn:

NAM_DRAGBLDGn
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

This namelist allows to couple the Town Energy Balance (SURFEX-TEB) at multiple levels with Meso-NH :cite:`schoetter_multi-layer_2020`. LDRAGBLDG activates the drag force due to buildings at grid points and model levels intersecting the buildings. The prognostic (U,V) wind componentes are reduced, the prognostic subgrid TKE is increased due to the turbulence produced by the wind shear close to the buildings. LFLUXBLDG additionally activates the release of heat and moisture fluxes from buildings at grid points and model levels intersecting the buildings. Otherwise, these fluxes are released at the surface. LDRAGURBVEG activates the drag force due to urban trees at grid points and model levels intersecting the trees. The prognostic (U,V) wind components are reduced, for the prognostic subgrid TKE there is a production term due to the wind shear close to the trees, and a dissipation term representing turbulence destruction by leaves.

When building drag is activated, the roughness length of the urban areas should be reduced to avoid a double counting of building drag via the drag force and the high surface roughness.

Furthermore, for multi-layer coupling, the number of atmospheric model levels sent to SURFEX (NLEV_COUPLE) needs to be specified in :ref:`nam_coupling_levelsn` such that all model levels intersecting the buildings are coupled with SURFEX.

.. csv-table:: NAM_DRAGBLDGn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LDRAGBLDG","LOGICAL","FALSE"
   "LFLUXBLDG","LOGICAL","FALSE"
   "LDRAGURBVEG","LOGICAL","FALSE"

* :code:`LDRAGBLDG` : flag to activate drag of buildings

* :code:`LFLUXBLDG` : flag to activate release of heat and moisture from buildings at model levels instead of the surface

* :code:`LDRAGURBVEG` : flag to activate drag of urban vegetation
