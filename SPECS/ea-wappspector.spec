Name:           ea-wappspector
Version:        0.2.8
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 2
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Tool for analyzing web frameworks used in hosted websites
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0:        v%{version}.tar.gz
Source1:        composer-installer.php
Source2:        pkg.ea-wappspector.postinst
Source3:        pkg.ea-wappspector.prerm
Source4:        pkg.ea-wappspector.postrm
Source5:        ea-wappspector-wrapper

Requires:       ea-php-cli

%description
Command-line interface utility to analyze the file structure of a web hosting server and identify the frameworks and CMS used in the websites hosted on it.

%prep
%setup -q -n wappspector-%{version}
cp %{SOURCE1} composer-installer.php
cp %{SOURCE5} ea-wappspector-wrapper

%build
# No build steps - everything happens during package installation
echo "Source prepared for installation"

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/opt/cpanel/ea-wappspector

# Copy all source files to wappspector directory
cp -r . %{buildroot}/opt/cpanel/ea-wappspector

cp ea-wappspector-wrapper %{buildroot}/usr/bin/ea-wappspector
chmod 755 %{buildroot}/usr/bin/ea-wappspector

%post

%include %{SOURCE2}

%preun

%include %{SOURCE3}

%postun

%include %{SOURCE4}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/cpanel/ea-wappspector
/usr/bin/ea-wappspector

%changelog
* Thu Oct 16 2025 Brian Mendoza <brian.mendoza@cpanel.net> - 0.2.8-2
- EA4-153: Bump version to fix issues

* Tue Sep 16 2025 Brian Mendoza <brian.mendoza@cpanel.net> - 0.2.8-1
- EA4-110: Initial version