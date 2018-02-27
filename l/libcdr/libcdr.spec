
Name: libcdr
Version: 0.0.14
Release: alt1
Summary: A library providing ability to interpret and import Corel Draw drawings
Group: System/Libraries
# the only Public Domain source is src/lib/CDRColorProfiles.h
License: (GPLv2+ or LGPLv2+ or MPLv1.1) and Public Domain
URL: http://www.freedesktop.org/wiki/Software/libcdr
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libwpg-0.2)
BuildRequires: pkgconfig(libwpd-0.9) pkgconfig(libwpd-stream-0.9)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(icu-i18n)

BuildRequires: boost-devel
BuildRequires: doxygen

%description
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %{name} API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Corel Draw drawings into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Corel Draw drawings into other formats.
Currently supported: XHTML, text, raw.

%prep
%setup -q

%build
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror
%make_build


%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS COPYING.* README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING.*
%dir %_docdir/%name
%_docdir/%name/html

%files tools
%_bindir/*

%changelog
* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.14-alt1
- initial build
