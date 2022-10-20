#!/usr/bin/bash

read -p "Enter url: " URL

#data url:  https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip

if [ -z "$URL"];
then
	echo "No url passed..."
else
	curl "$URL" -O

echo "****************************** DONE ***********************************"

ZIPFILE="stack-overflow-developer-survey-2021.zip"

unzip "$ZIPFILE"

rm "$ZIPFILE"

fi
