Name: dvdstyler
Version: 2.4.3
Release: alt1
Summary: %name is a crossplatform DVD Authoring System
Summary(ru_RU.UTF-8): %name - это программа для создания DVD дисков
License: GPL
Group: Video
Url: http://www.dvdstyler.de
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: http://prdownloads.sourceforge.net/dvdstyler/DVDStyler-%version.tar
Source2: %name.desktop
Source4: %name-16x16.png
Source5: %name-32x32.png

BuildRequires: gcc-c++ libwxGTK2.9-devel libmjpegtools-devel netpbm libnetpbm-devel libwxsvg-devel libexif-devel libjpeg-devel libudev-devel libgnomeui-devel
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel libavfilter-devel libswscale-devel avconv
BuildRequires: dvdauthor mjpegtools genisoimage dvd+rw-tools cdrecord-classic dvdrecord xmlto zip bison flex mpgtx

Requires: mjpegtools dvdauthor dvd+rw-tools genisoimage dvdisaster

%description 
%name is a crossplatform DVD Authoring System.
The main %name features are:
    * you can drag and drop MPEG files directly
    * you can import image file for background
    * you can create NTSC/PAL menus
    * you can place text and images anywhere on the menu screen
    * you can change font/color
    * you can put basic text buttons, change font/color and background color
    * you can copy and paste any menu object
    * you can set chapters for each movie
    * you can change post command for each movie

%description -l ru_RU.UTF-8
%name программа для создания DVD дисков.
Основные возможности:
    * вы можете просто перетащить ваши видеозаписи мышкой
    * вы можете импортировать изображения как фон
    * вы можете создавать NTSC/PAL меню
    * вы можете размещать текст и меню где угодно на экране
    * вы можете менять шрифт и цвет
    * вы можете создавать простые текстовые кнопки, изменять шрифт и фоновый цвет
    * вы можете копировать и вставлять любой объект меню
    * вы можете создавать главы для каждого фильма
    * вы пожете указывать команды для каждого фильма
    * и многое другое...

%prep
%setup -q -n DVDStyler-%version

rm -f ./configure

touch NEWS

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

#meny
install -p -m 644 %SOURCE2 %buildroot%_datadir/applications

#icons
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir
install -p -m 644 %SOURCE4 %buildroot%_miconsdir/%name.png
install -p -m 644 %SOURCE5 %buildroot%_niconsdir/%name.png
install -p -m 644 data/%name.png %buildroot%_liconsdir/%name.png

%find_lang --with-gnome %name

%files -f %name.lang
%doc COPYING README TODO ChangeLog
%_bindir/*
%_datadir/%name
%_man1dir/*

#icons
%_datadir/pixmaps/*
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_datadir/applications/*


%changelog
* Tue Apr 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.3-alt1
- New release version
- Cleanup spec

* Sat Sep 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3-alt1
- New release version

* Thu May 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2-alt1
- New release version (ALT #26810)

* Wed Jan 25 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1-alt1
- New release version (ALT #26810)
- Drop all patches and add from ubuntu

* Fri Dec 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.1-alt1
- New release version

* Sat Aug 13 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.4.2-alt1
- New release version (ALT #25983)
- Add dvdstyler-libav.patch (thanks sbolshakov@)

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1.1
- Rebuilt with updated wxGTK2.9

* Sun Apr 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.3-alt1
- New release version

* Sat Mar 26 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.2.1-alt2
- Rebuild

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2.1-alt1.0
- Rebuilt with wxGTK2.9
- Add patch for fix build with wxGTK2.9

* Sun Mar 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.2.1-alt1
- New release version

* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.2-alt2
- New release version

* Sun Sep 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.2-alt1b3
- New beta 3 version

* Mon Jun 21 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.1-alt1
- New release version

* Sun Apr 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.0.2-alt1
- New minor release version

* Mon Feb 08 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.0-alt1
- New release version

* Mon Nov 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.4-alt4
- New minor release

* Thu Oct 29 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.4-alt3
- New release version

* Fri Sep 25 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.4-alt2.r1
- New version
- Add Requires: mjpegtools dvdauthor dvd+rw-tools genisoimage dvdisaster

* Sat Sep 12 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.4-alt1.b2
- New version

* Mon Aug 17 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.3-alt2
- New version

* Tue Jul 21 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.7.3-alt1.b4
- New version

* Fri Mar 13 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.2-alt1
- New version
- Add xmlto, zip to BuildRequires

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.1-alt1
- New version
- Remmove depricated update-menus
- Remove patch

* Thu Nov 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.0-alt2
- Fix for repocop test

* Fri Sep 12 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.0-alt1
- New version
- Add patch for build with ffmpeg (Thanks hsvhome at mail.ru)
- Fix for repocop test

* Wed Jun 25 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.2-alt1
- New version
  + added possibility to add audio to the menu
  + added possibility to copy complete menu
  + added possibility to copy menu objects by pressing control key and moving
  + some other small changes
* Tue Jan 22 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.6.0-alt1
- built for ALT Linux
