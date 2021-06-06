# dcs-liberation-PlaneExportScript
bash script to export plane and weapon data for modded aircraft

Exports the data required for Step1 of 
https://github.com/dcs-liberation/dcs_liberation/wiki/Modded-Aircraft-Support

extracts data (after export) from DCS/planes.py into plane specific py files 

Remark: In my installation the aircraft data was stored in planes.py instead of aircraft.py like mentioned in the dsc_liberation Wiki

If your installation exports into aircraft.py, please adjust the line 

export DATAFILE="DCS/planes.py"

Extract the data as explained in the dcs_liberation wiki into the DCS folder of this script.

Install bash (f.e. Git for Windows or MinGW), open bash move into the script folder (f.e.  cd /E/DCS_Tools/ )


Run with 
./Extract_Planes.sh -Plane-Name-

-This is case sensitive will add wildcards to the plane name (Rafale will also export Rafale_A_S , Rafale_B and so on)

