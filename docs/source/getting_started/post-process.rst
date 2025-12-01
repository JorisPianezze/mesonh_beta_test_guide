Post-process and vizualize
================================================

http://mesonh.aero.obs-mip.fr/mesonh57/graphic

.. error::

   Ne conserver que ?
    
   * MNHPy

   * Epygram


ncview
------------------------------------------------

.. warning::

   If your netCDF files are compressed with the Zstandard compression library (by default since Meso-NH 6.0), your environment must be adapted to support them.
   The easiest way is to load the MesoNH environment in the shell used to start :file:`ncview`. You can do this by running the command: :code:`. MY_MESONH_DIRECTORY/conf/profile_mesonh`.


panoply
------------------------------------------------

.. warning::

   If your netCDF files are compressed with the Zstandard compression library (by default since Meso-NH 6.0), you need to satisfy several conditions to be able to read them:

   * The minimum supported version of :file:`panoply` is the 5.7.0.

   * You need to change the preferences in :file:`panoply`: in the "Files" section, check "Use nj22Config.xml file to load netCDF-C library".

   * Next, you need to create the file ~/.unidata/nj22Config.xml with:

     .. code-block:: xml

        <nj22Config>
           <Netcdf4Clibrary>
              <libraryPath>$NETCDFC_LIB_PATH</libraryPath>
              <libraryName>netcdf</libraryName>
              <useForReading>true</useForReading>
           </Netcdf4Clibrary>
        </nj22Config>

   * Finally, set the :code:`NETCDFC_LIB_PATH` to point to the installation of the netCDF-C library from Meso-NH (e.g. :code:`export NETCDFC_LIB_PATH=MY_MESONH_DIRECTORY/src/dir_obj$XYZ/MASTER/NETCDF-4.6.1/lib/`).
