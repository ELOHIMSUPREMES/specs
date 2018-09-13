%define oname ice

Name: ice-ssb
Version: 5.3.4
Release: alt1

Summary: Application to easily add and remove Chromium site specific browsers.
License: GPL
Group: Networking/WWW
Url: https://github.com/peppermintos/ice
BuildArch: noarch

Source: %name-%version.tar
Patch0: fix-paths.patch

Requires: python3-module-requests
Requires: chromium

%description
Application to easily add and remove Chromium site specific browsers in Debian 
and Ubuntu based Linux distributions. It was originally created for Peppermint 
OS Ice and is now used as the default SSB application in Peppermint OS since 
the two branches of the OS merged for Peppermint Two. Since version 5, Ice has 
supported Google Chrome. Since version 5.1, Ice has supported Mozilla Firefox.

%prep
%setup
%patch0 -p1

%install
install -d -m 0755 %buildroot%_bindir
install -m 0755 %name/%oname %buildroot%_bindir/%name
install -m 0755 %name/%oname-firefox %buildroot%_bindir/%oname-firefox

install -d -m 0755 %buildroot/usr/lib/peppermint
install -d -m 0755 %buildroot/usr/lib/peppermint/%oname
install -m 0755 %name/%oname.glade %buildroot/usr/lib/peppermint/%oname/%oname.glade
install -m 0755 %name/search.json.mozlz4 %buildroot/usr/lib/peppermint/%oname/search.json.mozlz4

install -d -m 0755 %buildroot%_desktopdir
install -m 0755 %name/%oname.desktop %buildroot%_desktopdir/%name.desktop

install -d -m 0755 %buildroot%_pixmapsdir
install -m 0755 %name/%oname.png %buildroot%_pixmapsdir/%name.png

install -d -m 0755 %buildroot%_datadir/%name
cp -fR %name/locale %buildroot%_datadir/%name

%files
%_bindir/%name
%_bindir/%oname-firefox
%dir /usr/lib/peppermint
%dir /usr/lib/peppermint/%oname
/usr/lib/peppermint/%oname/%oname.glade
/usr/lib/peppermint/%oname/search.json.mozlz4
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/%name/locale


%changelog
* Tue Sep 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt1
- Init build to Sisyphus

