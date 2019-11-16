#!/bin/bash

while read fpath
do
    fpathhtml="${fpath%.txt}.html"
    fpathpdf="${fpath%.txt}.pdf"
    jschordpro -fhtml -o$fpathhtml $fpath
    /opt/google/chrome/chrome --headless --print-to-pdf="$fpathpdf" $fpathhtml
done
