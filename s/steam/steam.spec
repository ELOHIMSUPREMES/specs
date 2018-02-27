Name: steam
Version: 1.0.0.47
Release: alt1

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
%makeinstall_std
%__rm -rf %buildroot%_bindir/%{name}deps
%__install -Dp -m0644 lib/udev/rules.d/99-%name-controller-perms.rules %buildroot%_udevrulesdir/99-%name-controller-perms.rules

%files
%_bindir/%name
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
%config %_udevrulesdir/99-%name-controller-perms.rules

%changelog 
* Fri Feb 14 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.47-alt1
- Version 1.0.0.47

* Wed Nov 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.45-alt0.M70P.1
- Build for branch p7

* Wed Nov 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.45-alt1
- Version 1.0.0.45

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt0.M70P.1
- Build for branch p7

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt0.M70T.1
- Build for branch t7

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt1
- Version 1.0.0.44

* Thu Oct 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.43-alt0.M70P.1
- Build for branch p7

* Thu Oct 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.43-alt1
- Version 1.0.0.43

* Tue Sep 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.42-alt0.M70P.1
- Build for branch p7

* Tue Sep 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.42-alt1
- Version 1.0.0.42

* Wed Sep 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.41-alt0.M70P.1
- Build for branch p7 (ALT #29322)

* Wed Sep 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.41-alt1
- Version 1.0.0.41

* Thu Aug 29 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.40-alt0.M70P.1
- Build for branch p7

* Thu Aug 29 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.40-alt1
- Version 1.0.0.40

* Sun May 12 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.39-alt0.M70P.1
- Build for branch p7

* Sat May 11 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.39-alt1
- Version 1.0.0.39

* Sun May 05 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.38-alt0.M70P.1
- Build for branch p7

* Sat Apr 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.38-alt1
- Version 1.0.0.38

* Wed Apr 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.37-alt1
- Version 1.0.0.37

* Wed Mar 13 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.36-alt1
- Version 1.0.0.36

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

