#!/bin/bash

for dir in *
do
    #echo $dir

    for song in $dir/*txt
    do
        #echo $song
        songName=`sed -e '1s/^\xef\xbb\xbf//' $song | grep "{title:" | sed -e "s/{title: *//" | sed s/}.*//`
        songData=`sed ':a;N;$!ba;s/\n/\\n/g' $song`

        echo "$songName ------------ $song $songData"
    done

done
