#!/bin/sh
delimter=$' '
valid=0

while IFS="$delimter" read -r quantity char password; do
    min=`echo "$quantity" | cut -d "-" -f 1`
    max=`echo "$quantity" | cut -d "-" -f 2`
    letter=`echo "$char" | cut -c 1`
    letter_count=0
    for(( i=0 ; i<${#password} ; i++))do
        if [ ${password:$i:1} = "$letter" ]
        then
            let "letter_count+=1"
        fi
    done
    if [ "$letter_count" -ge "$min" ] && [ "$letter_count" -le "$max" ]
    then
        let "valid+=1"
    fi
done

echo $valid
