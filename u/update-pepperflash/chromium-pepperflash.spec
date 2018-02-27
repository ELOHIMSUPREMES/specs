Name: 	  update-pepperflash
Version:  1.5.3
Release:  alt2

Summary:  Pepper Flash Player downloader
License:  GPLv3+
Group:    Networking/WWW
Url: 	  http://altlinux.org/PepperFlash

Packager: Andrey Cherepanov <cas@altlinux.org>

Source1:  update-pepperflash

BuildRequires: curl wget gzip xml-utils
Requires: curl wget gzip xml-utils

%description
This package will download Chrome from Google, and unpack it to make the
included Pepper Flash Player available for use with Chromium.  The end
user license agreement is available at Google.

%package -n chromium-pepperflash
Summary:  Pepper Flash Player - browser plugin for Chromium
Group: Networking/WWW
BuildArch: noarch
Requires: %name = %version-%release
Requires: chromium

%description -n chromium-pepperflash
Pepper Flash Player - browser plugin for Chromium (virtual package)

%package -n firefox-pepperflash
Summary:  Pepper Flash Player - browser plugin for Firefox
Group: Networking/WWW
BuildArch: noarch
Requires: %name = %version-%release
Requires: /usr/bin/firefox
Requires: freshplayerplugin

%description -n firefox-pepperflash
Pepper Flash Player - browser plugin for Firefox (virtual package)

%prep

%install
install -D -m 0755 %SOURCE1 %buildroot%_sbindir/update-pepperflash
mkdir -p %buildroot%_libdir/pepper-plugins
touch %buildroot%_libdir/pepper-plugins/libpepflashplayer.so
mkdir -p %buildroot%_cachedir/pepperflash

%preun
[ "$1" -eq "0" ] && %_sbindir/update-pepperflash --uninstall --quiet ||:
exit 0

%post
%_sbindir/update-pepperflash --install --quiet ||:
%_sbindir/update-pepperflash --status ||:

%files
%_sbindir/update-pepperflash
%ghost %_libdir/pepper-plugins/libpepflashplayer.so
%dir %_cachedir/pepperflash

%files -n chromium-pepperflash
%files -n firefox-pepperflash

%changelog
* Wed Jul 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.3-alt2
- Bumped release to force pepflashplayer upgrade.

* Tue Mar 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.3-alt1
- update-pepperflash:
 + Cleanup cache dir after successful installation.
 + Change dl.google.com URLs to https.
- Rename main package to to update-pepperflash.
- Add {chromium,firefox}-pepperflash virtual packages.

* Tue Oct 14 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt3
- Force update from alt2 to prevent wrong %%preun trigger

* Mon Oct 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt2
- Do not remove plugin on update

* Thu Oct 09 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1
- Use only IPv4 for curl (fix hang up in %%post script)
- Show status on %%post section

* Tue Sep 16 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Fix version detect in new plugin versions
- Add arguments --clean and --version
- Change plugin location to %%_libdir/pepper-plugins

* Mon Sep 01 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt3
- Remove unnecessary require of glibc-utils

* Fri Aug 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt2
- Mark plugin file as %%ghost file (ALT #30225)
- Package cache directory

* Tue Jul 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Initial build in Sisyphus adapted from Debian

