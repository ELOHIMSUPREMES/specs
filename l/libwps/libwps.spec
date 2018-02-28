Name: libwps
Version: 0.4.3
Release: alt1
Summary: Library for reading and converting Microsoft Works word processor documents
License: LGPL
Group: System/Libraries
Url: http://libwps.sourceforge.net/

Source: %name-%version.tar.xz

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)

BuildRequires: doxygen
BuildRequires: gperf

%description
Library that handles Microsoft Works documents

%package tools
Summary: Tools to transform Works documents into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Works documents into other formats.
Currently supported: html, raw, text

%package devel
Summary: Files for developing with libwps
Group: Development/C++
Requires: %name = %version-%release

%description devel
Includes and definitions for developing with libwps

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
%makeinstall_std

# we install API docs directly from build
rm -rf %buildroot%_defaultdocdir/%name

%files
%_libdir/*.so.*

%files tools
%_bindir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%changelog
* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.4.3-alt1
- Autobuild version bump to 0.4.3

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 0.4.2-alt1
- Autobuild version bump to 0.4.2

* Mon Sep 21 2015 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- Autobuild version bump to 0.4.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.1
- Removed bad RPATH

* Tue Dec 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Sat Dec 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release
