%set_verify_elf_method unresolved=strict

Name: gnustep-gmines
Version: 0.2
Release: alt3
Summary: The classic Minesweeper game 
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/gmines/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
The classic Minesweeper game for GNUstep.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Rebuilt with new gnustep-gui

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added menu file (thnx kostyalamer@)

* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

