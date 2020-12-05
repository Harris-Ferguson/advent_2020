#!/bin/bash

delimter=$' '
valid=0

while IFS="$delimter" read -r quantity char password; do
    min=`echo "$quantity" | cut -d "-" -f 1`
    max=`echo "$quantity" | cut -d "-" -f 2`
    letter=`echo "$char" | cut -c 1`
    let "min-=1"
    let "max-=1"
    if [ "${password:$min:1}" = "$letter" ] && [ "${password:$max:1}" != "$letter" ]
    then
        let "valid+=1"
    elif [ "${password:$min:1}" != "$letter" ] && [ "${password:$max:1}" = "$letter" ]
    then
        let "valid+=1"
    fi
done

echo $valid
