
Name: libvisio
Version: 0.0.30
Release: alt1
Summary: A library providing ability to interpret and import visio diagrams

Group: System/Libraries
License: GPLv2+ or LGPLv2+ or MPLv1.1
Url: http://www.freedesktop.org/wiki/Software/libvisio
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libwpg-0.2)
BuildRequires: pkgconfig(libwpd-0.9) pkgconfig(libwpd-stream-0.9)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(zlib)

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gperf

%description
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Visio diagrams into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Visio diagrams into other formats.
Currently supported: XHTML, raw, plain text.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS COPYING.*
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%dir %_docdir/%name
%_docdir/%name/html

%files tools
%_bindir/*

%changelog
* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.30-alt1
- initial build
