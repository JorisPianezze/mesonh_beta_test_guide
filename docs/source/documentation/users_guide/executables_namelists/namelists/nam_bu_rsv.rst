.. _nam_bu_rsv:

NAM_BU_RSV
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RSV content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RSV", "LOGICAL", ".FALSE."
   "CBULIST_RSV", "ARRAY(CHARACTER)", ""

* :code:`LBU_RSV` : flag to activate budget for scalar variable

* :code:`CBULIST_RSV` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RSV array and the conditions of their availability:
   
General source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ALL","all available source terms (separated, water microphysics included)","no condition"
   "ASSE","time filter (Asselin)","no condition"
   "NEST","nesting","NMODEL>1"
   "VISC","viscosity","LVISC=T and LVISC_SV=T"
   "ADV","total advection","no condition"
   "FRC","forcing","LFORCING=T"
   "DIF","numerical diffusion","LNUMDIFSV=T"
   "REL","relaxation","LHORELAX_SV(jsv)=T or corresponding LHOREAX_SV*=T or (CELEC/='NONE' and LRELAX2FW_ION=T and (jsv=NSV_ELECBEG or jsv=NSV_ELECEND) )"
   "DCONV","KAFR convection","CDCONV='KAFR' or CSCONV='KAFR'"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"
   "MAFL","mass flux","CSCONV='EDKF'"
   "NEGA2","negativity correction","no condition"

with jsv the scalar variable number.

C2R2 / KHKO source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Common source terms for C2R2 / KHKO :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NEGA","negativity correction","no condition"
   "NECON","negativity correction induced by condensation","no condition"

* Concentration of activated nuclei for C2R2 / KHKO :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HENU","CCN activation","LSUPSAT=F or (CACTCCN='ABRK' and (LORILAM=T or LDUST=T or LSALT=T))"
   "CEVA","evaporation","no condition"

* Concentration of cloud droplets for C2R2 / KHKO :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "DEPOTR","tree droplet deposition","LDRAGTREE=T and LDEPOTREE=T"
   "HENU","CCN activation","LSUPSAT=F or (CACTCCN='ABRK' and (LORILAM=T or LDUST=T or LSALT=T))"
   "SELF","self-collection of cloud droplets","NMOM_R>=1"
   "ACCR","accretion of cloud droplets","NMOM_R>=1"
   "SEDI","sedimentation","LSEDC=T"
   "DEPO","surface droplet deposition","LDEPOC=T"
   "CEVA","evaporation","no condition"

* Concentration of raindrops for C2R2 / KHKO :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "AUTO","autoconversion into rain","NMOM_R>=1"
   "SCBU","self collection - coalescence/break-up","CCLOUD/='KHKO'"
   "REVA","rain evaporation","NMOM_R>=1"
   "BRKU","spontaneous break-up","NMOM_R>=1"
   "SEDI","sedimentation","no condition"

* Supersaturation for C2R2 / KHKO :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "CEVA","evaporation","no condition"

LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Common source terms for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NEGA","negativity correction","no condition"
   "NECON","negativity correction induced by condensation","no condition"

* Concentration of cloud droplets for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "DEPOTR","tree droplet deposition","LDRAGTREE=T and LDEPOTREE=T"
   "SEDI","sedimentation of cloud","NMOM_C>=1 and LSEDC=T"
   "DEPO","surface droplet deposition","NMOM_C>=1 and LDEPOC=T"
   "R2C1","rain to cloud change after sedimentation","LPTSPLIT=T and NMOM_C>=1 and NMOM_R>=1"
   "HENU","CCN activation","NMOM_C>=1 and LACTI=T and NMOD_CCN>0 and (LPTSPLIT=F or LSUBG_COND=F)"
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T"
   "SELF","self-collection of cloud droplets","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "AUTO","autoconversion into rain","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "ACCR","accretion of cloud droplets","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "REVA","evaporation of rain drops","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "HONC","droplet homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T)"
   "IMLT","melting of ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "RIM","riming of cloud water","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CVRC","rain to cloud change after other microphysical processes","LPTSPLIT=T"
   "WETH","wet growth of hail","LPTSPLIT=T or NMOM_H>=1"
   "CEDS","adjustment to saturation","NMOM_C>=1"
   "CORR2","supplementary correction inside LIMA splitting","LPTSPLIT=T"

