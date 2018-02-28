%define module mageia-compat
Name: rpm-macros-%module
Summary: Mageia compatibility set of macro
Version: 0.01
Release: alt1
License: GPL
Group: System/Base
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: %name-%version.tar
#Requires: rpm-macros-kde-common-devel
Patch: mageia-compat.patch

%description
%summary

%prep
%setup
%patch -p0

%install
install -D -m644 %module -p %buildroot%_rpmmacrosdir/%module-base
for ext in cmake ; do
    install -D -m644 $ext.macros -p %buildroot%_rpmmacrosdir/%module-$ext
done

%files
%_rpmmacrosdir/*

%changelog
* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
