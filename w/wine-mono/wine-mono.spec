%define winemonodir %_datadir/wine/mono

Name: wine-mono
Version: 4.5.6
Release: alt1

Summary: Windows build of Mono to run .NET applications via Wine

License: MPL
Group: Office
Url: http://wiki.winehq.org/Mono

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://prdownloads.sf.net/projects/wine/files/Wine%%20Mono/%version/wine-mono-%version.msi
Source: http://downloads.sourceforge.net/wine/wine-mono-%version.msi

BuildArch: noarch

%description
Mono is an open-source and cross-platform implementation of the .NET
Framework. Wine can use a Windows build of Mono to run .NET applications.
For Wine releases 1.5.3 and later, the Wine Mono package is recommended.

%install
mkdir -p %buildroot%winemonodir
install -m 644 %SOURCE0 %buildroot%winemonodir

%files
%dir %_datadir/wine/
%dir %winemonodir/
%winemonodir/%name-%version.msi

%changelog
* Mon Mar 09 2015 Vitaly Lipatov <lav@altlinux.ru> 4.5.6-alt1
- update to 4.5.6

* Fri Dec 12 2014 Vitaly Lipatov <lav@altlinux.ru> 4.5.4-alt1
- update to 4.5.4

* Thu Sep 25 2014 Vitaly Lipatov <lav@altlinux.ru> 4.5.2-alt1
- update to 4.5.2

* Sat Dec 22 2012 Vitaly Lipatov <lav@altlinux.ru> 0.0.8-alt1
- update to 0.0.8

* Sat Jul 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.0.4-alt1
- initial build for ALT Linux Sisyphus (0.0.4 use since wine 1.5.6)

