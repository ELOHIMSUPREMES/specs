Name:		gamine
Version:	1.1
Release:	alt4
Summary:	Gamine - game for small children :)
Source:		%name-%version.tar.gz
Source1:	%name.desktop.in
URL:		http://gnunux.info/projets/gamine
Group:		Games/Educational
License:	Distributable

BuildRequires:  libGConf-devel libcairo-devel gstreamer-devel gtk2-devel GConf

%description
Gamine is a game designed for 2 years old children who are not able to
use mouse and keyboard.

The child uses the mouse to draw coloured dots and lines on the screen
and keyboard to display letter.

Author:
--------
GARETTE Emmanuel (gnunux@gnunux.info)

%prep
%setup
cp %SOURCE1 .
subst 's/^LDLIBS = /LDLIBS = -lX11 -lm /' Makefile

%build
%make_build

%install
mkdir -p %buildroot/usr/
make install PREFIX=%buildroot/usr/

%files
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/doc/%name/*
%_datadir/%name/*
%_datadir/icons/%name.png
%_datadir/icons/hicolor/scalable/apps/%name.svg
%_datadir/locale/*/LC_MESSAGES/%name.mo

%changelog
* Fri Feb 21 2014 Andrey Cherepanov <cas@altlinux.org> 1.1-alt4
- Fix build in Sisyphus (missing libm in linked libs)

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 1.1-alt3
- Adapt BuildRequires to new version of GConf

* Fri Jun 01 2012 Andrey Cherepanov <cas@altlinux.org> 1.1-alt2
- Add required X11 library to the linker command line

* Wed Aug 17 2011 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Initial build for Sisyphus (thanks kostyalamer) (closes: #26074)

