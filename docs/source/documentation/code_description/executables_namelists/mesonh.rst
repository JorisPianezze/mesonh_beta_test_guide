.. _mesonh:

MESONH
***************************************************************************** 

The :program:`MESONH` user will specify some free parameters of the run by fixing their new values in the namelists of the file :file:`EXSEG$n.nam`.
When more than one model is present, each model needs its own Meso-NH file to be initialized and its own :file:`EXSEG$n.nam` file to fix the free-parameters (note that a lot of physical free-parameters depends on the mesh and therefore vary with the model number). The input files are read by the program in order to realize the initialization and the eventual coupling of the MESONH model with a large-scale model (ECMWF, ARPEGE, AROME, GFS). The output files are of two types:

* synchronous files for a given instant of the run. They contain the prognostic fields and eventually, additional records for supplementary diagnostic fields at the same instant. The file name ends by 00n with n>0

* a diachronic file for the temporal series of prognostic or diagnostic fields. The file name ends by 000.

.. csv-table:: MESONH program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "MESONH", "EXSEG1.nam", "Launch simulation"

The following namelists can be used in the :file:`EXSEG1.nam` file :

* :ref:`nam_2d_frc`
* :ref:`nam_advn`
* :ref:`nam_aircrafts`
* :ref:`nam_backup`
* :ref:`nam_balloons`
* :ref:`nam_blankn`
* :ref:`nam_blowsnow`
* :ref:`nam_blowsnown`  
* :ref:`nam_budget`
* :ref:`nam_bu_rrc`
* :ref:`nam_bu_rrg`
* :ref:`nam_bu_rrh`
* :ref:`nam_bu_rri`
* :ref:`nam_bu_rrr`
* :ref:`nam_bu_rrs`
* :ref:`nam_bu_rrv`
* :ref:`nam_bu_rsv`
* :ref:`nam_bu_rth`
* :ref:`nam_bu_rtke`
* :ref:`nam_bu_ru`
* :ref:`nam_bu_rv`
* :ref:`nam_bu_rw`
* :ref:`nam_ch_mnhcn`
* :ref:`nam_ch_orilam`
* :ref:`nam_ch_solvern`
* :ref:`nam_condsamp`
* :ref:`nam_conf`
* :ref:`nam_confio`
* :ref:`nam_confn`
* :ref:`nam_confz`
* :ref:`nam_dragn`
* :ref:`nam_dragtreen`
* :ref:`nam_dragbldgn`
* :ref:`nam_coupling_levelsn`
* :ref:`nam_dust`
* :ref:`nam_dyn`
* :ref:`nam_dynn`
* :ref:`nam_firen`
* :ref:`nam_flyers`                 
* :ref:`nam_latz_edflx`
* :ref:`nam_elec`
* :ref:`nam_eol`
* :ref:`nam_eol_adnr`
* :ref:`nam_eol_adr`
* :ref:`nam_eol_alm`
* :ref:`nam_frc`
* :ref:`nam_ibm_paramn`
* :ref:`nam_lbcn`
* :ref:`nam_les`
* :ref:`nam_lunitn`
* :ref:`nam_mean`
* :ref:`nam_nebn`
* :ref:`nam_nesting`
* :ref:`nam_nudgingn`
* :ref:`nam_output`
* :ref:`nam_paramn`
* :ref:`nam_param_c2r2`
* :ref:`nam_param_ecradn`
* :ref:`nam_param_icen`
* :ref:`nam_param_kafrn`
* :ref:`nam_param_lima`
* :ref:`nam_param_mfshalln`
* :ref:`nam_param_radn`
* :ref:`nam_paspol`
* :ref:`nam_pdf`
* :ref:`nam_profilern`
* :ref:`nam_recycl_paramn`
* :ref:`nam_salt`
* :ref:`nam_series`
* :ref:`nam_seriesn`
* :ref:`nam_stationn`
* :ref:`nam_turbn`
* :ref:`nam_visc`
* :ref:`nam_sso`
* :ref:`nam_surf_csts`
* :ref:`nam_surf_atm`
* :ref:`nam_write_surf_atm`
* :ref:`nam_seafluxn`
* :ref:`nam_surf_slt`
* :ref:`nam_watfluxn`
* :ref:`nam_flaken`
* :ref:`nam_isban`
* :ref:`nam_surf_dst`
* :ref:`nam_ideal_flux`
* :ref:`nam_tebn`
* :ref:`nam_ch_controln`
* :ref:`nam_ch_surfn`
* :ref:`nam_ch_seafluxn`
* :ref:`nam_ch_watfluxn`
* :ref:`nam_ch_tebn`
* :ref:`nam_ch_isban`
* :ref:`nam_chs_orilam`
* :ref:`nam_diag_surf_atmn`
* :ref:`nam_write_diag_surfn`
* :ref:`nam_diag_surfn`
* :ref:`nam_diag_isban`
* :ref:`nam_diag_tebn`
* :ref:`nam_diag_flaken`
* :ref:`nam_diag_oceann`
 

