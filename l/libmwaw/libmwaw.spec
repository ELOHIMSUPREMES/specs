
Name: libmwaw
Version: 0.2.0
Release: alt1
Summary: Import library for some old mac text documents
Group: System/Libraries
# The entire source code is LGPLv2+/MPLv2.0 except
# src/lib/MWAWOLEStream.[ch]xx which are BSD. There is also
# src/tools/zip/zip.cpp which is GPLv2+, but we do not build the binary
# it is used for.
License: (LGPLv2+ or MPLv2.0) and BSD
Url: http://sourceforge.net/projects/libmwaw/
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libwpd-0.9) pkgconfig(libwpd-stream-0.9)

BuildRequires: doxygen libwpg-devel

%description
libmwaw contains some import filters for old mac text documents
(MacWrite, ClarisWorks, ... ) based on top of the libwpd (which is
already used in three word processors).

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
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform the supported formats into other formats
Group: Publishing
License: LGPLv2+
Requires: %name = %version-%release

%description tools
Tools to transform the supported document formats into other formats.
Supported output formats are XHTML, text and raw.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror --disable-zip \
    --with-sharedptr=c++11 CXXFLAGS="$CXXFLAGS -std=c++11"

%make_build

%install
%make_install install DESTDIR=%buildroot
# it seems this tool is only useful on MacOS
rm -f %buildroot/%_bindir/mwawFile

%files
%doc CHANGES COPYING.* README
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
* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.2.0-alt1
- new version

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1.10-alt1
- initial build
