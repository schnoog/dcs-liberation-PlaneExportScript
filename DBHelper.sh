#!/usr/bin/bash
IFS="
"

SP=`dirname $(realpath $0)`
cd "$SP"

cd exporttmpdir

function GetInjection {
	echo $1

}

function GetCaps {
CAPS="CAP
CAS
Transport
Refueling
AWACS
PinpointStrike
AirDefence
Reconnaissance
Nothing
Embarking
Carriage
CargoTransportation"

DF="*.dump"

ALL=$(grep tasks $DF)



#grep tasks *.dump | grep "$1" | cut -d "." -f 1


}






function Work {
	PLANE=$1
	GetInjection  $PLANE
	GetCaps $PLANE
}


Work $1