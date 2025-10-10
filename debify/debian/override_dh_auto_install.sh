#!/bin/bash

source debian/vars.sh

set -x

mkdir -p $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector
mkdir -p $DEB_INSTALL_ROOT/usr/local/bin

cp LICENSE $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector
cp README.md $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector
cp composer.json $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector
cp ea-wappspector-wrapper $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector
cp -r bin $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector
cp -r src $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector
cp -r .github $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector

cp $SOURCE1 $DEB_INSTALL_ROOT/opt/cpanel/ea-wappspector/composer-installer.php
cp $SOURCE5 $DEB_INSTALL_ROOT/usr/local/bin/ea-wappspector
chmod 755 $DEB_INSTALL_ROOT/usr/local/bin/ea-wappspector

echo "Files copied to install root:"
find $DEB_INSTALL_ROOT -type f | head -20