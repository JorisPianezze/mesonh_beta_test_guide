Extract CAMS's data
============================================


Registration
--------------------------------------------

Access to ADS data is restricted to registred users. See `ADS's website <https://ads.atmosphere.copernicus.eu/#!/home>`_ for more detailed informations. 

.. _configure_ads_api_key:

.. note::

   You need to accept the licence to use CAMS products `here <https://ads.atmosphere.copernicus.eu/datasets/cams-global-reanalysis-eac4?tab=download#manage-licences>`_.

Configure
--------------------------------------------

Once your account create, you need to configure CDS API following https://ads.atmosphere.copernicus.eu/how-to-api instructions.

.. warning::

   I recommend to create a file called `.adsapirc` and not `.cdsapirc` because you can have conflict with CDS API key if you also extract ERA5 data from CDS server.

First you need to create a file called `.adsapirc` in your HOME directory. Your `.adsapirc` file needs to contain lines that look likes:

.. code-block:: bash

   url: https://ads.atmosphere.copernicus.eu/api
   key: your_key

.. note::

   To fill this file go to https://ads.atmosphere.copernicus.eu/how-to-api.

.. warning::

   You need to suppress rules for group and other users with ``chmod 600 .adsapirc``.

.. _install_python_cdsapi:

Installation
--------------------------------------------

You can install CDS API required to extract CAMS data using following conda command in your conda environment, do

.. code-block:: console

   conda install cdsapi>=0.7.2
   
If you want to used a dedicated conda environment you can create an `environment.yml` file containing :

.. code-block:: python
   
   name: env_extract_cdsapi
   channels:
       - conda-forge
   dependencies:
       - cdsapi>=0.7.2
       - eccodes==2.35.0
       - pip==24.0
       - pip:
           - yaml-config==0.1.5

.. note:: 
  
   * This is the last version of cdsapi and yaml-config tested.
   * yaml-config is used to read `.adsapirc` file.
   * eccodes is used to concatenate grib files.   

Then you can create your conda environment with :

.. code-block:: console
 
   conda env create -f environment.yml

Then load new created python environment :

.. code-block:: console
 
   conda activate env_extract_cdsapi


Example
--------------------------------------------

To extract CAMS data from example script, you have to :
* create a script called `your_script.sh` with the following code
* and adapt the path for file `.adsapirc` inside this script

.. code-block:: bash

   #!/bin/bash

   # AREA = 'Norht, West, South, East'
   export AREA='20, -20, -60, 80'

   export YEAR='2019'
   export MONTH='03'

   for DAY in  '09' #  '10' '11' '12' '13' '14' '15' 
   do
   for HOUR in  '00' # '06' '12' '18'
   do

   echo '--> Extacting date : ' ${YEAR}${MONTH}${DAY}_${HOUR}

   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   #   Create request file
   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   cat > request_CAMS_${YEAR}${MONTH}${DAY}_${HOUR}.py << EOF

   import cdsapi
   import yaml

   with open('/path/to/your/.adsapirc', 'r') as f: credentials = yaml.safe_load(f)

   c = cdsapi.Client(url=credentials['url'], key=credentials['key'])

   c.retrieve(
       'cams-global-reanalysis-eac4',
       {
           'date'     : '${YEAR}-${MONTH}-${DAY}/${YEAR}-${MONTH}-${DAY}',
           'format'   : 'netcdf',
           'variable' : [
               'acetone', 'acetone_product', 'aldehydes',
               'amine', 'ammonia', 'ammonium',
               'carbon_monoxide', 'dimethyl_sulfide', 'dinitrogen_pentoxide',
               'dust_aerosol_0.03-0.55um_mixing_ratio', 'dust_aerosol_0.55-0.9um_mixing_ratio', 'dust_aerosol_0.9-20um_mixing_ratio',
               'ethane', 'ethanol', 'ethene',
               'formaldehyde', 'formic_acid', 'hydrogen_peroxide',
               'hydroperoxy_radical', 'hydrophilic_black_carbon_aerosol_mixing_ratio', 'hydrophilic_organic_matter_aerosol_mixing_ratio',
               'hydrophobic_black_carbon_aerosol_mixing_ratio', 'hydrophobic_organic_matter_aerosol_mixing_ratio', 'hydroxyl_radical',
               'isoprene', 'methacrolein_mvk', 'methacrylic_acid',
               'methane_sulfonic_acid', 'methanol', 'methyl_glyoxal',
               'methyl_peroxide', 'methylperoxy_radical', 'nitrate',
               'nitrate_radical', 'nitric_acid', 'nitrogen_dioxide',
               'nitrogen_monoxide', 'olefins', 'organic_ethers',
               'organic_nitrates', 'ozone', 'paraffins',
               'pernitric_acid', 'peroxides', 'peroxy_acetyl_radical',
               'peroxyacetyl_nitrate', 'propane', 'propene',
               'sea_salt_aerosol_0.03-0.5um_mixing_ratio', 'sea_salt_aerosol_0.5-5um_mixing_ratio', 'sea_salt_aerosol_5-20um_mixing_ratio',
               'specific_humidity', 'sulphate_aerosol_mixing_ratio', 'sulphur_dioxide',
               'surface_pressure', 'temperature', 'terpenes',
           ],
           'model_level' : [
               '1', '2', '3',
               '4', '5', '6',
               '7', '8', '9',
               '10', '11', '12',
               '13', '14', '15',
               '16', '17', '18',
               '19', '20', '21',
               '22', '23', '24',
               '25', '26', '27',
               '28', '29', '30',
               '31', '32', '33',
               '34', '35', '36',
               '37', '38', '39',
               '40', '41', '42',
               '43', '44', '45',
               '46', '47', '48',
               '49', '50', '51',
               '52', '53', '54',
               '55', '56', '57',
               '58', '59', '60',
           ],
           'time': '${HOUR}:00',
           'area': [${AREA},
           ],
       },
       'download.nc')
   EOF

   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   #   Send request
   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   python request_CAMS_${YEAR}${MONTH}${DAY}_${HOUR}.py

   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   #   Unzip, concatenate and remove tmp files
   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   unzip download.nc
   ncks -A data_sfc.nc data_mlev.nc
   mv data_mlev.nc CAMS_${YEAR}${MONTH}${DAY}_${HOUR}.nc
   rm -f data_sfc.nc download.nc
 
   done
   done

.. note::

   You need to have ncks installed.

Then, you can launch the extraction with :

.. code-block:: bash

   ./your_script.sh

.. note::

   * At the end of the extraction you need to have files called `CAMS_${YEAR}${MONTH}${DAY}_${HOUR}.nc` !
   * Once the example script works, you can adapt the area and the date to your case.
