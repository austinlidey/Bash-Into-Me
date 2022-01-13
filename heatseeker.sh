#!/bin/bash

echo 'Enter target phrase:'
read flagtype

command=$(grep -nR $flagtype $pwd)
echo $command
