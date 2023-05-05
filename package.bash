#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

rm -f send2World_Imagery_Wayback.zip

mkdir -p send2World_Imagery_Wayback
cp *.py send2World_Imagery_Wayback/
cp README.md send2World_Imagery_Wayback/
cp metadata.txt send2World_Imagery_Wayback/
cp -R icons/ send2World_Imagery_Wayback/icons/
zip -r send2World_Imagery_Wayback.zip send2World_Imagery_Wayback
rm -rf send2World_Imagery_Wayback
