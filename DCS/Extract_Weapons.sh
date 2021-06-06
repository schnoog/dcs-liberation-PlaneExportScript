#!/usr/bin/bash
IFS="
"

SP=`dirname $(realpath $0)`
cd "$SP"


rm Rafale_weapons.py 2>/dev/null

ALLWEAPONS=$(grep 'Weapons.' Rafale_plane.py | cut -d '=' -f 1 | sort -u )

for WEAPON in $ALLWEAPONS
do

tmp="    "$(echo "$WEAPON" | xargs)" ="
echo "---""$tmp""---" 

grep $tmp weapons_data.py >> Rafale_weapons.py

done