* Concentration of raindrops for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation","NMOM_C>=1 and NMOM_R>=1"
   "R2C1","rain to cloud change after sedimentation","LPTSPLIT=T and NMOM_C>=1 and NMOM_R>=1"
   "AUTO","autoconversion into rain","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "SCBU","self collection - coalescence/break-up","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "REVA","rain evaporation","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "BRKU","spontaneous break-up","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "HONR","rain homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_R>=1 and LNUCL=T)"
   "ACC","accretion of rain on aggregates","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and NMOM_R>=1)"
   "CFRZ","conversion freezing of rain","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "GMLT","graupel melting","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CVRC","rain to cloud change after other microphysical processes","LPTSPLIT=T"
   "WETH","wet growth of hail","LPTSPLIT=T or NMOM_H>=1"
   "HMLT","melting of hail","LPTSPLIT=T or NMOM_H>=1"
   "CORR2","supplementary correction inside LIMA splitting","LPTSPLIT=T"

* Concentration of free CCN for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HENU","CCN activation","NMOM_C>=1 and LACTI=T and NMOD_CCN>0 and (LPTSPLIT=F or LSUBG_COND=F)"
   "HONH","haze homogeneous nucleation","NMOM_I>=1 and LNUCL=T and LHHONI=T and NMOD_CCN>0"
   "CEDS","adjustment to saturation","NMOM_C>=1"
   "SCAV","scavenging","LSCAV=T"

* Concentration of activated CCN for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HENU","CCN activation","NMOM_C>=1 and LACTI=T and NMOD_CCN>0 and (LPTSPLIT=F or LSUBG_COND=F)"
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T and LMEYERS=F"
   "CEDS","adjustment to saturation","NMOM_C>=1"

* Scavenged mass variable for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SCAV","scavenging","LSCAV=T and LAERO_MASS=T"
   "CEDS","adjustment to saturation","LSCAV=T and LAERO_MASS=T and LSPRO=F"

* Concentration of pristine ice crystals for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation","NMOM_I>=1 and LSEDI=T"
   "HIND","heterogeneous nucleation by deposition","NMOM_I>=1 and LNUCL=T"
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T"
   "HONH","haze homogeneous nucleation","NMOM_I>=1 and LNUCL=T and LHHONI=T and NMOD_CCN>0"
   "HONC","droplet homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T)"
   "CNVI","conversion of snow to cloud ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "CNVS","conversion of pristine ice to snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "AGGS","aggregation of snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "IMLT","melting of ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "HMS","Hallett-Mossop ice multiplication process due to snow riming","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CIBU","ice multiplication process due to ice collisional breakup","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and LCIBU=T)"
   "CFRZ","conversion freezing of rain","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "RDSF","ice multiplication process following rain contact freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and LRDSF=T)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "HMG","Hallett-Mossop ice multiplication process due to graupel riming","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETH","wet growth of hail","LPTSPLIT=T or NMOM_H>=1"
   "CEDS","adjustment to saturation","LPTSPLIT=F and LSPRO=F"
   "CORR2","supplementary correction inside LIMA splitting","LPTSPLIT=T"

* Concentration of snow for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation","NMOM_S>=2"
   "CNVI","conversion of snow to cloud ice","NMOM_S>=2"
   "CNVS","conversion of pristine ice to snow","NMOM_S>=2"
   "BRKU","break up of snow","NMOM_S>=2"
   "RIM","heavy riming of cloud droplet on snow","NMOM_S>=2"
   "ACC","accretion of rain on snow","NMOM_S>=2"
   "CMEL","conversion melting of snow","NMOM_S>=2"
   "WETG","wet growth of graupel","NMOM_S>=2"
   "DRYG","dry growth of graupel","NMOM_S>=2"
   "WETH","wet growth of hail","NMOM_S>=2"
   "SSC","snow self collection","NMOM_S>=2"
   "CEDS","adjustment to saturation","LPTSPLIT=F and NMOM_I>=1 and LSPRO=F"

* Concentration of graupel for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation","NMOM_G>=2"
   "RIM","heavy riming of cloud droplet on snow","NMOM_G>=2"
   "ACC","accretion of rain on snow","NMOM_G>=2"
   "CMEL","conversion melting of snow","NMOM_G>=2"
   "CFRZ","conversion freezing of raindrop","NMOM_G>=2"
   "WETG","wet growth of graupel","NMOM_G>=2"
   "GMLT","raupel melting","NMOM_G>=2"
   "WETH","wet growth of hail","NMOM_G>=2"
   "COHG","conversion hail graupel","NMOM_G>=2"
   "CEDS","adjustment to saturation","LPTSPLIT=F and NMOM_I>=1 and LSPRO=F"

* Concentration of hail for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation","NMOM_H>=2"
   "WETG","wet growth of graupel","NMOM_H>=2"
   "COHG","conversion hail graupel","NMOM_H>=2"
   "HMLT","hail melting","NMOM_H>=2"

* Concentration of free IFN for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HIND","heterogeneous nucleation by deposition","NMOM_I>=1 and LNUCL=T and LMEYERS=F"
   "CEDS","adjustment to saturation","NMOM_I>=1 and LPTSPLIT=F and LSPRO=F"
   "SCAV","scavenging","LSCAV=T"

