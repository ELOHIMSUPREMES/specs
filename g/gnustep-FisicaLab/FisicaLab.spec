%set_verify_elf_method unresolved=strict

Name: gnustep-FisicaLab
Version: 0.3.2
Release: alt1
Summary: FisicaLab.app is an educational application to solve physics problems
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: libgsl-devel gnustep-gui-devel

%description
FisicaLab consist in a chalkboard to set the problems and a palette with
elements like mobiles, blocks, forces,... that let the user set the
problems.

FisicaLab can solve the fallowing problems:
* Kinematics of particles in 2D.
* Circular kinematics of particles in 2D.
* Static of particles in 2D.
* Static of rigid bodies in 2D.
* Dynamics of particles in 2D.
* Circular dynamics of particles in 2D.
* Heat, calorimetry, ideal gas and expansion.

%prep
%setup

%build
%autoreconf
%configure

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

install -Dp -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Version 0.3.2

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

