#!/bin/bash

source debian/vars.sh

set -x

mkdir -p $DEB_INSTALL_ROOT/var/cpanel/wappspector

cp LICENSE $DEB_INSTALL_ROOT/var/cpanel/wappspector
cp README.md $DEB_INSTALL_ROOT/var/cpanel/wappspector
cp composer.json $DEB_INSTALL_ROOT/var/cpanel/wappspector
cp -r bin $DEB_INSTALL_ROOT/var/cpanel/wappspector
cp -r src $DEB_INSTALL_ROOT/var/cpanel/wappspector
cp -r .github $DEB_INSTALL_ROOT/var/cpanel/wappspector

cp $SOURCE1 $DEB_INSTALL_ROOT/var/cpanel/wappspector/composer-installer.php

echo "Files copied to install root:"
find $DEB_INSTALL_ROOT -type f | head -20