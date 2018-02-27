Name: liborcus
Version: 0.7.0
Release: alt2.1
Summary: Standalone file import filter library for spreadsheet documents

Group: System/Libraries
License: MIT
Url: http://gitorious.org/orcus
Source: %name-%version.tar.bz2
Patch: liborcus-alt-boost.patch

%define libver 0.8

# Automatically added by buildreq on Thu Jul 25 2013
# optimized out: boost-devel boost-intrusive-devel libstdc++-devel pkg-config
BuildRequires: boost-devel-headers boost-interprocess-devel boost-program_options-devel gcc-c++ zlib-devel boost-filesystem-devel mdds-devel

BuildRequires: chrpath

%description
%name is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Tools for working with Orcus
Group: Publishing

%description tools
Tools for working with Orcus.

%prep
%setup
%patch -p1

%build
sed -i 's|liborcus_@ORCUS_API_VERSION@_la_LIBADD = |& ../parser/liborcus-parser-@ORCUS_API_VERSION@.la|' src/liborcus/Makefile.am
sed -i 's/liborcus_parser_.*_la_LIBADD = /& $(BOOST_SYSTEM_LIB) /' src/parser/Makefile.am

%autoreconf

# TODO spreadsheet-model requires ixion
%configure \
	--disable-debug \
	--disable-static \
	--disable-werror \
	--with-pic \
	--with-boost \
	--with-boost-system \
	\
	--disable-spreadsheet-model

sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build V=1

%install
make install DESTDIR=%buildroot
chrpath -d %buildroot/%_libdir/*.so.*.*.*
rm -f %buildroot/%_libdir/*.la

%files
%doc AUTHORS
%_libdir/%name-*%libver.so.*

%files devel
%_includedir/%name-%libver
%_libdir/%name-*%libver.so
%_libdir/pkgconfig/%name-*%libver.pc

%files tools
%_bindir/orcus-*

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.7.0-alt2.1
- rebuild with boost 1.57.0

* Sat Jun 07 2014 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt2
- build to sisyphus

* Thu Feb 20 2014 Fr. Br. George <george@altlinux.ru> 0.7.0-alt1
- Autobuild version bump to 0.7.0
- Fix build (introduce chrpath hack)

* Thu Jul 25 2013 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Autobuild version bump to 0.5.1
- Fix underlinkage

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.0-alt1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Tue Feb 05 2013 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial build from FC

* Sat Dec 08 2012 David Tardon <dtardon@redhat.com> - 0.3.0-2
- a pointless release bump

* Fri Dec 07 2012 David Tardon <dtardon@redhat.com> - 0.3.0-1
- new release

* Sun Sep 09 2012 David Tardon <dtardon@redhat.com> - 0.1.0-1
- initial import
