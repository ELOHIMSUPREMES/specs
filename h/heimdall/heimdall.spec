# SPEC file for heimdall package

%def_without gui

Name:    heimdall
Version: 1.3.2
Release: alt1

Summary: tool suite to flash firmware onto Samsung smartphones

License: %bsdstyle
Group:   Other
URL:     https://github.com/Benjamin-Dobell/Heimdall
#URL:    http://www.glassechidna.com.au/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-1.3.2-alt-fix_install.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Fri Sep 07 2012
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-xml libstdc++-devel pkg-config zlib-devel
BuildRequires: gcc-c++ libusb-devel

%if_with gui
BuildRequires: phonon-devel
%endif

%description
Heimdall is a cross-platform open-source tool suite used to flash
firmware (aka ROMs) onto Samsung Galaxy S devices and some other
Samsung smartphones.

This software attempts to flash your Galaxy S device. The very
nature of flashing is dangerous. As with all flashing software,
Heimdall has the potential to damage (brick) your phone if not
used carefully. If you're concerned, don't use this software.

%if_with gui
%package frontend
Summary: graphic fronted to the Heimdall
Group: Other
License: %bsdstyle
Requires: %name

%description frontend
Heimdall is a cross-platform open-source tool suite used to flash
firmware (aka ROMs) onto Samsung Galaxy S devices and some other
Samsung smartphones.

This package contains graphic frontend to the Heimdall utility.
%endif

%prep
%setup
%patch0 -p1

%patch1


%build
cd libpit
%autoreconf
%configure
%make_build
cd ..

cd heimdall
%autoreconf
%configure
%make_build
cd ..

%if_with gui
cd heimdall-frontend
%_qt4dir/bin/qmake heimdall-frontend.pro OUTPUTDIR=%_bindir
%make_build
%endif

%install
cd heimdall
%make_install DESTDIR=%buildroot install
cd ..

%if_with gui
cd heimdall-frontend
install -m 755 -p "../Linux/heimdall-frontend" "%buildroot%_bindir/heimdall-frontend"
cd ..
%endif

%files
%doc heimdall/doc-pak/README
%doc heimdall/LICENSE

%_bindir/%name

%_sysconfdir/udev/rules.d/60-heimdall-galaxy-s.rules

%if_with gui
%files frontend
%_bindir/%name-frontend
%endif

%changelog
* Sun Sep 09 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.2-alt1
- Initial build for ALT Linux
