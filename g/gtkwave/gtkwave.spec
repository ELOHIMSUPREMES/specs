Name: gtkwave
Version: 3.3.58
Release: alt1
Summary: %name
License: GPL
Group: Development/Other

Packager: Denis Smirnov <mithraen@altlinux.ru>

Url: http://gtkwave.sourceforge.net/

Source: %name-%version.tar
Source100: %name.watch

# Automatically added by buildreq on Thu Aug 08 2013 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel gnu-config libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-server pkg-config python-base rpm-build-tcl shared-mime-info tcl tcl-devel xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel desktop-file-utils flex gcc-c++ gperf libgtk+2-devel liblzma-devel tk-devel

%description
%summary

%prep
%setup

%build
%configure --disable-mime-update
%make_build
%install
%makeinstall_std

%files
%_bindir/*
%_man5dir/*
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/gnome/16x16/mimetypes/*.png
%_iconsdir/gnome/32x32/mimetypes/*.png
%_iconsdir/gnome/48x48/mimetypes/*.png
%_iconsdir/gtkwave_256x256x32.png
%_iconsdir/gtkwave_files_256x256x32.png
%_iconsdir/gtkwave_savefiles_256x256x32.png
%_datadir/mime/packages/*.xml

%changelog
* Thu Apr 03 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.58-alt1
- new version 3.3.58

* Mon Feb 17 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.57-alt1
- new version 3.3.57

* Fri Feb 14 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.56-alt1
- new version 3.3.56

* Tue Feb 11 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.55-alt1
- new version 3.3.55

* Sun Jan 05 2014 Cronbuild Service <cronbuild@altlinux.org> 3.3.54-alt1
- new version 3.3.54

* Thu Dec 19 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.53-alt1
- new version 3.3.53

* Tue Nov 12 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.52-alt1
- new version 3.3.52

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.51-alt1
- new version 3.3.51

* Thu Oct 17 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.50-alt1
- new version 3.3.50

* Sat Sep 14 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.49-alt1
- new version 3.3.49

* Thu Aug 08 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.48-alt1
- new version 3.3.48

* Tue Jun 11 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.47-alt1
- new version 3.3.47

* Fri May 03 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.46-alt1
- new version 3.3.46

* Sun Mar 24 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.45-alt1
- new version 3.3.45

* Sat Mar 02 2013 Cronbuild Service <cronbuild@altlinux.org> 3.3.44-alt1
- new version 3.3.44

* Fri Feb 08 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.43-alt1
- new version 3.3.43

* Mon Jan 21 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.42-alt1
- new version 3.3.42

* Thu Nov 08 2012 Denis Smirnov <mithraen@altlinux.ru> 3.3.41-alt1
- 3.3.41

* Fri Oct 12 2012 Denis Smirnov <mithraen@altlinux.ru> 3.3.40-alt1
- 3.3.40

* Wed Apr 04 2012 Denis Smirnov <mithraen@altlinux.ru> 3.3.34-alt1
- 3.3.34

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.26-alt2
- add buildrequires to liblzma-devel

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.26-alt1
- 3.3.26

* Fri Mar 25 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt5
- rebuild

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt4
- auto rebuild

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt3
- auto rebuild

* Thu Dec 31 2009 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt2
- add Url tag

* Sun Dec 27 2009 Denis Smirnov <mithraen@altlinux.ru> 3.3.0-alt1
- first build for Sisyphus