.. include:: namelists/nam_2d_frc.rst
.. include:: namelists/nam_advn.rst
.. include:: namelists/nam_aircrafts.rst
.. include:: namelists/nam_backup.rst
.. include:: namelists/nam_balloons.rst
.. include:: namelists/nam_blankn.rst
.. include:: namelists/nam_blowsnow.rst
.. include:: namelists/nam_blowsnown.rst  
.. include:: namelists/nam_budget.rst
.. include:: namelists/nam_bu_rrc.rst
.. include:: namelists/nam_bu_rrg.rst
.. include:: namelists/nam_bu_rrh.rst
.. include:: namelists/nam_bu_rri.rst
.. include:: namelists/nam_bu_rrr.rst
.. include:: namelists/nam_bu_rrs.rst
.. include:: namelists/nam_bu_rrv.rst
.. include:: namelists/nam_bu_rsv.rst
.. include:: namelists/nam_bu_rth.rst
.. include:: namelists/nam_bu_rtke.rst
.. include:: namelists/nam_bu_ru.rst
.. include:: namelists/nam_bu_rv.rst
.. include:: namelists/nam_bu_rw.rst
.. include:: namelists/nam_ch_mnhcn.rst
.. include:: namelists/nam_ch_orilam.rst
.. include:: namelists/nam_ch_solvern.rst
.. include:: namelists/nam_condsamp.rst
.. include:: namelists/nam_conf.rst
.. include:: namelists/nam_confio.rst
.. include:: namelists/nam_confn.rst
.. include:: namelists/nam_confz.rst
.. include:: namelists/nam_dragn.rst
.. include:: namelists/nam_dragtreen.rst
.. include:: namelists/nam_dragbldgn.rst
.. include:: namelists/nam_coupling_levelsn.rst
.. include:: namelists/nam_dust.rst
.. include:: namelists/nam_dyn.rst
.. include:: namelists/nam_dynn.rst
.. include:: namelists/nam_firen.rst
.. include:: namelists/nam_flyers.rst                 
.. include:: namelists/nam_latz_edflx.rst
.. include:: namelists/nam_elec.rst
.. include:: namelists/nam_eol.rst
.. include:: namelists/nam_eol_adnr.rst
.. include:: namelists/nam_eol_adr.rst
.. include:: namelists/nam_eol_alm.rst
.. include:: namelists/nam_frc.rst
.. include:: namelists/nam_ibm_paramn.rst
.. include:: namelists/nam_lbcn.rst
.. include:: namelists/nam_les.rst
.. include:: namelists/nam_lunitn.rst
.. include:: namelists/nam_mean.rst
.. include:: namelists/nam_nebn.rst
.. include:: namelists/nam_nesting.rst
.. include:: namelists/nam_nudgingn.rst
.. include:: namelists/nam_output.rst
.. include:: namelists/nam_paramn.rst
.. include:: namelists/nam_param_c2r2.rst
.. include:: namelists/nam_param_ecradn.rst
.. include:: namelists/nam_param_icen.rst
.. include:: namelists/nam_param_kafrn.rst
.. include:: namelists/nam_param_lima.rst
.. include:: namelists/nam_param_mfshalln.rst
.. include:: namelists/nam_param_radn.rst
.. include:: namelists/nam_paspol.rst
.. include:: namelists/nam_pdf.rst
.. include:: namelists/nam_profilern.rst
.. include:: namelists/nam_recycl_paramn.rst
.. include:: namelists/nam_salt.rst
.. include:: namelists/nam_series.rst
.. include:: namelists/nam_seriesn.rst
.. include:: namelists/nam_stationn.rst
.. include:: namelists/nam_turbn.rst
.. include:: namelists/nam_visc.rst
.. include:: namelists/nam_sso.rst
.. include:: namelists/nam_surf_csts.rst
.. include:: namelists/nam_surf_atm.rst
.. include:: namelists/nam_write_surf_atm.rst
.. include:: namelists/nam_seafluxn.rst
.. include:: namelists/nam_surf_slt.rst
.. include:: namelists/nam_watfluxn.rst
.. include:: namelists/nam_flaken.rst
.. include:: namelists/nam_isban.rst
.. include:: namelists/nam_surf_dst.rst
.. include:: namelists/nam_ideal_flux.rst
.. include:: namelists/nam_tebn.rst
.. include:: namelists/nam_ch_controln.rst
.. include:: namelists/nam_ch_surfn.rst
.. include:: namelists/nam_ch_seafluxn.rst
.. include:: namelists/nam_ch_watfluxn.rst
.. include:: namelists/nam_ch_tebn.rst
.. include:: namelists/nam_ch_isban.rst
.. include:: namelists/nam_chs_orilam.rst
.. include:: namelists/nam_diag_surf_atmn.rst
.. include:: namelists/nam_write_diag_surfn.rst
.. include:: namelists/nam_diag_surfn.rst
.. include:: namelists/nam_diag_isban.rst
.. include:: namelists/nam_diag_tebn.rst
.. include:: namelists/nam_diag_flaken.rst
.. include:: namelists/nam_diag_oceann.rst