* Concentration of nucleated IFN for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HIND","heterogeneous nucleation by deposition","NMOM_I>=1 and LNUCL=T and (LMEYERS=F or jsv=NSV_LIMA_IFN_NUCL)"
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T and LMEYERS=T and jsv=NSV_LIMA_IFN_NUCL"
   "IMLT","melting of ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "CEDS","adjustment to saturation","NMOM_I>=1 and LPTSPLIT=F and LSPRO=F"

with jsv the scalar variable number.

* Concentration of nucleated IMM for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T and LMEYERS=F"
   "CEDS","adjustment to saturation","NMOM_I>=1 and LPTSPLIT=F and LSPRO=F"

* Homogeneous freezing of CCN for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HONH","haze homogeneous nucleation","NMOM_I>=1 and LNUCL=T and ( (LHHONI=T and NMOD_CCN>0) or (LPTSPLIT=F and NMOM_C>=1) )"

* Supersaturation for LIMA :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "CEDS","adjustment to saturation","no condition"

Electricity source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Common source terms for electricity :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NEGA","negativity correction","no condition"
   "NECON","negativity correction induced by condensation","no condition"


* Positive ions :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30

   "DRIFT","ion drift motion","no condition"
   "CORAY","cosmic ray source","no condition"
   "ADJU","adjustement to saturation","CCLOUD(1:3)='ICE' and LRED=T and LADJ_BEFORE"
   "DEPS","deposition on snow","no condition"
   "DEPG","deposition on graupel","no condition"
   "REVA","rain evaporation","NMOM_C>=1"
   "DEPI","condensation/deposition on ice","CCLOUD(1:3)='ICE' and (LRED=F or LADJ_AFTER)"
   "CEDS","adjustement to saturation","CCLOUD='LIMA'"
   "NEUT","neutralization","no condition"
   "SUBI","sublimation of ice crystals","CCLOUD='LIMA' and LPTSPLIT=T"
   "CORR2","supplementary correction inside LIMA splitting","CCLOUD='LIMA' and LPTSPLIT=T"

* Volumetric charge of cloud droplets :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30

   "ADJU","adjustement to saturation","CCLOUD(1:3)='ICE' and LRED=T and LADJ_BEFORE"
   "HON","homogeneous nucleation","no condition"
   "AUTO","autoconversion into rain","NMOM_C>=1"
   "ACCR","accretion of cloud droplets","NMOM_C>=1"
   "RIM","riming of cloud water","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "INCG","inductive charge transfer between cloud droplets and graupel","LINDUCTIVE=T"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "IMLT","melting of ice","no condition"
   "BERFI","Bergeron-Findeisen","no condition"
   "SEDI","sedimentation","LSEDIC=T"
   "DEPI","condensation/deposition on ice","CCLOUD(1:3)='ICE' and (LRED=F or LADJ_AFTER)"
   "CEDS","adjustement to saturation","CCLOUD='LIMA'"
   "NEUT","neutralization","no condition"
   "R2C1","rain to cloud change after sedimentation","CCLOUD='LIMA' and LPTSPLIT=T and NMOM_C>=1 NMOM_R>=1"
   "CORR2","supplementary correction inside LIMA splitting","CCLOUD='LIMA' and LPTSPLIT=T"
   "CMEL","collection by snow and conversion into rain with T>XTT on ice","CCLOUD(1:3)='ICE' and LRED=T"

* Volumetric charge of rain drops :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SFR","spontaneous freezing","no condition"
   "AUTO","autoconversion into rain","NMOM_C>=1"
   "ACCR","accretion of cloud droplets","NMOM_C>=1"
   "REVA","rain evaporation","NMOM_C>=1"
   "ACC","accretion of rain on aggregates","no condition"
   "CFRZ","conversion freezing of rain","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "GMLT","graupel melting","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "HMLT","melting of hail","CCLOUD='ICE4'"
   "SEDI","sedimentation","no condition"
   "NEUT","neutralization","no condition"
   "R2C1","rain to cloud change after sedimentation","CCLOUD='LIMA' and LPTSPLIT=T and NMOM_C>=1 NMOM_R>=1"
   "CORR2","supplementary correction inside LIMA splitting","CCLOUD='LIMA' and LPTSPLIT=T"
   "CMEL","collection by snow and conversion into rain with T>XTT on ice","CCLOUD(1:3)='ICE' and LRED=T"
   "RDSF","raindrop shattering by freezing","CCLOUD='LIMA' and LPTSPLIT=T and LRDSF=T"

