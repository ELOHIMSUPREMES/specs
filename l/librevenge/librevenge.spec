
Name: librevenge
Version: 0.0.2
Release: alt1
Summary: A base library for writing document import filters
Group: System/Libraries

# src/lib/RVNGOLEStream.{h,cpp} are BSD
License: (LGPLv2+ or MPLv2.0) and BSD
Url: http://sourceforge.net/p/libwpd/wiki/librevenge/

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)

BuildRequires: boost-devel
BuildRequires: doxygen

%description
%name is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.

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
rm -rf %{buildroot}/%{_docdir}/%{name}

%check
export LD_LIBRARY_PATH=%buildroot%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make check

%files
%doc COPYING.* README NEWS
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING.*
%doc docs/doxygen/html

%changelog
* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 0.0.2-alt1
- 0.0.2

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.0.1-alt1
- initial build
