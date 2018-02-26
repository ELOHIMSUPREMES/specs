Name: steam
Version: 1.0.0.35
Release: alt2

Summary: Launcher for the Steam software distribution service
License: Proprietary
Group: Games/Other

URL: http://www.steampowered.com/
Packager: Nazarov Denis <nenderus@altlinux.org>
Vendor: Valve Corporation

ExclusiveArch: %ix86

Source0: http://repo.steampowered.com/%name/pool/%name/s/%name/%{name}_%version.tar.gz
Patch0: %name-apt-alt.patch

Requires: curl
Requires: glibc-pthread >= 2.15
Requires: glibc-nss >= 2.15
Requires: libGL
Requires: mozilla-plugin-adobe-flash
Requires: xz

BuildRequires: python-module-distribute
BuildRequires: xterm
BuildRequires: zenity

%description
Steam is a software distribution service with an online store, automated
installation, automatic updates, achievements, SteamCloud synchronized
savegame and screenshot functionality, and many social features.

%prep
%setup -n %name
%patch0 -p1

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%dir %_libdir/%name
%_libdir/%name/*
%_desktopdir/*
%_docdir/*
%_miconsdir/*
%_iconsdir/hicolor/24x24/apps/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/256x256/apps/*
%_man6dir/*
%_pixmapsdir/*

%changelog 
* Wed Mar 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.35-alt2
- Fix resolved DNS on x86_64 (ALT #28640)

* Sat Mar 02 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.35-alt1
- Version 1.0.0.35

* Mon Feb 25 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.34-alt1
- Version 1.0.0.34
- Added requires on curl and xz

* Sun Feb 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.33-alt2
- Fix summary title

* Sun Feb 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.33-alt1
- Version 1.0.0.33

* Wed Feb 20 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.29-alt1
- Version 1.0.0.29

* Sat Feb 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.28-alt1
- Version 1.0.0.28
- Added require on mozilla-plugin-adobe-flash

* Fri Feb 15 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.27-alt1
- Version 1.0.0.27

* Mon Feb 11 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt2
- Fix end of line in desktop file

* Sun Feb 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt1
- Initial build for ALT Linux

