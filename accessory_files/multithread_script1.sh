#!/bin/bash
input=$(echo $1 | sed 's/sample//g')
echo "Processing job $input"