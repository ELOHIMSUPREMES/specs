# TODO: add cherrypy, check other bundled three part projects and drop it

# -*- coding: utf-8 -*-
Name: calibre
Version: 0.9.42
Release: alt1

Summary: A e-book library management application
Summary(ru_RU.UTF8): Программа для работы с личной электронной библиотекой

License: GPL
Group: File tools
Url: http://calibre-ebook.com/

Packager: Damir Shayhutdinov <damir@altlinux.ru>

# Source-url: http://status.calibre-ebook.com/dist/src
Source: %name-%version.tar
Source1: calibre-mount-helper

Patch: calibre-no-update.patch
Patch1: calibre-0.8.55-alt-no-macmenu.patch

Requires: fonts-ttf-liberation

%add_python_req_skip win32serviceutil win32service win32event win32con win32com win32api pythoncom usbobserver

BuildRequires: chrpath
BuildRequires: xdg-utils >= 1.0.2
BuildRequires: /proc

BuildRequires: gcc-c++ libX11-devel libXext-devel libjpeg-devel libusb-devel libsqlite3-devel

BuildRequires: python-modules-json python-modules-compiler python-modules-curses python-modules-encodings
BuildRequires: python-module-sip-devel

# Note: checked with http://calibre-ebook.com/download_linux 04.08.2013
BuildRequires: python-module-imaging >= 1.1.6
BuildRequires: libqt4-devel >= 4.8.0
BuildRequires: python-module-PyQt4-devel >= 4.9.6
BuildRequires: python-module-mechanize >= 0.1.11
BuildRequires: libImageMagick-devel >= 6.5.9
BuildRequires: python-module-lxml >= 2.2.1
BuildRequires: python-module-dateutil >= 1.4.1
BuildRequires: python-module-cssutils >= 0.9.9
BuildRequires: python-module-BeautifulSoup >= 3.0.5
BuildRequires: python-module-dns >= 1.6.0
BuildRequires: libpoppler-qt4-devel >= 0.20.2
BuildRequires: libpodofo-devel >= 0.8.2
BuildRequires: libwmf-devel >= 0.2.8
BuildRequires: libchm-devel >= 0.4
BuildRequires: libicu-devel >= 4.4
BuildRequires: libmtp-devel >= 1.1.5
BuildRequires: python-module-netifaces >= 0.8
#Requires: psutil
BuildRequires: python-module-cssselect >= 0.7.1

%description
calibre is an e-book library manager. It can view, convert and catalog e-books
in most of the major e-book formats. It can also talk to e-book reader
devices. It can go out to the internet and fetch metadata for your books.
It can download newspapers and convert them into e-books for convenient
reading. It is cross platform, running on Linux, Windows and OS X.

%description -l ru_RU.UTF8
Calibre - свободная программа для создания и управления библиотекой электронных книг,.
которая работает в среде Linux, OSX и Windows. Calibre должна уметь делать все, что
необходимо для поддержки электронной библиотеки: работать с каталогом, преобразовывать.
форматы, загружать новости и адаптировать их для устройств чтения, а также.
синхронизировать коллекцию с устройствами для чтения.

Поддерживаемые форматы: MOBI, LIT, PRC, EPUB, ODT, HTML, CBR, CBZ, RTF,
TXT, PDF, LRS и FB2.

%prep
%setup -n %name
# don't check for new upstream version
%patch -p1
%patch1 -p1

%build
%python_build

%install
#python_install (not use due skip-build unsupported)
mkdir -p %buildroot%python_sitelibdir/
python setup.py install --staging-libdir=%buildroot%_libdir --libdir=%_libdir --prefix=%_prefix --root=%buildroot --staging-root=%buildroot/%_prefix
%find_lang --with-kde %name
# fix /etc placement
mv %buildroot{/usr,}/etc

chrpath -d %buildroot%_libdir/%name/%name/plugins/*.so

rm -f %buildroot%_bindir/calibre-uninstall
rm -rf %buildroot%_datadir/%name/fonts/liberation/
install -m 755 %SOURCE1 %buildroot%_bindir/calibre-mount-helper

%files -f %name.lang
%doc README.md Changelog.yaml
/etc/bash_completion.d/%name
%_bindir/*
%_libdir/%name/
# FIXME: strange
%ifnarch x86_64
%python_sitelibdir/*
%endif
%_datadir/%name/

%changelog
* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.42-alt1
- new version 0.9.42 (with rpmrb script)

* Thu Apr 18 2013 Anton Farygin <rider@altlinux.ru> 0.8.55-alt1.4
- rebuild with new ImageMagick

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.8.55-alt1.3
- Correct install icons and remove rpath from plugins

* Thu Jan 17 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.55-alt1.2
- rebuild with new sip

* Thu Oct 11 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.55-alt1.1
- disable xbar support

* Tue Jun 19 2012 Anton Farygin <rider@altlinux.ru> 0.8.55-alt1
- Updated to 0.8.55 release
=======
- new version 0.9.42 (with rpmrb script) (ALT bug #29056)
- rebuild with libpodofo 0.9.1
- partially added private qt4 4.8.5 headers
- add no-update patch from Fedora
>>>>>>> add some private headers from qt4-4.8.5

* Wed Jun 13 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.41-alt3
- rebuild with libpodofo

* Tue Feb 28 2012 Mykola Grechukh <gns@altlinux.ru> 0.8.41-alt2
- Updated to 0.8.41 release

* Fri Nov 25 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.8.27-alt2
- Fixed shebang in all executable scripts (env python2->env python)

* Thu Nov 24 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.8.27-alt1
- Updated to 0.8.27 release

* Thu Mar 31 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.7.50-alt2
- Dropped sphinx depends

* Wed Mar 30 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.7.50-alt1
- new version
- drop bzr depends (closes #18216)
- rebuilt with new sip API (closes #24867)

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 0.7.9-alt2
- rebuild with new ImageMagick

* Tue Aug 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.7.9-alt1
- new version
- skip bundling Liberation fonts in favor of corresponding package

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6.37-alt1
- new version (0.6.37) (fix alt bug #18217)
- add russian translation (thanks, V. Dikonov)
- fix build on x86_64, update buildreqs

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.77-alt1.1
- Rebuilt with python 2.6

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.77-alt1
- initial build for ALT Linux Sisyphus
