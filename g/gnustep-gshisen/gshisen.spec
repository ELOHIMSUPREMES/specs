%set_verify_elf_method unresolved=strict

Name: gnustep-gshisen
Version: 1.3.0
Release: alt4
Summary: GShisen is a game for GNUstep
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/gshisen/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
GShisen is the first GNUstep game!

The object of the game is to remove all tiles from the field. Only two
matching tiles can be removed at a time. Two tiles can only be removed
if they can be connected with at most three connected lines. Lines can
be horizontal or vertical but not diagonal.

Remember that lines may cross the empty border. If you are stuck, you
can use the Hint feature to find two tiles which may be removed.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt4
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3
- Rebuilt with new gnustep-gui

* Sun Jan 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Added menu file (thnx kostyalamer@)

* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