* Volumetric charge of ice crystals :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ADJU","adjustement to saturation","CCLOUD(1:3)='ICE' and LRED=T and LADJ_BEFORE"
   "HON","homogeneous nucleation","no condition"
   "AGGS","aggregation of snow","no condition"
   "AUTS","autoconversion of ice","no condition"
   "CFRZ","conversion freezing of rain","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "IMLT","melting of ice","no condition"
   "BERFI","Bergeron-Findeisen","no condition"
   "NIIS","non-inductive charge separation due to ice-snow collisions","no condition"
   "NIIG","non-inductive charge separation due to ice-graupel collisions","no condition"
   "SEDI","sedimentation","no condition"
   "DEPI","condensation/deposition on ice","CCLOUD(1:3)='ICE' and (LRED=F or LADJ_AFTER)"
   "CEDS","adjustement to saturation","CCLOUD='LIMA'"
   "NEUT","neutralization","no condition"
   "CNVI","conversion of snow to cloud ice","CCLOUD='LIMA' and LPTSPLIT=T"
   "SUBI","sublimation of ice crystals","CCLOUD='LIMA' and LPTSPLIT=T"
   "HMS","Hallett-Mossop ice multiplication process due to snow riming","CCLOUD='LIMA' and LPTSPLIT=T"
   "HMG","Hallett-Mossop ice multiplication process due to graupel riming","CCLOUD='LIMA' and LPTSPLIT=T"
   "CIBU","collisional ice breakup","CCLOUD='LIMA' and LPTSPLIT=T and LCIBU=T"
   "RDSF","raindrop shattering by freezing","CCLOUD='LIMA' and LPTSPLIT=T and LRDSF=T"
   "CORR2","supplementary correction inside LIMA splitting","CCLOUD='LIMA' and LPTSPLIT=T"

* Volumetric charge of snow :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "DEPS","deposition on snow","no condition"
   "AGGS","aggregation of snow","no condition"
   "AUTS","autoconversion of ice","no condition"
   "RIM","riming of cloud water","no condition"
   "ACC","accretion of rain on snow","no condition"
   "CMEL","conversion melting","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "NIIS","non-inductive charge separation due to ice-snow collisions","no condition"
   "NISG","non-inductive charge separation due to snow-graupel collisions","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "SEDI","sedimentation","no condition"
   "CNVI","conversion of snow to cloud ice","CCLOUD='LIMA' and LPTSPLIT=T"
   "HMS","Hallett-Mossop ice multiplication process due to snow riming","CCLOUD='LIMA' and LPTSPLIT=T"
   "CIBU","collisional ice breakup","CCLOUD='LIMA' and LPTSPLIT=T and LCIBU=T"
   "NEUT","neutralization","no condition"

* Volumetric charge of graupel :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SFR","spontaneous freezing","no condition"
   "DEPG","deposition on graupel","no condition"
   "RIM","riming of cloud water","no condition"
   "ACC","accretion of rain on graupel","no condition"
   "CMEL","conversion melting","no condition"
   "CFRZ","conversion freezing of rain","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "INCG","inductive charge transfer between cloud droplets and graupel","LINDUCTIVE=T"
   "NIIG","non-inductive charge separation due to ice-graupel collisions","no condition"
   "NISG","non-inductive charge separation due to snow-graupel collisions","no condition"
   "GMLT","graupel melting","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "SEDI","sedimentation","no condition"
   "HMG","Hallett-Mossop ice multiplication process due to graupel riming","CCLOUD='LIMA' and LPTSPLIT=T"
   "NEUT","neutralization","no condition"

* Negative ions :

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "DRIFT","ion drift motion","no condition"
   "CORAY","cosmic ray source","no condition"
   "ADJU","adjustement to saturation","CCLOUD(1:3)='ICE' and LRED=T and LADJ_BEFORE"
   "DEPS","deposition on snow","no condition"
   "DEPG","deposition on graupel","no condition"
   "REVA","rain evaporation","NMOM_C>=1"
   "DEPI","condensation/deposition on ice","CCLOUD(1:3)='ICE' and (LRED=F or LADJ_AFTER)"
   "CEDS","adjustement to saturation","CCLOUD='LIMA'"
   "NEUT","neutralization","no condition"
   "SUBI","sublimation of ice crystals","CCLOUD='LIMA' and LPTSPLIT=T"
   "CORR2","supplementary correction inside LIMA splitting","CCLOUD='LIMA' and LPTSPLIT=T"

Chemistry
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "CHEM","chemistry activity","no condition"
   "NEGA","negativity correction","no condition"

Chemical aerosols
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30

   "NEGA","negativity correction","no condition"

Blowing snow
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SNSUB","blowing snow sublimation","LBLOWSNOW=T and LSNOWSUBL=T"
   "SNSED","blowing snow sedimentation","LBLOWSNOW=T"

