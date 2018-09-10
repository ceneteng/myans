#!/bin/bash

echo "Enter the filename"
read filename

if [ -e "$filename" ]
then 
    echo "copying the file!"
    ansible all -m copy -a "src=$filename dest=$filename.bak"
else
    echo "Sorry the file doesn't exist"

fi
