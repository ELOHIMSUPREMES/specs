# spec file for package qupzilla
# Original author: Mariusz Fik (Fisiu)
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

Name: qupzilla
Version: 1.8.3
Release: alt1

Summary: A very fast open source browser based on WebKit core
License: GPLv3+
Group: Networking/WWW

Url: http://qupzilla.com
# https://github.com/QupZilla/qupzilla
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Mar 13 2012
# optimized out: fontconfig libgst-plugins libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-sql libqt4-webkit libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ phonon-devel

BuildRequires: libqt4-devel >= 4.7
BuildRequires: gdb

Requires: libqt4-sql-sqlite

%description
QupZilla is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebKit rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.

%prep
%setup

%build
export USE_WEBGL="true"
export NONBLOCK_JS_DIALOGS="true"
export KDE="false"
export USE_LIBPATH="%_libdir"
echo "CONFIG += debug" >> src/defines.pri
qmake-qt4
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc AUTHORS FAQ
%_bindir/%name
%_libdir/%name
%_libdir/*.so.*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/*/*.png
%dir %_datadir/%name
%_datadir/%name/locale
%exclude %_datadir/%name/locale/uz@Latn.qm
%_datadir/%name/themes
%_datadir/bash-completion/completions/qupzilla
%_datadir/appdata/*

# TODO:
# - move shared libraries to a subpackage?

%changelog
* Sat Oct 25 2014 Michael Shigorin <mike@altlinux.org> 1.8.3-alt1
- 1.8.3 (closes: #30415)
- added appdata just in case

* Sun Oct 05 2014 Michael Shigorin <mike@altlinux.org> 1.8.1-alt1
- 1.8.1
- added missing dependency (closes: #30370)

* Fri Sep 26 2014 Michael Shigorin <mike@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 1.6.6-alt1
- 1.6.6

* Fri Apr 25 2014 Michael Shigorin <mike@altlinux.org> 1.6.5-alt1
- 1.6.5

* Mon Apr 14 2014 Michael Shigorin <mike@altlinux.org> 1.6.4-alt1
- 1.6.4

* Sat Feb 15 2014 Michael Shigorin <mike@altlinux.org> 1.6.3-alt1
- 1.6.3

* Mon Jan 27 2014 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2
- BR: gdb (https://github.com/QupZilla/qupzilla/issues/1180)
- disabled KDE integration, I prefer qupzilla package
  to stay relatively lean and mean regarding R:

* Mon Jan 27 2014 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1
- 1.6.1

* Thu Jan 02 2014 Michael Shigorin <mike@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Nov 22 2013 Michael Shigorin <mike@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Mar 12 2013 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jul 16 2012 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- 1.3.1
  + dropped desktop file patch (merged upstream)
- fixed x86_64 build (thx led@ for a hint)

* Sun Jul 15 2012 Michael Shigorin <mike@altlinux.org> 1.3.0-alt1
- 1.3.0
  + enabled nonblocking js dialogs
  + added desktop file patch from gentoo

* Tue Mar 13 2012 Michael Shigorin <mike@altlinux.org> 1.1.8-alt1
- initial build for ALT Linux Sisyphus (based on opensuse package)
- considerable cleanup of otherwise quite nice spec
- buildreq

* Tue Feb 14 2012 fisiu@opensuse.org
- Update to 1.1.8:
  + new translations: Swedish, Serbian and Traditional Chinese
  + option to use external download manager
  + import/export passwords into xml file
  + option to change user agent
  + support for JavaScript Popup windows
  + allow changing background in Speed Dial
  + many bugfixes, details in Changelog file
- Drop qupzilla-1.1.5-remove-date-time.patch: sed'ed in .spec
* Sun Jan  8 2012 fisiu@opensuse.org
- Update to 1.1.5:
  + new translations: Portuguese, French, Greek
  + add support for js printing with window.print()
  + improved commandline options
  + improved performance of history delete
  + many bugfixes
- Rebase remove_date-time.patch
* Thu Dec 22 2011 fisiu@opensuse.org
- Add fedora and mandriva items
* Mon Dec 19 2011 fisiu@opensuse.org
- Upstream update to 1.1.0:
  + speed dial
  + import bookmarks from html file
  + option to turn on XSS Auditing
  + many bugfixes
- Set variable KDE to "true" to enable better integration
  (atm only incons, nepomuk is planned)
* Tue Nov  1 2011 fisiu@opensuse.org
- enable webgl only for openSUSE >= 12.1
* Tue Nov  1 2011 fisiu@opensuse.org
- initial package
