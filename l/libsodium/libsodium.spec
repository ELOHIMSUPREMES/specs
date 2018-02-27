#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: libsodium
Summary: %name
Version: 0.5.0
Release: alt1
License: ISC license
Group: System/Libraries
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Source100: %name.watch
Url: https://download.libsodium.org/libsodium/releases/

%package devel
Summary: %summary
Group: System/Libraries

%description devel
%summary

%package devel-static
Summary: %summary
Group: System/Libraries
Requires: %name-devel

%description devel-static
%summary

%package -n libsodium10
Summary: %summary
Group: System/Libraries

%description -n libsodium10
%summary

%description
%name


%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files devel
%_libdir/libsodium.so
%_libdir/pkgconfig/%name.pc
%_includedir/sodium.h
%_includedir/sodium

%files devel-static
%_libdir/libsodium.a

%files -n libsodium10
%_libdir/libsodium.so.10*

%changelog
* Wed Jun 25 2014 Denis Smirnov <mithraen@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus

