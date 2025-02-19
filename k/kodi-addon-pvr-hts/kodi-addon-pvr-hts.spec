Name: kodi-addon-pvr-hts
Version: 18.0
Release: alt1

Summary: PVR TVheadend addon for Kodi
License: GPL
Group: Video

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libcec-platform-devel libkodiplatform-devel >= 18.0

%description
%summary

%prep
%setup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_INSTALL_LIBDIR=%_libdir/kodi
%make_build

%install
%makeinstall_std

%files
%_libdir/kodi/addons/pvr.hts
%_datadir/kodi/addons/pvr.hts

%changelog
* Thu Jan 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Thu Nov 29 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- initial
