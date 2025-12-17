.. _nam_diag_aerosols:

NAM_DIAG - Aerosols
-----------------------------------------------------------------------------

* ORILAM (Only available if LUSECHEM=T and LORILAM=T in YINIFILE.des.), add :code:`LCHEMDIAG=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "SOAI...", "Aerosol scalar variable as defined in ch_aer_init_soa.f90 (ppb)", "3D"
   "RGAn", "Aerosol number mean Radius of the lognormal mode n (:math:`mu` m)", "3D"
   "RGAMn", "Aerosol Mass mean Radius of the lognormal mode n (:math:`mu` m)", "3D"
   "N0An", "Aerosol Number of the lognormal mode n (/cc)", "3D"
   "SIGAn", "Aerosol Standard deviation of the lognormal mode n (-)", "3D"
   "MSO4n", "Mass SO4 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MNO3n", "Mass NO3 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MNH3n", "Mass NH3 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MH2On", "Mass H2O aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA1n", "Mass SOA1 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA2n", "Mass SOA2 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA3n", "Mass SOA3 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA4n", "Mass SOA4 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA5n", "Mass SOA5 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA6n", "Mass SOA6 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA7n", "Mass SOA7 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA8n", "Mass SOA8 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA9n", "Mass SOA9 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MSOA10n:", "Mass SOA10 aerosol mode n (:math:`mu` m/m3)", "3D"
   "MOCn", "Mass OC aerosol mode n (:math:`mu` m/m3)", "3D"
   "MBCn", "Mass BC aerosol mode n (:math:`mu` m/m3", "3D"

  
* Dust (Only available if LDUST=T in YINIFILE.des.)

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "DSTM0n", "Dust 0-order moment of the lognormal mode n (ppb)", "3D"
   "DSTM3n", "Dust 3rd-order moment of the lognormal mode n (ppb)", "3D"
   "DSTM6n", "Dust 6rd-order moment of mode n (if LVARSIG) (ppb)", "3D"
   "DSTRGAn", "Dust number mean Radius of the lognormal mode n (:math:`mu` m)", "3D"
   "DSTRGAMn", "Dust Mass mean Radius of the lognormal mode n (:math:`mu` m)", "3D"
   "DSTN0An", "Dust Number of the lognormal mode n (/m3)", "3D"
   "DSTSIGAn", "Dust Standard deviation of the lognormal mode n (-)", "3D"
   "DSTMSSn", "Dust Mass concentration of the lognormal mode n (:math:`mu` g/m3)", "3D"
   "DSTBRDNn", "Dust Burden of the lognormal mode n (g/m2)", "2D"
   "DEDSTM3nC", "Dust Mass of mode n in cloud water only if LDEPOS_DST (ppb)", "3D"
   "DEDSTM3nR", "Dust Mass of mode n in rain only if LDEPOS_DST=T (ppb)", "3D"
   "DEDSTN0An", "Number of dust particles in cloud water (for n=1,2,3) or in rain (for n=4,5,6) only if LDEPOS_DST=T (/m3)", "3D"
   "DEDSTMSSn", "Dust mass in cloud water (for n=1,2,3) or in rain (for n=4,5,6) only if LDEPOS_DST=T(:math:`mu` g/m3)", "3D"
   "DSTAOD2D", "Dust Optical Depth (-) if NRAD_3D :math:`geq` 1 in :ref:`nam_diag_radiation`", "2D"
   "DSTAOD3D", "Dust Optical Depth between two vertical levels (-) if NRAD_3D :math:`geq` 1 in :ref:`nam_diag_radiation`", "3D"
   "DSTEXT", "Dust Extinction (1/km) if NRAD_3D :math:`geq` 1 in :ref:`nam_diag_radiation`", "3D"

* Salt (Only available if LSALT=T in YINIFILE.des.)

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "SLTM0n", "Salt 0-order moment of the lognormal mode n (ppb)", "3D"
   "SLTM3n", "Salt 3rd-order moment of the lognormal mode n (ppb)", "3D"
   "SLTM6n", "Salt 6rd-order moment of mode n (if LVARSIG_SLT) (ppb)", "3D"
   "SLTRGAn", "Salt number mean Radius of the lognormal mode n (:math:`mu` m)", "3D"
   "SLTRGAMn", "Salt Mass mean Radius of the lognormal mode n (:math:`mu` m)", "3D"
   "SLTN0An", "Salt Number of the lognormal mode n (/m3)", "3D"
   "SLTSIGAn", "Salt Standard deviation of the lognormal mode n (-)", "3D"
   "SLTMSSn", "Salt Mass concentration of the lognormal mode n (:math:`mu` g/m3)", "3D"
   "SLTBRDNn", "Salt Burden of the lognormal mode n (g/m2)", "2D"
   "DESLTM3nC", "Salt Mass of mode n in cloud water only if LDEPOS_SLT=T (ppb)", "3D"
   "DESLTM3nR", "Salt Mass of mode n in rain only if LDEPOS_SLT=T (ppb)", "3D"
   "DESLTN0An", "Number of salt particles in cloud water (for n=1,2,3) or in rain (for n=4,5,6) only if LDEPOS_SLT=T (/m3)", "3D"
   "DESLTMSSn", "Salt mass in cloud water (for n=1,2,3) or in rain (for n=4,5,6) only if LDEPOS_SLT=T (:math:`mu` g/m3)", "3D"
   "SLTAOD2D", "Salt Optical Depth (-) if NRAD_3D :math:`geq` 1 in :ref:`nam_diag_radiation`", "2D"
   "SLTAOD3D", "Salt Optical Depth between two vertical levels (_) if NRAD_3D :math:`geq` 1 in :ref:`nam_diag_radiation`", "3D"
   "SLTEXT", "Salt Extinction (1/km) if NRAD_3D :math:`geq` 1 in :ref:`nam_diag_radiation`", "3D"
