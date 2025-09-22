Name:           ea-wappspector
Version:        0.2.8
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 1
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Tool for analyzing web frameworks used in hosted websites
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0:        v%{version}.tar.gz
Source1:        composer-installer.php

Requires:       ea-php-cli

%description
Command-line interface utility to analyze the file structure of a web hosting server and identify the frameworks and CMS used in the websites hosted on it.

%prep
%setup -q -n wappspector-%{version}
cp %{SOURCE1} composer-installer.php

%build
# No build steps - everything happens during package installation
echo "Source prepared for installation"

%install
mkdir -p %{buildroot}/usr/local/cpanel/bin
mkdir -p %{buildroot}/usr/local/cpanel/share/wappspector

# Copy all source files to share directory
cp -r . %{buildroot}/usr/local/cpanel/share/wappspector/

%post
echo "Building wappspector PHAR..."

cd /usr/local/cpanel/share/wappspector

# Install composer
/usr/local/cpanel/3rdparty/bin/php composer-installer.php

# Install dependencies
/usr/local/cpanel/3rdparty/bin/php composer.phar require clue/phar-composer
/usr/local/cpanel/3rdparty/bin/php composer.phar install

# Install phar-composer
/usr/local/cpanel/3rdparty/bin/php ./composer global require clue/phar-composer

# Build wappspector.phar
/usr/local/cpanel/3rdparty/bin/php -d phar.readonly=off vendor/bin/phar-composer build .

# Create wrapper script that uses cpanel php
cat > /usr/local/bin/ea-wappspector << 'EOF'
#!/bin/bash
exec /usr/local/cpanel/3rdparty/bin/php /usr/local/cpanel/share/wappspector/wappspector.phar "$@"
EOF

chmod 755 /usr/local/bin/ea-wappspector

echo "wappspector installation complete!"

%preun
echo "Cleaning up wappspector files..."

# Remove the wrapper script
rm -f /usr/local/bin/ea-wappspector

# Remove build artifacts that weren't tracked by RPM
if [ -d "/usr/local/cpanel/share/wappspector" ]; then
    rm -rf /usr/local/cpanel/share/wappspector/.composer
    rm -f /usr/local/cpanel/share/wappspector/composer.phar
    rm -f /usr/local/cpanel/share/wappspector/composer.lock
    rm -rf /usr/local/cpanel/share/wappspector/vendor
    rm -f /usr/local/cpanel/share/wappspector/wappspector.phar
fi

%postun
# Remove the directory if it's empty after RPM removes the tracked files
if [ -d "/usr/local/cpanel/share/wappspector" ]; then
    rmdir /usr/local/cpanel/share/wappspector
    echo "Removed empty wappspector directory"
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/cpanel/share/wappspector

%changelog
* Tue Sep 16 2025 Brian Mendoza <brian.mendoza@cpanel.net> - 0.2.8-1
- EA4-110: Initial version