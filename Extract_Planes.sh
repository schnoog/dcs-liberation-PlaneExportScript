#!/usr/bin/bash
IFS="
"

SP=`dirname $(realpath $0)`
#echo $SP
cd "$SP"

export DATAFILE="DCS/planes.py"
export WEAPONFILE="DCS/weapons_data.py"

mkdir -p OUTPUT

export exporttmpdir="$SP""/exporttmpdir/"
mkdir -p "$exporttmpdir"



function SanitizePlane {
	PLANE=$1
	PFILE="$exporttmpdir""$PLANE"".dump"
	WFILE="$exporttmpdir""$PLANE"".weapon"
	mkdir -p "OUTPUT/$PLANE/"
	OUTFILE="OUTPUT/$PLANE/$PLANE"".py"
	echo "Combining $PFILE AND $WFILE to $OUTFILE"
	
	echo 'from enum import Enum' > "$OUTFILE"
	echo '' >> "$OUTFILE"
	echo 'from dcs import task' >> "$OUTFILE"
	echo 'from dcs.planes import PlaneType' >> "$OUTFILE"
	echo 'from dcs.weapons_data import Weapons' >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	echo 'from pydcs_extensions.weapon_injector import inject_weapons' >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	WCLASS="Weapons""$PLANE"
	echo "class $WCLASS"":" >> "$OUTFILE"
	cat "$WFILE" >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	INJ='inject_weapons('"$WCLASS"')'
	echo "$INJ" >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	echo '' >> "$OUTFILE"
	cat "$PFILE" >> "$OUTFILE"

	
}


function ExportPlane {
	PLANE=$1
	FIRSTLINE=0
	LASTLINE=0
	echo "#####################################"
	PFILE="$exporttmpdir""$PLANE"".dump"
	WFILE="$exporttmpdir""$PLANE"".weapon"
#	PF=$(cat "$DATAFILE")
	SL="class $PLANE""(PlaneType)"
	FIRSTLINE=$(grep -n "$SL" $DATAFILE | cut -d ':' -f 1)
	#grep -n "$SL" $DATAFILE
	ABSEND=$(grep -n 'plane_map =' $DATAFILE | cut -d ':' -f 1)
	
	POSSENDS=$(grep -n '(PlaneType)' $DATAFILE | grep -A99999 "$SL" | cut -d ':' -f 1)
	
	for POSSEND in $POSSENDS
	do
		if [ $POSSEND -gt $FIRSTLINE ]
		then
			let LASTLINE=$POSSEND-1
			break
		fi
	done

	if [ $LASTLINE -eq 0 ]
	then
		let LASTLINE=$ABSEND-1
	fi


	echo "Extract $PLANE from $FIRSTLINE to $LASTLINE"
	cat $DATAFILE | head -n +$LASTLINE | tail -n +$FIRSTLINE > "$PFILE"


	ALLWEAPONS=$(grep 'Weapons.' "$PFILE" | cut -d '=' -f 1 | sort -u )

	for WEAPON in $ALLWEAPONS
	do

	tmp="    "$(echo "$WEAPON" | xargs)" ="
	echo "---""$tmp""---" 

	grep $tmp $WEAPONFILE >> "$WFILE"

	done






}


PLANE_NAME=$1
if [ "$PLANE_NAME" == "" ]
then
	PLANE_NAME="Rafale"
fi


PLANENAMES=$(grep "$PLANE_NAME" $DATAFILE | grep PlaneType | cut -d " " -f 2 | cut -d '(' -f 1)

for PLANE_WORK in $PLANENAMES
do
	ExportPlane "$PLANE_WORK"
	SanitizePlane "$PLANE_WORK"
done