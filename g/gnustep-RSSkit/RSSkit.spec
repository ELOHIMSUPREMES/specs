%set_verify_elf_method unresolved=strict

Name: gnustep-RSSkit
Version: 0.4.0
Release: alt1
Summary: Simple library for reading the different types of RSS file formats
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: doxygen gnustep-gui-devel

Requires: lib%name = %EVR

%description
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

%package -n lib%name
Summary: Shared libraries of RSSKit
Group: System/Libraries

%description -n lib%name
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

This package contains shared libraries of RSSKit.

%package -n lib%name-devel
Summary: Development files of RSSKit
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

This package contains development files of RSSKit.

%package -n lib%name-devel-docs
Summary: Documentation for RSSKit
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
RSSKit is a simple library for reading the different types of
RSS file formats. It is mainly used by RSSReader.app and will
hopefully soon be used by PlopFolio by Ludovic Marcotte.

This package contains development documentation for RSSKit.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

doxygen doxygen
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for i in RSSKit; do
	lib=$(ls lib$i.so.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/0/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/0/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$i
done
popd

%files
%doc AUTHORS INTRO README TODO
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files -n lib%name-devel-docs
%doc Documentation/html/*

%changelog
* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

